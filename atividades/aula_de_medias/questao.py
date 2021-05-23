# 2021-04-08, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula uma quantidade até que o total do somatório 
# seja maior ou igual a 100 e mostra suas estatisticas

numeros = []
total = 0

while True :
    valor = float(input())
    numeros.append(valor)
    total += valor
    if total >= 100 :
        break

media = total / len(numeros)

print(f"Quantidade de números lidos: {len(numeros)}")
print(f"Soma dos números lidos: {total:.2f}")
print(f"Média = {media:.2f}")
print("\nAbaixo da média")

for i in range(len(numeros)) :
    if numeros[i] < media :
        print(f"{numeros[i]:.2f} ({i+1}o)")

print("\nAcima da média")

for i in range(len(numeros)) :
    if numeros[i] > media :
        print(f"{numeros[i]:.2f} ({i+1}o)")
