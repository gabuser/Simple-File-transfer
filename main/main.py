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
sentinel = asyncio.Queue()

class server:
    async def block_search(self,lists:list):
        self.data = await asyncio.to_thread(binarysearch.searchfile,self.inputed, lists)
        #print(self.data)
        #self.order = self.data.split(" ")

    async def block_cheking(self,option:str,values:list|str, dire:str):

        self.inputed = values

        if(self.inputed):
            for value in values:
                await listqueue.put(value)
        
            for _ in range(len(values)):
                self.value = await asyncio.to_thread(checkingfile.checking,dire,await listqueue.get())

                if(self.value):
                    await chekedqueue.put(self.value)
                
        #self.inputed="q"
            match(option):

                case "1":
                    if(self.inputed == "q"):
                        await chekedqueue.put(None)
                    
                    if(not self.value):
                        await chekedqueue.put(False)
                case "2":
                    await chekedqueue.put(None)
        else:
         await chekedqueue.put(False)

        #print(chekedqueue)
    async def reading(self):
        self.recived = await chekedqueue.get()

        match(self.recived):
            case self.recived if(self.recived is not None and 
                                 self.recived ):
                    
                    async with aiofiles.open(self.recived,"rb") as opening:
                        readingmode = await opening.read()
                        await readingqueue.put((self.recived,readingmode))
                        print(readingqueue)
            
            case self.recived if(type(self.recived) is bool):
                print(f"\n file not found or is a folder")
                
    async def main(self):
        choice= input("1: select one file each \n 2: choose all file \n 3: q to quit:")

        match(choice):
            case '1':
                while True:
                    self.inputed = input("insert a file:")
                    await asyncio.gather(self.block_search(listsfiles))
                    await asyncio.gather(self.block_cheking(choice,self.data, current_path),self.reading())
                    
                    if(self.recived is None):
                        break
                    

            case '2':
                await asyncio.gather(self.block_cheking(choice,listsfiles, current_path))

                while True:
                    await asyncio.gather(self.reading())
                    if(self.recived is None):
                        break
running= server()

asyncio.run(running.main())
    