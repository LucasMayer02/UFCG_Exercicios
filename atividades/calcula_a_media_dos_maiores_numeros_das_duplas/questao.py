# 2021-03-25, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a média entre os maiores números das duplas

duplas = []
acumulo = 0
vezes = int(input())

for _ in range(vezes) :
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    if num1 > num2 :
        duplas.append(num1)
        acumulo += num1
    elif num2 > num1 :
        duplas.append(num2)
        acumulo += num2

if len(duplas) == 0 :
    print("Não é possível calcular a média.")
else:
    media = acumulo / len(duplas)
    print(f"{media:.2f}")
