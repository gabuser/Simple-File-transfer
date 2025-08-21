from utils import binarysearch
from utils import checkingfile
from os import chdir,listdir,getcwd
from os import path
import asyncio 
import aiofiles

#paths = getcwd()

#directory = chdir(f"{paths}/main/utils")
directory = input("inset the path u want to copy file:")
chdir(directory)
listsfiles = listdir(directory)
current_path = getcwd()
corroutine:list
readingqueue = asyncio.Queue()
chekedqueue= asyncio.Queue()
listqueue = asyncio.Queue()

class server:
    async def block_search(self,lists:list):
        self.data = await asyncio.to_thread(binarysearch.searchfile,self.inputed, lists)
        self.order = self.data.split(" ")

    async def block_cheking(self,values:list|str, dire:str):
        
        for value in values:
            await listqueue.put(value)
        
        for _ in range(len(values)):
            self.value = await asyncio.to_thread(checkingfile.checking,dire,await listqueue.get())

            if(self.value):
                await chekedqueue.put(self.value)

    async def reading(self):
        self.recived = await chekedqueue.get()

        if(self.recived is not None):
            async with aiofiles.open(self.recived,"rb") as opening:
                readingmode = await opening.read()
                await readingqueue.put((self.recived,readingmode))
                print(readingqueue)
                
    async def main(self):
        choice= input("1: select one file each \n 2: choose all file \n 3: q to quit:")

        match(choice):
            case '1':
                while True:
                    self.inputed = input("insert a file:")
                    await asyncio.gather(self.block_search(listsfiles))
                    await asyncio.gather(self.block_cheking(self.order, current_path),self.reading())
                    #await asyncio.gather(self.reading())
                    #await self.block(listsfiles,current_path)
                    #await self.reading(self.data)
        
            case '2':
                await asyncio.gather(self.block_cheking(listsfiles, current_path))

                while True:
                    await asyncio.gather(self.reading())

                    if(self.recived is None):
                        break
running= server()

asyncio.run(running.main())
    