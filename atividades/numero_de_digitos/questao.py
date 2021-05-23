# 2021-03-31, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula quantos digitos tem um número

num = int(input())
digitos = 0
divisor = 1

while True :
    if num / divisor >= 1 :
        digitos += 1
    else :
        break
    divisor *= 10

if num == 0 :
    print("1")
else:
    print(digitos)
