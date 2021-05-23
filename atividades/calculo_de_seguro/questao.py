# 2021-04-08, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a pontuação feita baseada nos elementos da lista e 
# calcula o seguro como sendo uma porcentagem do valor do veículo

def calcula_seguro(valor, lista):
    resultado = []
    pontos = 0
    if lista[0] <= 21 :
        pontos += 20
    elif lista[0] <= 30 :
        pontos += 15
    elif lista[0] <= 40 :
        pontos += 12
    elif lista[0] <= 60 :
        pontos += 10
    else :
        pontos += 20
    if lista[1] :
        pontos += 10
    else :
        pontos += 20
    if lista[2] :
        pontos += 20
    else :
        pontos += 10
    if lista[3] :
        pontos += 20
    else :
        pontos += 10
    if lista[4] :
        pontos += 20
    else :
        pontos += 10
    if lista[5] :
        pontos += 10
    else :
        pontos += 20
    if lista[6] == "Trabalho" :
        pontos += 10
    else :
        pontos += 20
    resultado.append(pontos)
    if pontos <= 80 :
        resultado.append("Risco Baixo")
        seguro = valor * 0.1
    elif pontos <= 100 :
        resultado.append("Risco Medio")
        seguro = valor * 0.2
    else :
        resultado.append("Risco Alto")
        seguro = valor * 0.3
    resultado.append(seguro)
    return resultado
