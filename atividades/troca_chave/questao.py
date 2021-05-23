# 2021-05-05, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função retorna um dicionário que as chaves e valores se invertem

def troca_chave(dic) :
    resultado = {}
    for k, v in dic.items() :
        resultado[v] = k
    return resultado
