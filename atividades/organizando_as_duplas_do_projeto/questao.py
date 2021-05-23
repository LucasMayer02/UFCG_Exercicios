# 2021-04-14, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função veirifca se a dupla de um aluno esta na lista e 
# coloca ao seu lado, caso não esteja, coloca no final da lista

def insere_nome(aluno1, duplas, aluno2) :
    duplas.append(aluno1)
    possui = False
    for i in duplas :
        if i == aluno2 :
            possui = True
            break
    if possui :
            j = len(duplas) - 1
            while True :
                if duplas[j-1] == aluno2 :
                    duplas[j], duplas[j-1] = duplas[j-1], duplas[j]
                    break
                duplas[j], duplas[j-1] = duplas[j-1], duplas[j]
                j -= 1
    return None
