import asyncio 


listas = iter([c for c in range(0,200)])
print(listas)

producers = asyncio.Queue()

async def producer():
        while True:
            try:
                await producers.put(next(listas))
            
            except StopIteration:
                for _ in range(4):
                    await producers.put(None)
                break
    

async def consumer():
    while True:
        value = await producers.get()
        print(value)

        if(value is None):
            break

async def main():
    cproducer = list()
    cconsumer = list()

    for _ in range(4):
        cproducer.append(producer())
    
    for _ in range(3):
        cconsumer.append(consumer())
    
    await asyncio.gather(*cproducer)
    await asyncio.gather(*cconsumer)

asyncio.run(main())