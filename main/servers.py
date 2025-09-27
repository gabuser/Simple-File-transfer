import asyncio 
import aiofiles
from pickle import loads

class Server:

    async def handle_connections(self,header:str,running:int):
        try:
            #file = await header.read(8192)
            filebinary= await header.readuntil(b'\n')
            filetext = filebinary.decode()

            content = await header.read(8192)
            #filename = unpack("!Q",file)
            async with aiofiles.open(filetext.replace("\n",""),"ab") as save:
                await save.write(content)
            
            running.write(filebinary)
            await running.drain()

            #running.close()
            #await running.wait_closed()
        #data = await header.read(8192)
        #decoding = file.decode()
            #data = loads(file[1])
            #print(data[1])
            """async with aiofiles.open(filename,"a") as save:
                await save.write(data)"""

            #running.write(file)
            #await running.drain()

            """async with open(file[0],"a") as saving:
                await saving.write(file[1])"""

        except EOFError:
            pass
            #scritpt for writing the data
            
    async def main(self,host):
        server = await asyncio.start_server(
            self.handle_connections, host,8000
        )

        async with server:
            await server.serve_forever()

Servers = Server()
host = input("insert the host:")
asyncio.run(Servers.main(host))
#precisar enviar o tamanho do arquivo binário de tal forma que uma não sobreponha ou leia a parte do outro e causar deadlocks