# 2021-04-15, lucas.mayer.almeida@ccc.ufcg.edu.br
# Elimina da lista elementos que se repetem 3 vezes

def triplets(lista) :
    numeros = []
    repetidos = []
    for i in range(len(lista)) :
        possui = False
        for j in range(len(numeros)) :
            if lista[i] == numeros[j] :
                possui = True
                repetidos[j] += 1
        if not possui :
            numeros.append(lista[i])
            repetidos.append(1)
    desgasto = 0
    provisorio = []
    for n in lista :
        provisorio.append(n)
    for i in range(len(repetidos)) :
        if repetidos[i] == 3 :
            for l in range(len(provisorio)) :
                if provisorio[l] == numeros[i] :
                    lista.pop(l - desgasto)
                    desgasto += 1
    return None
