import time 

values = [c for c in range(0,299)]
counting = 20
counting2 = 0

last = len(values)-1 

def chunks():
    global counting,counting2
    while True:
        for c in range(0, len(values),20):
            yield values[counting2:0+counting]
            counting+=20
            counting2+=20
            
        if(values[last]) == last:
                break

for cp in chunks():
    time.sleep(1)
    for a in cp:
         print(a)
    #counting2+=20"""


"""a lógica para fazer o fatiamento está sendo feita de maneira manual, mas no teoria não precisa fazer isso:
o for itera sobre os valores começando do zero indo até índice 20, ele divide a lista em 20 pedaços a cada iteração e retorna
fazendo um fatiamento de listas, o número 20 especifica quantos elementos serão divididos a cada iteração, cada uma vai conter
20 elementos para ser processado. 

então ele divide a lista em 20 pedaços cada

"""