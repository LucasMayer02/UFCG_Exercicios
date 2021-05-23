# 2021-03-18, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o maior primo multiplicaodor menor que 10

numero = int(input())
maior_primo = 0
novo_numero = numero
fator_2 = False
fator_3 = False
fator_5 = False
fator_7 = False


while novo_numero > 1 :
    if novo_numero % 2 == 0 :
        novo_numero /= 2
        fator_2 = True
    
    elif novo_numero % 3 == 0 :
        novo_numero /= 3
        fator_3 = True
    
    elif novo_numero % 5 == 0 :
        novo_numero /= 5
        fator_5 = True

    elif novo_numero % 7 == 0 :
        novo_numero /= 7
        fator_7 = True

if fator_2 :
    resultado = 0
    multiplicador = 0
    while resultado < numero :
        multiplicador += 1
        resultado = 2 * multiplicador
        if resultado == numero and 2 > maior_primo :
            maior_primo = 2
            final_multiplicador = multiplicador
    
if fator_3 :
    resultado = 0
    multiplicador = 0
    while resultado < numero :
        multiplicador += 1
        resultado = 3 * multiplicador
        if resultado == numero and 3 > maior_primo :
            maior_primo = 3
            final_multiplicador = multiplicador

if fator_5 :
    resultado = 0
    multiplicador = 0
    while resultado < numero : 
        multiplicador += 1
        resultado = 5 * multiplicador
        if resultado == numero and 5 > maior_primo :
            maior_primo = 5
            final_multiplicador = multiplicador
    
if fator_7 :
    resultado = 0
    multiplicador = 0
    while resultado < numero : 
        multiplicador += 1
        resultado = 7 * multiplicador
        if resultado == numero and 7 > maior_primo :
            maior_primo = 7
            final_multiplicador = multiplicador


if maior_primo == 0 :
    print(f"{numero} não tem fatores primos menores que 10")
else:
    print(f"{maior_primo} * {final_multiplicador} = {numero}")

