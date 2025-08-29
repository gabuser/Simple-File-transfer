
def chunking(queues,names,kb:int):

    for c in range(0,len(queues),kb):
        print(names,queues[c:c+kb])