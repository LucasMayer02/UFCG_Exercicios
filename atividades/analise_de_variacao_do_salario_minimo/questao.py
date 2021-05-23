# 2021-03-25, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe os anos que o salário mínimo ficou 
# abaixo ou acima de 100 e calcula as médias

maior = menor = total_maior = total_menor = 0
ano_inicial = int(input())
ano_final = int(input())

anos = ano_final - ano_inicial + 1 

for _ in range(anos) :
    salario = float(input())
    if salario > 100 :
        maior += 1
        total_maior += salario
    else :
        menor += 1
        total_menor += salario

porc_menor = menor / anos * 100
porc_maior = maior / anos * 100

if menor == 0:
    media_menor = 0
else:
    media_menor = total_menor / menor
if maior == 0 :
    media_maior = 0
else:
    media_maior = total_maior / maior

print(f"{menor} ano(s) abaixo ({porc_menor:.0f}% dos anos)")
if media_menor != 0 :
    print(f"média dos anos abaixo: U$ {media_menor:.2f}")
print(f"{maior} ano(s) acima ({porc_maior:.0f}% dos anos)")
if media_maior != 0 :
    print(f"média dos anos acima: U$ {media_maior:.2f}")
