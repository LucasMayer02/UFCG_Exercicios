# 2021-04-15, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função verifica se os elementos da l2 estão na l1 na mesma ordem

def verifica_esteira(l1, l2) :
    posicao = []
    ordem = True
    for i in range(len(l2)) :
        possui = False
        for j in range(len(l1)) :
            if l2[i] == l1[j] :
                posicao.append(j)
                possui = True
        if not possui :
            return False
    for i in range(1, len(posicao)) :
        if posicao[i-1] > posicao[i] :
            ordem = False
    if ordem :
        return True
    else :
        return False
