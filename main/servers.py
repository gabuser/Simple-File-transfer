import asyncio 
import aiofiles
from pickle import loads

class Server:

    async def handle_connections(self,header:str,running:int):
        try:
            file = await header.read(8192)
            running.write(file)
            await running.drain()

        #data = await header.read(8192)
        #decoding = file.decode()
            data = loads(file)
            #print(data[1])
            async with aiofiles.open(data[0],"a") as save:
                await save.write(data[1])

            #running.write(file)
            #await running.drain()

            """async with open(file[0],"a") as saving:
                await saving.write(file[1])"""

        except EOFError:
            pass
            #scritpt for writing the data
            
    async def main(self):
        server = await asyncio.start_server(
            self.handle_connections, "localhost",8000
        )

        async with server:
            await server.serve_forever()

Servers = Server()

asyncio.run(Servers.main())