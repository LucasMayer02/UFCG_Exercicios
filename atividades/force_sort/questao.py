# 2021-04-21, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função força a lista a ficar em ordem crescente 
# e retorna uma lista mostrando onde acontece mudança

def force_sort(seq) :
    if len(seq) == 0 :
        return []
    resultado = [0]
    for i in range(1, len(seq)) :
        if seq[i] < seq[i-1] :
            resultado.append(seq[i-1] - seq[i])
            seq[i] = seq[i-1]
        else :
            resultado.append(0)
    return resultado
