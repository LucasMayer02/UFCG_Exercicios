# 2021-04-14, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função remove os elementos da lista menores que a qtd_itens

def filtra_caixas_indisponiveis(lista_caixas, qtd_itens) :
    provisorio = lista_caixas.copy()
    resquicio = 0
    for i in range(len(provisorio)) :
        if provisorio[i] < qtd_itens :
             lista_caixas.pop(i - resquicio)
             resquicio += 1
    return None 
