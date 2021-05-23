# 2021-04-08, lucas.mayer.almeida@ccc.ufcg.edu.br
# Imprime os valores nas posições indicadas pelo indice

valores = [18, 22, 73, 32, 19, 21, 43]
indices = [3, 4, 8, 1]

def get_items(valores, indices) :
    lista = []
    for n in indices :
        if n >= len(valores) :
            lista.append(None)
        else :
            lista.append(valores[n])
    return lista

