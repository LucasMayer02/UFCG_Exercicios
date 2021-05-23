# 2021-03-13, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o valor do inss a ser pago pelo empregador e o empregado

salario = float(input())

empregador = salario * 0.12

if salario < 1317.08 :
    empregado = salario * 0.08
elif salario < 2195.12 :
    empregado = salario * 0.09
else:
    empregado = salario * 0.11

print("O valor da contribuição do INSS a ser pago pelo empregador é\
 de R$ %.2f" % empregador)
print("O valor da contribuição do INSS a ser pago pelo empregado é\
 de R$ %.2f" % empregado)

