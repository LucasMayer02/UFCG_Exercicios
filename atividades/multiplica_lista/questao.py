# 2021-04-08, lucas.mayer.almeida@ccc.ufcg.edu.br
# Multiplica os elementos da lista pela quantidade de vezes pedida

def multiplica_lista(n,lista) :
    resultado = []
    while n > 0 :
        for s in lista:
            resultado.append(s)
        n -= 1
    return resultado
