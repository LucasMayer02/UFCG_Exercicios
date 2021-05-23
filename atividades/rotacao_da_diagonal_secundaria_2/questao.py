# 2021-04-26, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função modifica os elementos da diagonal secundária 
# da lista de acordo com a direção indicada

def rotaciona_ds(matriz, direcao) :
    if direcao == "baixo" :
        resquicio = matriz[len(matriz)-1][0]
        posicao = len(matriz) - 1
        for i in range(len(matriz)) :
            matriz[i][posicao], resquicio = resquicio, matriz[i][posicao]
            posicao -= 1
    elif direcao == "cima" :
        resquicio = matriz[0][len(matriz[0]) -1]
        posicao = 0
        for i in range(len(matriz)-1, -1, -1) :
            matriz[i][posicao], resquicio = resquicio, matriz[i][posicao]
            posicao += 1
