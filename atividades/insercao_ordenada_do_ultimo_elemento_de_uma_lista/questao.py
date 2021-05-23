# 2021-04-19, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função troca a posição de determinado elemento 
# caso o elemento a sua esquerda seeja maior que ele

def insere_ordenado_ultimo(lista) :
        i = len(lista) - 1
        while i > 0 :
            if lista[i] < lista[i-1] :
                lista[i], lista[i-1] = lista[i-1], lista[i]
            else :
                break
            i -= 1
