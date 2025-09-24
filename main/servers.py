import asyncio 
from pickle import loads

class Server:

    async def handle_connections(self,header:str,running:int):
        try:
            file = await header.read(8192)
        #data = await header.read(8192)
        #decoding = file.decode()

            print(f'recived file chunk:{loads(file)}')

            running.write(file)
            await running.drain()

        except EOFError:
            print("all recived")
            #scritpt for writing the data
            
    async def main(self):
        server = await asyncio.start_server(
            self.handle_connections, "localhost",8000
        )

        async with server:
            await server.serve_forever()

Servers = Server()

asyncio.run(Servers.main())