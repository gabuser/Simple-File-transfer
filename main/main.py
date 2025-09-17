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
listsfiles = iter(listdir(directory))
current_path = getcwd()
corroutine = list()
corroutine2 = list()
readingqueue = asyncio.Queue()
chekedqueue= asyncio.Queue()
listqueue = asyncio.Queue()
sentinel = asyncio.Queue()
consumer = asyncio.Queue()

kb = 2

class server:
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
                #print(listqueue)
                #lembrete de gerenciar as corroutines para que possam ser encerradas de forma segura
            #for _ in range(len(values)):
                #self.value = await asyncio.to_thread(checkingfile.checking,dire,await listqueue.get())

                #if(self.value):
                 #   await chekedqueue.put(self.value)
                
        #self.inputed="q"
    
    async def chekingfiles(self, dire:str):
        #lenghts = listqueue.qsize()
        #while True:
        #tobecheck= await listqueue.get()
        #for _ in range(lenghts):
        #listqueue.task_done()
        #value=await listqueue.get()
        #print(value)
            
        #print(listqueue)
        #print(chekedqueue)
        #print(lenghts)
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
                break
            #print(listqueue)
        
        print(listqueue)

    """match(option):

                case "1":
                    if(self.inputed == "q"):
                        await chekedqueue.put(None)
                    
                    if(not self.value):
                     await chekedqueue.put(False)
                
                case "2":
                    #needs to be fixed
                    #for _ in range(3):
                    await chekedqueue.put(None)
        else:
         await chekedqueue.put(False)"""

        #print(chekedqueue)
    async def reading(self,corroutine=1):
        while True:    
            recived = await chekedqueue.get()
            
            match(recived):
                case recived if(recived is not None and
                                 recived ):
                    
                        async with aiofiles.open(recived,"rb") as opening:
                            readingmode = await opening.read(8192)
                            await readingqueue.put((recived,readingmode))
                        print(readingqueue)
            
                case recived if(type(recived) is bool):
                    print(f"\n file not found or is a folder")
            
                case recived if(recived is None):
                    for _ in range(corroutine):
                        #await chekedqueue.put(None)
                        await sentinel.put(None)
                        #print(sentinel)
                    break

        print(sentinel)
    

    async def chunking(self,corroutine=1):
        global kb

        while True:
            files = await readingqueue.get()
            #sentinels = await sentinel.get()
            #print(sentinels)
            #print(files[1])
            #print(readingqueue)
            #kb+=2
            
            #for c in await asyncio.to_thread(chunks.chunking,files[1],files[0],kb):
            for c in range(0,len(files[1]),kb):

                await consumer.put((files[0],files[1][c:c+kb]))
            
            if(files is None):
                print(consumer)
                for _ in range(corroutine):
                    await consumer.put(None)
                    print(consumer)
                break
    
    async def sending(self):
            while True:
                value = await consumer.get()
                print(value)

                if(value is None):
                  break


            #print(value.index(value[1]))
            #print(value[1])
    async def main(self):
        #global corroutine
        
        choice= input("1: select one file each \n 2: choose all file \n 3: q to quit:")

        match(choice):
            case '1':
                while True:
                    self.inputed = await asyncio.to_thread(input,"insert a file:")
                    await asyncio.gather(self.block_search(listsfiles))

                    await asyncio.gather(self.producer(self.inputed,choice))
                    
                    await asyncio.gather(self.chekingfiles(current_path))
                    await asyncio.gather(self.reading())
                    #await asyncio.gather(self.chunking())
                    #print(consumer)
                    #await asyncio.gather(self.sending())
                    #await asyncio.gather(self.block_cheking(choice,self.data, current_path),self.reading())

                    #awaiting_response = await sentinel.get()#problema aqui

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
                
                #await asyncio.gather(*producers)
                #await asyncio.gather(self.chekingfiles(current_path))
                
                a = 5
                for _ in range(5):
                   consumers.append(self.chekingfiles(current_path))
                #for _ in range(a):
                 #   readers.append(self.reading(a))
                
                #await asyncio.gather(*readers)

                #for _ in range(a):
                 #  chunkers.append(self.chunking(a))
                
                #await asyncio.gather(*chunkers)

                #for _ in range(_):
                 #   senders.append(self.sending())
                
                await asyncio.gather(*producers)
                for _ in range(5):
                    await listqueue.put(None)
                
                await asyncio.gather(*readers)

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
                

running= server()

asyncio.run(running.main())


#melhorar chunk, atualmente está totalmente simplificada, rodando apenas em uma core, o que garante a ordem das chunks dos arquivos, mas altera a parformace ao decorrer do tempo.
#garantir o offset das chunks, de tal forma que quando chegar no dispositivo B, ele possa reorganziar a ordem das chunks para fazer a reconstrução dos dados.
#melhorar o modelo de produtor consumidor

#problema é que o chekingfile não está contando ou melhor consumindo todos as sentinelas, como os valores estao ordenados, 
#ele consome os 3 primerios valores que são os arquivos e quando ela se depara com o none, ela fecha de forma incorreta. 
