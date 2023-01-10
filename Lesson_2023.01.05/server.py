import asyncio

users: dict[str: (asyncio.ReadTransport, asyncio.WriteTransport)] = {}

async def post_all(data: str):
    delete = []
    for user in users:
        print(f">{user}  {data}")
        user_writer: asyncio.WriteTransport = users[user][1]
        if user_writer.is_closing():
            print(f"                 {user} IS CLOSED")
            delete.append(user)
        else:
            user_writer.write(data.encode())
            await user_writer.drain()
    for i in delete:
        del users[i]

async def handle_echo(reader: asyncio.ReadTransport, writer: asyncio.WriteTransport):
    data = await reader.read(100)
    username = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Added new user {username!r} from {addr!r}")

    users[username] = (reader, writer)

    print(f"New user joined: {username}")

    await post_all(f"Welcome {username}")
    
    while True:
        try:
            message_data = await reader.read(100)
            message = message_data.decode().strip()
            print(f"Number of users: {len(users)}")
            if message == 'exit':
                await post_all(f"Good Bye {username}")
                print("Close the connection")
                writer.close()
                break
            else:
                await post_all(f"{username} -> {message}")
        except Exception as e:
            print(f"ERROR: {e}")
            break

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
