def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    topo_esquerda, topo_direita = 0, 0
    for k in range(inicio, fim):
        if topo_esquerda >= len(esquerda):
            lista[k] = direita[topo_direita]
            topo_direita = topo_direita + 1
        elif topo_direita >= len(direita):
            lista[k] = esquerda[topo_esquerda]
            topo_esquerda = topo_esquerda + 1
        elif esquerda[topo_esquerda] < direita[topo_direita]:
            lista[k] = esquerda[topo_esquerda]
            topo_esquerda = topo_esquerda + 1
        else:
            lista[k] = direita[topo_direita]
            topo_direita = topo_direita + 1

lista = [7, 23, 14, 56, 2, 49, 30, 11, 85, 42, 6, 17, 98, 5, 71, 33]
print(f'Antes da ordenação: {lista}')
mergesort(lista)
print(f'Depois da ordenação: {lista}')