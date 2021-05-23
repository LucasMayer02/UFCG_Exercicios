# 2021-04-01, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe os digitos de um número 

num = int(input())
divisor = 10
casa = 1

while True :
    digito = int((num % divisor) / casa)
    print(f"{digito:d}")
    if num % divisor == num :
        break
    divisor *= 10
    casa *= 10
