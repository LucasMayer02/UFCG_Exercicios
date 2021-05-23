# 2021-03-31, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe os números menores que a média e sua posição na sequência

numeros = []
acumulo = 0

while True :
    num = input()
    if num == "fim" :
        break
    num = int(num)
    acumulo += num
    numeros.append(num)

media = acumulo / len(numeros)

print(f"{media:.2f}")

for i in range(len(numeros)) :
    if numeros[i] < media :
        print(f"{i + 1} {numeros[i]}")
