from utils import binarysearch
from utils import checkingfile
from os import chdir,listdir,getcwd
from os import path
import asyncio 

paths = getcwd()

#directory = chdir(f"{paths}/main/utils")
directory = input("inset the path u want to copy file:")
chdir(directory)
listsfiles = listdir(directory)
current_path = getcwd()

async def block(datas:str,lists:list,dire:str):
    data = await asyncio.to_thread(binarysearch.searchfile,datas, lists)

    value = await asyncio.to_thread(checkingfile.checking,dire,data)
    print(data)
    print(value)

async def main():
    while True:
        inputed = input("insert a file:")
        #main(inputed)
        await asyncio.gather(block(inputed, listsfiles,current_path))

asyncio.run(main())
    