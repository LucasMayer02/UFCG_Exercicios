# 2021-03-24, lucas.mayer.almeida@ccc.ufcg.edu.br
# Mostra o segundo menor e segundo maior numéros do conjunto

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())


if num1 >= num2 and num1 <= num3 and num1 <= num4 :
    segundo_menor = num1
elif num1 >= num3 and num1 <= num2 and num1 <= num4 :
    segundo_menor = num1
elif num1 >= num4 and num1 <= num2 and num1 <= num3 :
    segundo_menor = num1

if num2 >= num1 and num2 <= num3 and num2 <= num4 :
    segundo_menor = num2
elif num2 >= num3 and num2 <= num1 and num2 <= num4 :
    segundo_menor = num2
elif num2 >= num4 and num2 <= num1 and num2 <= num3 :
    segundo_menor = num2

if num3 >= num1 and num3 <= num2 and num3 <= num4 :
    segundo_menor = num3
elif num3 >= num2 and num3 <= num1 and num3 <= num4 :
    segundo_menor = num3
elif num3 >= num4 and num3 <= num1 and num3 <= num2 :
    segundo_menor = num3

if num4 >= num1 and num4 <= num2 and num4 <= num3 :
    segundo_menor = num4
elif num4 >= num2 and num4 <= num1 and num4 <= num3 :
    segundo_menor = num4
elif num4 >= num3 and num4 <= num1 and num4 <= num2 :
    segundo_menor = num4


if num1 <= num2 and num1 >= num3 and num1 >= num4 :
    segundo_maior = num1
elif num1 <= num3 and num1 >= num2 and num1 >= num4 :
    segundo_maior = num1
elif num1 <= num4 and num1 >= num2 and num1 >= num3 :
    segundo_maior = num1

if num2 <= num1 and num2 >= num3 and num2 >= num4 :
    segundo_maior = num2
elif num2 <= num3 and num2 <= num1 and num2 >= num4 :
    segundo_maior = num2
elif num2 <= num4 and num2 >= num1 and num2 >= num3 :
    segundo_maior = num2

if num3 <= num1 and num3 >= num2 and num3 >= num4 :
    segundo_maior = num3
elif num3 <= num2 and num3 >= num1 and num3 >= num4 :
    segundo_maior = num3
elif num3 <= num4 and num3 >= num1 and num3 >= num2 :
    segundo_maior = num3

if num4 <= num1 and num4 >= num2 and num4 >= num3 :
    segundo_maior = num4
elif num4 <= num2 and num4 >= num1 and num4 >= num3 :
    segundo_maior = num4
elif num4 <= num3 and num4 >= num1 and num4 >= num2 :
    segundo_maior = num4


print(f"Considerando os números {num1}, {num2}, {num3} e {num4}")
print(f"O segundo menor número é {segundo_menor}")
print(f"O segundo maior número é {segundo_maior}")
