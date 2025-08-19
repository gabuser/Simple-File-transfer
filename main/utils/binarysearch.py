def searchfile(file:str,path:list) ->str| bool:
    #list of directorys and files to be search
    fileslists = sorted(path)
    
    starts = 0 
    endlist = len(path)-1 

    while(starts <= endlist):
        halfstart= (starts+endlist)//2 
        foundfile = (fileslists[halfstart])

        if(foundfile == file):
            return file
        
        if(foundfile <file):
            starts = halfstart+1
        
        else:
            endlist = halfstart -1
    
    return f'arquivo não foi encontrado'

#print(searchfile('.py',path=getcwd()))
