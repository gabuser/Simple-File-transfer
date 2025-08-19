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

async def block(datas:str,lists:list,dire:str):
    data = await asyncio.to_thread(binarysearch.searchfile,datas, lists)

    value = await asyncio.to_thread(checkingfile.checking,dire,data)

    if(value):
        return data

async def reading(onefile:str|list):
    match(onefile):
        case onefile if(type(onefile)) is str:
            async with aiofiles.open(onefile,"rb") as opening:
                readingmode = await opening.read()
            print(readingmode)

async def main():
    while True:
        inputed = input("insert a file:")
        #main(inputed)
        onefile = await asyncio.gather(block(inputed, listsfiles,current_path))
        #print(onefile)
        await asyncio.gather(reading(onefile[0]))

asyncio.run(main())
    