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
corroutines:list
readingqueue = asyncio.Queue()
chekingqueue = asyncio.Queue()
listqueue = asyncio.Queue()

class server:
    async def block_search(self,lists:list):
        self.data = await asyncio.to_thread(binarysearch.searchfile,self.inputed, lists)

    async def block_cheking(self,values:str|list, dire:str):
        
        for value in values:
            await listqueue.put(value)
        
        for _ in range(len(values)):
            self.value = await asyncio.to_thread(checkingfile.checking,dire,await listqueue.get())
            
    async def reading(self,onefile:str|list):
            
        match(onefile):
            case onefile if(type(onefile)) is str:
                async with aiofiles.open(onefile,"rb") as opening:
                    readingmode = await opening.read()
                    await readingqueue.put((onefile,readingmode))
                    print(readingqueue)
            
            case onefile if(type(onefile)) is list:
                #print(True)
                pass

    async def main(self):
        choice= input("1: select one file each \n 2: choose all file \n 3: q to quit:")

        match(choice):
            case '1':
                while True:
                    self.inputed = input("insert a file:")
                    await asyncio.gather(self.block_search(listsfiles))
                    await asyncio.gather(self.block_cheking(self.data, current_path))
                    await asyncio.gather(self.reading(self.data))
                    #await self.block(listsfiles,current_path)
                    #await self.reading(self.data)
        
            case '2':
                await asyncio.gather(self.block_cheking(listsfiles, current_path))
                await asyncio.gather(self.reading(listsfiles))

running= server()

asyncio.run(running.main())
    