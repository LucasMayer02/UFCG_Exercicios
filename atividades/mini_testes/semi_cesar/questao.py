# 2021-04-12, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe uma string com as letras trocadas em equidistancia do alfabeto
# definido por um inteiro

def cesar(msg, d) :
    string = ""
    for i in msg :
        if ord(i) > 96 and ord(i) < 123 :
            if ord(i) + d > 122 :
                string += chr(((ord(i) + d) % 123) + 97)
            elif ord(i) + d < 97 :
                string += chr((ord(i) + d - 97 + 123))
            else :
                string += chr(ord(i) + d)
        else :
            string += i
    return string
