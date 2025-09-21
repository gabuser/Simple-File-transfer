import asyncio

async def tcp_echo_client(message):
    #função cliente que vai abrir uma conexão, isso é, tentar se conectar ao servidor no endereço e porta fornecido
    reader, writer = await asyncio.open_connection(
        'localhost', 8888)
    
    #emula uma notificação de mensagem que vai ser enviada
    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    #emula a parte que foi recebida, como se fosse uma conexão falando que chegou
    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')

    #fecha a conexão 
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client("hello world"))