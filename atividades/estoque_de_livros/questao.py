# 2021-05-05, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função retorna a quantidade de chaves com valores zerados

def ausentes(estoque) :
    quantidade = 0
    for v in estoque.values() :
        if v == 0 :
            quantidade += 1
    return quantidade
