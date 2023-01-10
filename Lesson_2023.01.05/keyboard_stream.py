import asyncio
import sys

async def proxy():
    while True:
        print("Doing the proxy thing")
        await asyncio.sleep(2)

async def main():
        # Create a StreamReader with the default buffer limit of 64 KiB.
        reader = asyncio.StreamReader()
        pipe = sys.stdin
        loop = asyncio.get_event_loop()
        await loop.connect_read_pipe(lambda: asyncio.StreamReaderProtocol(reader), pipe)

        async for line in reader:
                print(f'Got: {line.decode()!r}')

asyncio.run(main())
