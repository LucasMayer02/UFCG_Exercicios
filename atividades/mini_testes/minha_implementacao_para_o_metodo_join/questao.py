# 2021-04-12, lucas.mayer.almeida@ccc.ufcg.edu.br
# Implementa um caracter especifico entre cada 
# um dos caracteres originais da string

def meu_join(delimitador, sequencia_de_string) :
    string = ""
    for i in range(len(sequencia_de_string)) :
        if i == len(sequencia_de_string) - 1 :
            string += sequencia_de_string[i]
        else :
            string += sequencia_de_string[i] + delimitador
    return string
