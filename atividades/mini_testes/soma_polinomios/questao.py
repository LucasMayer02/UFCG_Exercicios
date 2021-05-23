# 2021-04-22, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função realiza soma de polinomios

def soma_polinomios(p1, p2) :
    maior = []
    menor = []
    resultado = []
    if len(p1) > len(p2) :
        for i in p1 :
            maior.append(i)
        for i in p2 :
            menor.append(i)
    else :
        for i in p2 :
            maior.append(i)
        for i in p1 :
            menor.append(i)
    if len(maior) != len(menor) :
        for i in range(len(maior) - len(menor)) :
            resultado.append(maior[i])
    for i in range(len(menor)) :
        soma = menor[i] + maior[i + len(maior) - len(menor)]
        resultado.append(soma)
    return resultado


