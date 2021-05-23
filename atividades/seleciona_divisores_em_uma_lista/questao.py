# 2021-04-14, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função retira da lista os números que 
# não são divisiveis pela soma de seus algarismos

def filtra_divisores(lista) :
    provisorio = lista.copy()
    resquicio = 0
    for i in range(len(provisorio)) :
        soma = 0
        for j in str(provisorio[i]) :
            soma += int(j)
        if provisorio[i] % soma != 0 :
            lista.pop(i - resquicio)
            resquicio += 1
    return None
