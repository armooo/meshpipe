import asyncio
import random
from types import TracebackType
from typing import Iterator, Type

from meshtastic.mesh_pb2 import ToRadio
from meshtastic.mesh_pb2 import FromRadio
from meshtastic.portnums_pb2 import PortNum
from meshtastic.telemetry_pb2 import Telemetry


class Message:
    def __init__(self, from_radio):
        self.from_radio = from_radio
        if self.from_radio.HasField(""):
            pass


class Client:
    def __init__(self, connection):
        self._connecion = connection
        self._stop = False

    def __repr__(self):
        return f'Client<{self._connecion!r}>'

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
        await self._connecion.connect()

    async def disconnect(self):
        await self._connecion.disconnect()

    async def read(self) -> Iterator[FromRadio]:
        while not self._stop:
            async for msg in self._connecion.read():
                yield FromRadio.FromString(msg)

    async def write(self, proto: ToRadio):
        await self._connecion.write(proto.SerializeToString())

    async def get_config(self) -> list[FromRadio]:
        nonce = random.randint(0, 2**32)
        config = []
        await self.write(ToRadio(want_config_id=nonce))
        async for proto in self.read():
            if proto.config_complete_id == nonce:
                break
            config.append(proto)
        return config
