import asyncio
import argparse
import contextlib
import time

from bleak import BleakScanner, BleakClient, BLEDevice

from bt_connection import BTConnection, SERVICE
from tcp_connection import TCPConnection
from client import Client
from meshtastic.mqtt_pb2 import ServiceEnvelope
from meshtastic.mesh_pb2 import ToRadio


MAX_PACKET_AGE = 10 * 60
MAX_PACKETS = 10000
PACKETS_SEEN = {}


def add_packet_id(packet_id):
    global PACKETS_SEEN
    PACKETS_SEEN[packet_id] = time.monotonic() + MAX_PACKET_AGE
    if len(PACKETS_SEEN) > MAX_PACKET_AGE:
        PACKETS_SEEN = {
            packet_id: exp_time for packet_id, exp_time in PACKETS_SEEN.items()
            if exp_time > time.monotonic()
        }


def has_seen_packet_id(packet_id):
    if not packet_id in PACKETS_SEEN:
        return False
    return PACKETS_SEEN[packet_id] < time.monotonic()


async def make_bt_clients(names):
    names = list(names)
    clients = []
    async with BleakScanner(service_uuids=[SERVICE]) as scanner:
        async for device, _ in scanner.advertisement_data():
            if device.name in names:
                clients.append(Client(BTConnection(device)))
                names.remove(device.name)
            if not names:
                break
    return clients


async def make_tcp_clients(ips):
    return [
        Client(TCPConnection(ip, 4403))
        for ip in ips
    ]


async def pipe(src, dests):
    print(f'Starting pipe {src} -> {dests}')
    async for fr in src.read():
        if not fr.HasField('mqttClientProxyMessage'):
            continue
        if not fr.mqttClientProxyMessage.HasField('data'):
            continue
        # Assume device has decrypted for us
        se = ServiceEnvelope.FromString(fr.mqttClientProxyMessage.data)
        packet = se.packet
        print('Got packet', packet)
        if has_seen_packet_id(packet.id):
            continue
        add_packet_id(packet.id)
        packet.hop_limit += 1
        for dest in dests:
            async with asyncio.TaskGroup() as tg:
                print(f'Sending packet out the pipe -> {dest}')
                tr = ToRadio()
                tr.packet.CopyFrom(packet)
                tg.create_task(dest.write(tr))


async def main(args):
    clients = await make_bt_clients(args.bt)
    clients.extend(await make_tcp_clients(args.tcp))

    async with contextlib.AsyncExitStack() as stack:
        open_clients = [await stack.enter_async_context(c) for c in clients]

        print('Loading configs')
        async with asyncio.TaskGroup() as tg:
            for client in open_clients:
                # we don't care aboutt the config but we to get it
                # before we will get data pushed to us
                tg.create_task(client.get_config())
        print('Configs loaded')

        async with asyncio.TaskGroup() as tg:
            for src in open_clients:
                dests = open_clients[:]
                dests.remove(src)
                tg.create_task(pipe(src, dests))


if __name__ == '__main__':
    parser = argparse.ArgumentParser('meshview')
    parser.add_argument('--bt', nargs='*', default=())
    parser.add_argument('--tcp', nargs='*', default=())
    args = parser.parse_args()
    asyncio.run(main(args))
