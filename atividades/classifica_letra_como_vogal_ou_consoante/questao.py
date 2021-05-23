# 2021-03-25, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe quais letras de uma palavra são vogais

palavra = input()

for s in palavra :
    if s == "a" or s == "e" or s == "i" or s == "o" or s == "u" or\
            s == "A" or s == "E" or s == "I" or s == "O" or s == "U" :
                print(f"<{s}> sim")
    else:
        print(f"<{s}> nao")
