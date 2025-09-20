import asyncio


#asyncio.run(tcp_echo_client('Hello World!'))

async def handle_echo(reader, writer):
    #recebe os dados que vem do cliente e le 100 bytes por vez, é o buffer ou tamanho para conseguir abrir os dados.
    data = await reader.read(100)

    #após abrir, ele precisa decodificar de tal forma que possa ser lida e entendida.
    message = data.decode()

    #pega algumas informações do cliente
    addr = writer.get_extra_info('peername')
    
    #mostra a mensagem do endereço de quem enviou, no caso o cliente
    print(f"Received {message!r} from {addr!r}")


    print(f"Send: {message!r}")

    #salva os dados ou rescreve eles
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()

async def main():
    #inicia o servidor com a endereço e porta onde a comunicação vai ocorrer
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    #permite que o servidor rode infinitamente ou permança ligado
    async with server:
        await server.serve_forever()

asyncio.run(main())
