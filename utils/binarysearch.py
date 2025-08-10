from os import listdir,getcwd


def searchfile(file:str,path:str) ->str| bool:
    #list of directorys and files to be search
    fileslists = sorted(listdir(path))
    
    starts = 0 
    endlist = len(fileslists)-1 

    while(starts <= endlist):
        halfstart= (starts+endlist)//2 
        foundfile = fileslists[halfstart]

        if(foundfile == file):
            return foundfile
        
        if(foundfile <file):
            starts = halfstart+1
        
        else:
            endlist = halfstart -1
    
    return False

#print(searchfile('.py',path=getcwd()))
