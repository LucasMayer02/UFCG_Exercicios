# 2021-04-15, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função retorna os elementos que possuem 'google.com'

def filtra_urls(l) :
    resultado = []
    for i in range(len(l)) :
        for j in range(len(l[i])) :
            if l[i][j] == "g" :
                if l[i][j+1] == "o" :
                    if l[i][j+2] == "o" :
                        if l[i][j+3] == "g" :
                            if l[i][j+4] == "l" :
                                if l[i][j+5] == "e" :
                                    if l[i][j+6] == "." :
                                        if l[i][j+7] == "c" :
                                            if l[i][j+8] == "o" :
                                                if l[i][j+9] == "m" :
                                                    resultado.append(l[i])
                                                    break
    return resultado
