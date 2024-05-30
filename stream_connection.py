import asyncio
from types import TracebackType
from typing import Iterator, Type

MAGIC = b'\x94\xC3'

class Connection:
    def __init__(self):
        self._stop = False

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
        raise NotImplementedError

    async def disconnect(self):
        self._writer.close()
        await self._writer.wait_closed()

    async def read(self) -> Iterator[bytes]:
        while not self._stop:
            await self._reader.readuntil(MAGIC)
            proto_len = int.from_bytes(await self._reader.readexactly(2), 'big')
            yield await self._reader.readexactly(proto_len)

    async def write(self, msg: bytes):
        print('write')
        self._writer.write(MAGIC)
        self._writer.write(len(msg).to_bytes(2, 'big', signed=False))
        self._writer.write(msg)
        await self._writer.drain()
