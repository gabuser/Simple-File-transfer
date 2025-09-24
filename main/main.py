from utils import binarysearch
from utils import checkingfile
from utils import chunks
from os import chdir,listdir,getcwd
from os import path
import asyncio 
import aiofiles
from pickle import dumps
#paths = getcwd()

#directory = chdir(f"{paths}/main/utils")
directory = input("inset the path u want to copy file:")
chdir(directory)
listsfiles = iter(listdir(directory))
current_path = getcwd()
corroutine = list()
corroutine2 = list()
readingqueue = asyncio.Queue()
chekedqueue= asyncio.Queue()
listqueue = asyncio.Queue()
sentinel = asyncio.Queue()
consumer = asyncio.Queue()

kb = 8192

class Client:
    async def block_search(self,lists:list):
        self.data = await asyncio.to_thread(binarysearch.searchfile,self.inputed, lists)
        #print(self.data)
        #self.order = self.data.split(" ")

    async def producer(self,values:list|str,option:str):

        match(option):
            case "1":
                self.inputed = values
                
                if(self.inputed and self.inputed != "q"):
                    await listqueue.put(self.inputed)
                    #encerrar as corroutines de forma segura
                await listqueue.put(None)
        
                #else:
                 #   await listqueue.put(None)
            
            case "2":
                while True:
                    try:
                        value = next(listsfiles)
                        await listqueue.put(value)
                    
                    except StopIteration:
                        #await listqueue.put(None)
                        break

    async def chekingfiles(self, dire:str):
        while True:
            #print(listqueue.task_done())
            tobecheck = await listqueue.get()
            listqueue.task_done()
            cheked = await asyncio.to_thread(checkingfile.checking, dire, tobecheck )
            #await chekedqueue.put(cheked)
            
            if(cheked and cheked is not None):
                await chekedqueue.put(cheked)
            

            if(tobecheck is None):
                #listqueue.task_done()
                await chekedqueue.put(None)
                break
            #print(listqueue)

    async def reading(self):
        while True:    
            recived = await chekedqueue.get()
            chekedqueue.task_done()

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
                    #await readingqueue.put(None)
                    break
    
    async def chunking(self):
        global kb

        while True:
            files = await readingqueue.get()
            readingqueue.task_done()

            if(files is not None):
                for c in range(0,len(files[1]),kb):

                    await consumer.put((files[0],files[1][c:c+kb]))

            if(files is None):
                await consumer.put(None)
                break

    async def sending(self,PORT:int, address:str):
        recived,sender = await asyncio.open_connection(
            address,PORT
        )

        while True:
            value = await consumer.get()
            consumer.task_done()
            #if(value is not None):
                #print(value[1])
            
            if(value is not None):

                #print(f'sending:{value[0]}')
                sender.write(dumps(value))
                await sender.drain()
                #await sender.drain()

                torecive= await recived.read(kb)
                print(f'downloading:{torecive}')

                sender.close()
                await sender.wait_closed()
            
            if(value is None):
                print(consumer)
                break

    async def main(self):
        choice= input("1: select one file each \n 2: choose all file \n 3: q to quit:")

        match(choice):
            case '1':
                while True:
                    self.inputed = await asyncio.to_thread(input,"insert a file:")
                    await asyncio.gather(self.block_search(listsfiles))

                    await asyncio.gather(self.producer(self.inputed,choice))
                    
                    await asyncio.gather(self.chekingfiles(current_path))
                    await asyncio.gather(self.reading())
                    await asyncio.gather(self.chunking(),self.sending())
                    if(self.inputed == "q"):
                        break
            
            case '2':
                producers= list()
                consumers = list()
                readers = list()
                chunkers = list()
                senders = list()

                
                for _ in range(5):
                    producers.append(self.producer(listsfiles,choice))
                    consumers.append(self.chekingfiles(current_path))
                    readers.append(self.reading())
                    chunkers.append(self.chunking())
                    senders.append(self.sending(8000,"localhost"))
                
                await asyncio.gather(*producers)
                for _ in range(5):
                    await listqueue.put(None)
                
                await asyncio.gather(*consumers,*readers)

                for _ in range(5):
                    await readingqueue.put(None)
                
                await asyncio.gather(*chunkers)
                await asyncio.gather(*senders)
                #await asyncio.gather(self.chekingfiles(current_path))
                #await asyncio.gather(self.chekingfiles(current_path))
                #await asyncio.gather(*readers)
                #await asyncio.gather(*chunkers)
                #await asyncio.gather(*senders)
                """await asyncio.gather(self.block_cheking(choice,listsfiles, current_path))

                #while True:
                for _ in range(9):
                    corroutine.append(self.reading())
                    #corroutine.append(self.consumer())
                await asyncio.gather(*corroutine)

                for _ in range(10):
                    corroutine2.append(self.consumer())
                    corroutine2.append(self.producer())
                
                await asyncio.gather(*corroutine2, self.producer())
                #await asyncio.gather(self.producer())"""
                

running= Client()

asyncio.run(running.main())


#melhorar chunk, atualmente está totalmente simplificada, rodando apenas em uma core, o que garante a ordem das chunks dos arquivos, mas altera a parformace ao decorrer do tempo.
#garantir o offset das chunks, de tal forma que quando chegar no dispositivo B, ele possa reorganziar a ordem das chunks para fazer a reconstrução dos dados.
#melhorar o modelo de produtor consumidor

#problema é que o chekingfile não está contando ou melhor consumindo todos as sentinelas, como os valores estao ordenados, 
#ele consome os 3 primerios valores que são os arquivos e quando ela se depara com o none, ela fecha de forma incorreta. 
