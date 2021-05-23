# 2021-03-22, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula os quadrados dos números entre dois valores

numero1 = int(input())
numero2 = int(input())

if numero1 > numero2 :
    print("---")
else:
    for i in range(numero1, numero2 + 1) :
        quadrado = i ** 2
        print(f"{i} {quadrado}")
