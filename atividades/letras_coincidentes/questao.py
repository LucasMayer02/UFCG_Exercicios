# 2021-03-14, lucas.mayer.almeida@ccc.ufcg.edu.br
# Identifica em duas palavras quais e quantas letras coincidem em posição

palavra1 = input()
palavra2 = input()
letras = []
posicao = []
total = 0


menor = min(len(palavra1), len(palavra2))

for i in range(menor) :
    if palavra1[i] == palavra2[i]:
        letras.append(palavra1[i])
        posicao.append(i + 1)
        total += 1

soma = len(palavra1) + len(palavra2)

if total != 0 :
    porcentagem = 100 / (soma / total)
else:
    porcentagem = 0

porc = "%"


print("Letras coincidentes")

for i in range(len(letras)):
    print("\'%s\' na posição %d" % (letras[i], posicao[i]))

print("Total de letras coincidentes: %d (%d%s)" % (total, porcentagem, porc))
