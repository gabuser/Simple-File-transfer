def searchfile(file:str,path:list) ->str| bool:
    appendfiles = list()
    fileslists =sorted(path)
    
    starts = 0 
    endlist = len(list(path))-1 

    if(file !="q"):
        while(starts <= endlist):
            halfstart= (starts+endlist)//2 
            foundfile = (fileslists[halfstart])

            if(foundfile == file):
                appendfiles.append(file)
                return appendfiles
        
            if(foundfile <file):
                starts = halfstart+1
        
            else:
                endlist = halfstart -1
    
        return False
    
    else:
        return file

#print(searchfile('.py',path=getcwd()))
