# 2021-03-12, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a porcentagem de aumento do segundo valor em relação ao primeiro 

valor_atual = float(input("Valor atual? "))
valor_novo = float(input("Novo valor? "))

reajuste =( (valor_novo / valor_atual) - 1) * 100
porcento = "%"

print("Reajuste de %.1f%s" % (reajuste, porcento))
