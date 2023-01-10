import asyncio
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


async def read_chat(reader):
    while True:
        data = await reader.read(100)
        print(data.decode())


async def tcp_chat_client():
    user_name = input("Please enter your name: ")

    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    writer.write((bcolors.OKGREEN + user_name + bcolors.ENDC).encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'{data.decode()}')

    keyboard_reader = asyncio.StreamReader()
    pipe = sys.stdin
    loop = asyncio.get_event_loop()
    loop.create_task(read_chat(reader=reader))
    await loop.connect_read_pipe(lambda: asyncio.StreamReaderProtocol(keyboard_reader), pipe)

    async for line in keyboard_reader:
        stripped_line = f"{bcolors.BOLD}{line.decode().strip()}{bcolors.ENDC}"
        writer.write(stripped_line.encode())
        await writer.drain()

asyncio.run(tcp_chat_client())
