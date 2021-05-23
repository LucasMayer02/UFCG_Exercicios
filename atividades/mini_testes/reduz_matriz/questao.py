# 2021-04-29, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função reduz as extremidades da matriz

def reduz_matriz(m) :
    copia = []
    retirado = 0
    for i in m :
        copia.append(i)
    if len(m[0]) == 4 :
        for i in range(len(copia)) :
            m[i].pop(0)
            retirado += 1
    elif len(m[0]) > 4 :
        for i in range(len(copia)) :
            m[i].pop(len(m[i])-1)
            m[i].pop(0)
            retirado += 2
    if len(m) == 4 :
        retirado += len(m[0])
        m.pop(0)
    elif len(m) > 4 :
        retirado += (len(m[0]) * 2)
        m.pop(len(m)-1)
        m.pop(0)
    return retirado
