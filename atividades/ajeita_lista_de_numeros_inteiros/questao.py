# 2021-04-15, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função ordenas primeiramente os pares decrescendo 
# e depois os impares crescendo

def ajeita_lista(lista) :
    for i in range(len(lista)) :
        j = i
        while j > 0:
            possui = False
            if lista[j] % 2 == 0 :
                if lista[j-1] % 2 == 0 :
                    if lista[j] > lista[j-1] :
                        lista[j], lista[j-1] = lista[j-1], lista[j]
                        possui = True
                else :
                    lista[j], lista[j-1] = lista[j-1], lista[j]
                    possui = True
            else :
                if lista[j-1] % 2 == 1 :
                    if lista[j] < lista[j-1] :
                        lista[j], lista[j-1] = lista[j-1], lista[j]
                        possui = True
            if not possui :
                break
            j -= 1
    return None
