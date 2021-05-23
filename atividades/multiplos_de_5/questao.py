# 2021-04-05, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe os múltiplos de 5 menores que um número limite

lim = int(input())
mult = 0
while mult < lim :
    mult += 5
    if mult % 2 == 0 and mult < lim :
        print(mult)
