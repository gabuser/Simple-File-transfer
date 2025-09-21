import asyncio 

class Server:

    async def handle_connections(self,host:str,running:int):
        data = await host.read(8192)
        decoding = data.decode()

        print(f'recived file chunk:{decoding!r}')

        running.write(data)
        await running.drain()

        running.close()
        await running.wait_closed()

    async def main(self):
        server = await asyncio.start_server(
            self.handle_connections, "localhost",8000
        )

        async with server:
            await server.serve_forever()

Servers = Server()

asyncio.run(Servers.main())