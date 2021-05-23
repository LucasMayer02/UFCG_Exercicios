# 2021-03-25, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe a quantidade de números divisíveis 
# pelo mesmo divisor dentro de um conjunto

divisor = int(input())
sequencia = int(input())
total = 0

for _ in range(sequencia) :
    num = int(input())
    if num % divisor == 0 :
        total += 1

porcentagem = total / sequencia * 100

print(f"{total} ({porcentagem:.1f}%)")
