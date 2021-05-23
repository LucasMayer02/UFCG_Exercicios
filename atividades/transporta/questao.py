# 2021-04-26, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função exibe a matriz transposta da matriz original sem alterala

def transposta(M) :
    resposta = []
    for i in range(len(M[0])) :
        resposta.append([])
    for i in range(len(M)) :
        for j in range(len(M[i])) :
            resposta[j].append(M[i][j])
    return resposta
