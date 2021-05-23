# 2021-03-17. lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o salário líquido e bruto 
# por meio das horas extras e valor do salãrio mĩnimo

nome = input()
horas_extras = float(input())
salario_minimo = float(input())
valor_hora = float(input())

salario_hora_extra = horas_extras * valor_hora
salario_bruto = 4 * salario_minimo + salario_hora_extra
inss = salario_bruto * 0.12
imposto_de_renda = salario_bruto * 0.2
descontos = inss + imposto_de_renda
salario_liquido = salario_bruto - descontos

print(f"O Salário Bruto de {nome} é de R$ {salario_bruto:.2f}")
print(f"O Salário Líquido de {nome} é de R$ {salario_liquido:.2f}")
