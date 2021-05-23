# 2021-04-29, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função cria uma nova lista que troca as posições dos elementos 
# de forma a criar uma sensação de rotação em 90 graus

def rotaciona90(imagem) :
    rotacionada = []
    for i in range(len(imagem[0])) :
        rotacionada.append([])
    for i in range(len(imagem)-1, -1, -1) :
        for j in range(len(imagem[i])) :
            rotacionada[j].append(imagem[i][j])
    return rotacionada
