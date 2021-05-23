# 2021-04-14, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função remove os últimos n numeros divisores de k 

def remove_divisores_k(lista, k, n) :
    provisorio = lista.copy()
    for i in range(len(provisorio) -1, -1, -1) :
        if k % provisorio[i] == 0 and n > 0:
            lista.pop(i)
            n -= 1
