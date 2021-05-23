# 2021-04-03, lucas.mayer.almeida@ccc.ufcg.edu.br
# Soma um valor até que esse seja menor que a média

total = divisor = media = valor = 0

while True :
    num = float(input())
    if num < media :
        break
    total += num
    divisor += 1
    media = total / divisor
    valor += num

print(f"Saldo total do FIS: R${valor:.2f}.")
print(f"Média das contribuições: R${media:.2f}.")
