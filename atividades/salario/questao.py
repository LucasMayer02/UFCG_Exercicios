# 2021-03-15, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o rendimento por hora trabalhada 
# com os descontos e sem os descontos 

salario_bruto = float(input())
horas_trabalhadas = int(input())


hora_bruta = salario_bruto / horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato
hora_liquida = salario_liquido / horas_trabalhadas


print("Salário Bruto = %.2f" % salario_bruto)
print("Hora Bruta = %.2f" % hora_bruta)
print("Desconto IR = %.2f" % ir)
print("Desconto INSS = %.2f" % inss)
print("Desconto Sindicato = %.2f" % sindicato)
print("Salário Líquido = %.2f" % salario_liquido)
print("Hora Líquida = %.2f" % hora_liquida)
