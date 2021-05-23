# 2021-03-31, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula e exibe as sequências com média maior que o limite 

estabelecido = float(input())
valores = []

while True :
    numeros = []
    total = 0 
    sequencia = input().split()
    if sequencia == ["fim"] :
        break
    for i in range(len(sequencia)) :
        total += float(sequencia[i])
        numeros.append(float(sequencia[i]))
    media = total / len(sequencia)
    if media <= estabelecido / 2:
        break
    if media > estabelecido :
        valores.append(numeros)

for i in range(len(valores)) :
    for j in range(len(valores[i])) :
        if j == len(valores[i]) - 1 :
            print(f"{valores[i][j]:.1f}") 
        else:
            print(f"{valores[i][j]:.1f}", end = " ")
