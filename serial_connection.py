import serial_asyncio

import stream_connection

class Connection(stream_connection.Connection):
    def __init__(self, path: str):
        stream_connection.Connection.__init__(self)
        self._path = path

    async def connect(self):
        self._reader, self._writer = await serial_asyncio.open_serial_connection(
            url=self._path,
            baudrate=115200,
        )

