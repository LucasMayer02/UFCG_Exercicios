# 2021-03-25, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o resto da divisão por 11 da soma dos dígitos de um número

soma = 0
digito = input()

for n in digito :
    soma += int(n)

verificador = soma % 11

if verificador == 10:
    print(f"{digito}-X")
else:
    print(f"{digito}-{verificador:.0f}")
