
def chunking(queues,kb:int):

    for c in range(0,len(queues),kb):
        print(queues[c:c+kb])