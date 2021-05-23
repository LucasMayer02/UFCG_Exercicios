# 2021-05-05, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função retorna uma função com chaves e valores trocados

def inverte_dicionario(dicionario) :
    resultado = {}
    for k, v in dicionario.items() :
        possui = False
        for i in resultado.keys() :
            if i == v :
                possui = True
        if possui :
            resultado[v].append(k)
        else :
            resultado[v] = [k]
    return resultado
