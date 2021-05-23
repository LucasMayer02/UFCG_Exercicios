# 2021-04-26, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função cria uma matriz com os menores elementos 
# de duas matrizes diferentes na mesma posição

def matriz_menor(matriz_1, matriz_2) :
    menores = []
    for i in range(len(matriz_1)) :
        menores.append([])
    for i in range(len(matriz_1)) :
        for j in range(len(matriz_1[i])) :
            if matriz_1[i][j] < matriz_2[i][j] :
                menores[i].append(matriz_1[i][j])
            else :
                menores[i].append(matriz_2[i][j])
    return menores
