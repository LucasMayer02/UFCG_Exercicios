# 2021-05-06, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função retorna uma lista com os netos de fulano

def netos(fulano, pais) :
    filhos = []
    netos = []
    for k in pais.keys() :
        if fulano in pais[k] :
            filhos.append(k)
    for i in filhos :
        for k in pais.keys() :
            if i in pais[k]:
                netos.append(k)
    for i in range(len(netos)) :
        j = i
        while j > 0 and netos[j] < netos[j-1] :
            netos[j], netos[j-1] = netos[j-1], netos[j]
            j -= 1
    return netos
