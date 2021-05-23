# 2021-03-26, lucas.mayer.almeida@ccc.ufcg.edu.br
# Define se o número tem uma sequẽncia alternada de impares e pares

numero = input()
verdadeiro = True

for i in range(1, len(numero)) :
    if int(numero[i]) % 2 == 0 and int(numero[i-1]) % 2 == 0:
        verdadeiro = False
    elif int(numero[i]) % 2 == 1 and int(numero[i-1]) % 2 == 1:
        verdadeiro = False

if verdadeiro:
    print(f"verdadeiro: {len(numero)} algarismos.")
else:
    print(f"falso: {len(numero)} algarismos.")
