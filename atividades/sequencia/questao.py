# 2021-04-03, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe os numeros da sequência enquanto 
# a soma desses é menor que o limite

limite = int(input())
num = soma = 1

while soma < limite :
    print(num)
    num *= 2
    soma += num
