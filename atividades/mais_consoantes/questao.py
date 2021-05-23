# 2021-04-08, lucas.mayer.almeida@ccc.ufcg.edu.br
# Pede entradas até que receba uma palavra com mais consoantes que vogais

contador = 0

while True :
    consoantes = vogais = 0
    palavra = input()
    for s in palavra :
        s = s.lower()
        if s == "a" or s == "e" or s == "i" or s == "o" or s == "u" :
            vogais += 1
        else :
            consoantes += 1
    contador += 1
    if consoantes > vogais :
        break

print(contador)
