# 2021-04-15, lucas.mayer.almeida@ccc.ufcg.edu.br
# Inverte os k primeiros elementos e os coloca no final da lista

def flipmove(lista, k) :
    resq = 0
    for i in range(k) :
        cont = k - resq -1
        j = 0
        while cont > 0 :
            lista[j], lista[j+1] = lista[j+1], lista[j]
            j += 1
            cont -= 1
        resq += 1
    for i in range(k) :
        lista.append(lista[0])
        lista.pop(0)
