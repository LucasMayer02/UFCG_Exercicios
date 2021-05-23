# 2021-04-15, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função distribui os elementos de uma lista em n diferentes listas

def distribui_materia_prima(esteira_de_materia_prima, n) :
    lista_esteiras = []
    for i in range(n) :
        lista_esteiras.append([])
    pos = 0
    for i in range(len(esteira_de_materia_prima)) :
        lista_esteiras[pos].append(esteira_de_materia_prima[i])
        pos += 1
        if pos == n :
            pos = 0
    return lista_esteiras
