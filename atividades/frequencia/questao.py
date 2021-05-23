# 2021-04-15, lucas.mayer.almeida@ccc.ufcg.edu.br
#

def get_frequencia(lista) :
    numeros = []
    vezes = []
    for i in range(len(lista)) :
        for j in range(len(numeros)) :
            if lista[i] == numeros[j] :
                possui = True
                vezes[i] += 1

