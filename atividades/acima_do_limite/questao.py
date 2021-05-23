# 2021-03-29, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe as somas maiores que o número limite 

lista_sequencias = []
lista_somas = []
limite = int(input())

while True :
    sequencia = input().split()
    soma = 0
    string = ""
    if sequencia == ["-"] :
        break
    for i in range(len(sequencia)) :
        soma += int(sequencia[i])
        if i == len(sequencia) - 1 :
            string += sequencia[i]
        else:
            string += sequencia[i] + " + "
    if soma >= limite :
        lista_sequencias.append(string)
        lista_somas.append(soma)
    if soma > limite * 5 :
        break

for i in range(len(lista_sequencias)) :
    print(f"{lista_sequencias[i]} = {lista_somas[i]}")    
