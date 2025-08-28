def chunks_simples(lista, tamanho_do_pedaco):
    for i in range(0, len(lista), tamanho_do_pedaco):
        yield lista[i:i + tamanho_do_pedaco]

values = [c for c in range(0,3000)]
tamanho_do_chunk = 10

for pedaco in chunks_simples(values, tamanho_do_chunk):
    print(pedaco)