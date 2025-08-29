from utils import binarysearch
from utils import checkingfile
from utils import chunks
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
corroutine = list()
corroutine2 = list()
readingqueue = asyncio.Queue()
chekedqueue= asyncio.Queue()
listqueue = asyncio.Queue()
sentinel = asyncio.Queue()
kb = 2

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

        recived = await chekedqueue.get()

        match(recived):
            case recived if(recived is not None and 
                                 recived ):
                    
                    async with aiofiles.open(recived,"rb") as opening:
                        readingmode = await opening.read(8192)
                        await readingqueue.put((recived,readingmode))
                        #print(readingqueue)
            
            case recived if(type(recived) is bool):
                print(f"\n file not found or is a folder")
            
            case recived if(recived is None):
                await sentinel.put(None)

    async def consumer(self):
        global kb

        while True:
            files = await readingqueue.get()
            #kb+=2
            await asyncio.to_thread(chunks.chunking,files[1],files[0],kb)

    async def main(self):
        #global corroutine

        choice= input("1: select one file each \n 2: choose all file \n 3: q to quit:")

        match(choice):
            case '1':
                while True:
                    self.inputed = input("insert a file:")
                    await asyncio.gather(self.block_search(listsfiles))
                    
                    await asyncio.gather(self.block_cheking(choice,self.data, current_path),self.reading())

                    #awaiting_response = await sentinel.get()#problema aqui

                    if(self.inputed == "q"):
                        break
            case '2':
                await asyncio.gather(self.block_cheking(choice,listsfiles, current_path))

                #while True:
                for _ in range(4):
                    corroutine.append(self.reading())
                    #corroutine.append(self.consumer())
                await asyncio.gather(*corroutine)

                #for _ in range(1):
                    #corroutine2.append(self.consumer())
                await asyncio.gather(self.consumer())

running= server()

asyncio.run(running.main())
#print(readingqueue)