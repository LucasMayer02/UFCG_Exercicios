# 2021-04-22, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função organiza os elementos entre numeros 
# inteiros, letras e alphanumericos trocando suas posiçõoes

def ordena_tipos(elementos) :
    for i in range(len(elementos)) :
        j = i
        while j > 0 :
            possui = False
            if elementos[j].isdigit() :
                if not elementos[j-1].isdigit():
                    elementos[j], elementos[j-1] = elementos[j-1], elementos[j]
                    possui = True
            elif elementos[j].isalpha():
                if elementos[j-1].isdigit() == False and elementos[j-1].isalpha() == False:
                    elementos[j], elementos[j-1] = elementos[j-1], elementos[j]
                    possui = True
            if not possui :
                break
            j -= 1
    return elementos
