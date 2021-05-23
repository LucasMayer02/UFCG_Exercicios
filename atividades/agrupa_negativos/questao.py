# 2021-05-05, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função cria um dicionário que separa 
# os números negativos e não negativos

def agrupa_negativos(lista) :
    resultado = {"nao-negativos":[], "negativos":[]}
    for n in lista :
        if n < 0 :
            resultado["negativos"].append(n)
        else :
            resultado["nao-negativos"].append(n)
    return resultado

