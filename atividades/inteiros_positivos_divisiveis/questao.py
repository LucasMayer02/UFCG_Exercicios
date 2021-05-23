# 2021-03-25, lucas.mayer.almeida@ccc.ufcg.edu.br
# Mostra os números divisiveis por outros 2 dentro de um intervalo

num1 = int(input())
num2 = int(input())
divisor = int(input())


for n in range(1, divisor+1) :
    if n % num1 == 0 and n % num2 == 0 :
        print(n)
