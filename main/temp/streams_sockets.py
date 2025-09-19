import asyncio 

async def tcp_echo(message):
    reciver, sender = await asyncio.open_connection(
        'localhost',8000)

    print(f'sending:{message}')
    sender.write(message.encode())
    await sender.drain()

    data = await reciver.read(100)
    print(f'recived:{data.decode()}')

    sender.close()
    await sender.wait_closed()

asyncio.run(tcp_echo('hello world'))
