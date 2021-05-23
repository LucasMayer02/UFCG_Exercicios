# 2021-04-29, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função exibe as somas dos números que estão na linha 
# ou coluna definida, exceto aquele que entra nos dois casos

def soma_linha_e_coluna(matriz,l,c) :
    soma = 0
    for i in range(len(matriz)) :
        for j in range(len(matriz[i])) :
            if (j == l and i != c) or (j != l and i == c) :
                soma += matriz[i][j]
    return soma
