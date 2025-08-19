from os import path

"""paths = getcwd()
exists = binarysearch.searchfile('ut',paths)

print(path.isfile(exists))"""

def checking(paths:str,files="")->bool:
    if(files):
        #print(f"{paths}\{files}")
        return path.isfile(f"{paths}\{files}")
    
"""
algoritmo de busca binária será reutilizada duas vezes, a primeira vez iremos usar para buscar os arquivos que o usuário que mandar para outro dispositivo 
e a segunda vez será usada para verificar se o arquivo que o usuário quer enviar é de fato um arquivo. 

para isso precisamos listar os arquivos com os.listdir no arquivo main, onde essas ferramentas serão executadas antes de qualquer operação assíncrona
listas de arquivos dentro do diretório será criada apenas uma vez e reutilizada apenas uma vez cada.

mudanças:

a busca e a verificação dos arquivos vão ocorrer em duas threads diferentes, enquanto ele busca um arquivo ja verifica outro sem atrapalhar e envia para para parte assíncrona
"""