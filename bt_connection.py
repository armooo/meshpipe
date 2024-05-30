import asyncio
from types import TracebackType
from typing import Iterator, Type
from bleak import BleakScanner, BleakClient, BLEDevice


SERVICE = '6ba1b218-15a8-461f-9fa8-5dcae273eafd'
FROM_RADIO = '2c55e69e-4993-11ed-b878-0242ac120002'
TO_RADIO = 'f75c76d2-129e-4dad-a1dd-7866124401e7'
CURRENT_PACKET_NUM = 'ed9da18c-a800-4f66-a670-aa7547e34453'


class BTConnection:
    def __init__(self, device: BLEDevice):
        self._name = device.name
        self._client = BleakClient(device)
        self._stop = False
        self._read_ready = asyncio.Event()

    def __repr__(self):
        return f'BTConnection<{self._name}>'

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException],
        exc_val: BaseException,
        exc_tb: TracebackType,
    ) -> None:
        await self.disconnect()

    async def connect(self):
        await self._client.connect()

    async def disconnect(self):
        await self._client.disconnect()

    async def read(self) -> Iterator[bytes]:
        await self._client.start_notify(CURRENT_PACKET_NUM, lambda _, __: self._read_ready.set())

        while not self._stop:
            while data := await self._client.read_gatt_char(FROM_RADIO):
                yield bytes(data)
            await self._read_ready.wait()
            self._read_ready.clear()

    async def write(self, msg: bytes):
        await self._client.write_gatt_char(TO_RADIO, msg, response=False)


async def find_first_device() -> BLEDevice:
    device = None
    async with BleakScanner(service_uuids=[SERVICE]) as scanner:
        async for device, data in scanner.advertisement_data():
            return device
