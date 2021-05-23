# 2021-04-15, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função adiciona um item e mantem a lista em ordem alfabetica

def adiciona_item(item, lista) :
    lista.append(item)
    provisorio = lista.copy()
    resq = 0
    for i in range(len(provisorio)) :
        if provisorio[i] > item :
           lista.append(provisorio[i])
           lista.pop(i - resq)
           resq += 1
    return lista
