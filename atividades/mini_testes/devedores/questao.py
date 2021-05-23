# 2021-05-06, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função retorna quantos valores são negativos

def devedores(contas) :
    quantidade = 0
    for v in contas.values() :
        if v < 0 :
            quantidade += 1
    return quantidade
