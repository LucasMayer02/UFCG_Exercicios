# 2021-03-23, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe se a soma dos números é dividido por 3 ou 5

num1 = int(input())
num2 = int(input())
num3 = int(input())

soma = num1 + num2 + num3

if soma % 3 == 0 and soma % 5 == 0 :
    print("plifplof")

elif soma % 3 == 0 :
    print("plif")

elif soma % 5 == 0 :
    print("plof")

else:
    print(soma)
