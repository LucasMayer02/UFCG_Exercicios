# 2021-03-26, lucas.mayer.almeida@ccc.ufcg.edu.br
# Soma até ultrapassar 999, calcula a media 
# e quantos números são maiores que a média

soma = quant = 0
numeros = []

while soma < 999 :
    num = int(input())
    quant += 1
    soma += num
    numeros.append(num)

media = soma / quant
acima_media = 0

for i in range(len(numeros)) :
    if numeros[i] > media :
        acima_media += 1

print(soma)
print(f"{media:.2f}")
print(acima_media)
