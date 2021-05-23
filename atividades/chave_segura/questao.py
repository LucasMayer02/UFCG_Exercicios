# 2021-04-08, lucas.mayer.almeida@ccc.ufcg.edu.br
# Lê uma entrada e verifica se a entrada corresponde 
# aos paramentros para ser uma chave segura

consecutivos = False
vogais = False
vogal = 0
chave = input()

if chave[0] == "a" or chave[0] == "e" or chave[0] == "i" or \
                chave[0] == "o" or chave[0] == "u" :
                    vogal += 1

if chave[1] == "a" or chave[1] == "e" or chave[1] == "i" or \
                chave[1] == "o" or chave[1] == "u" :
                    vogal += 1

for i in range(2, len(chave)) :
    if chave[i] == chave[i -1] and chave[i] == chave[i -2] :
        consecutivos = True
        break
    if chave[i] == "a" or chave[i] == "e" or chave[i] == "i" or \
                chave[i] == "o" or chave[i] == "u" :
                    vogal += 1
    if vogal > 5 :
        vogais = True
        break

if consecutivos :
    print("Chave insegura. 3 caracteres consecutivos iguais.")
elif vogais :
    print("Chave insegura. 6 vogais.")
else :
    print("Chave segura!")
