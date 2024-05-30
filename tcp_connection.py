import asyncio

import stream_connection

class TCPConnection(stream_connection.Connection):
    def __init__(self, host: str, port: int):
        stream_connection.Connection.__init__(self)
        self._host = host
        self._port = port

    def __repr__(self):
        return f'TCPConnection<{self._host}:{self._port}>'

    async def connect(self):
        self._reader, self._writer = await asyncio.open_connection(self._host, self._port)
