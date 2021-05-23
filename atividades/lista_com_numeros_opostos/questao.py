# 2021-04-13, lucas.mayer.almeida@ccc.ufcg.edu.br
# Ao invocar a função, retorna a lista apenas os numeros 
# que os seus opostos tambem estão presente na lista

def lista_so_com_oposto(lista) :
    resquicio = 0
    temporario = lista.copy()
    for i in  range(len(temporario)) :
        possui = False
        for j in range(len(temporario)) :
            if temporario[i] * -1 == temporario[j] :
                possui = True
        if not possui :
            lista.pop(i - resquicio)
            resquicio += 1
    return None
