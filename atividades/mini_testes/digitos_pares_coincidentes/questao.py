# 2021-03-26, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe os pares que coincidem de posição nos dois números

num1 = input()
num2 = input()
soma = 0

print("Dígitos coincidentes")

for i in range(len(num1)) :
    if num1[i] == num2[i] and int(num1[i]) % 2 == 0 :
        print(f"{num1[i]} na posição {i + 1}")
        soma += int(num1[i])

print(f"Soma de dígitos coincidentes: {soma}")
