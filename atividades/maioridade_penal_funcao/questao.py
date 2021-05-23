# 2021-04-11, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe quais pessoas atingiram a maioridade penal

def maioridade_penal(nomes, idades) :
    resultado = []
    string = ""
    nomes = nomes.split()
    idades = idades.split()
    for i in range(len(idades)) :
        if int(idades[i]) >= 18 :
            resultado.append(nomes[i])
    for i in range(len(resultado)) :
        if i == len(resultado) - 1 :
            string += resultado[i]
        else :
            string += resultado[i] + " "
    return string
