# 2021-03-15, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o imc e mostra quando precisa pra alcançar o imc ideal

peso = float(input())
altura = float(input())


imc = peso / (altura ** 2)
novo_peso = 24.9 * (altura **2)
ganha_perda = novo_peso - peso


print("IMC atual = %.2f" % imc)
print("Peso a ser ganho/perdido = %.2f" % ganha_perda)
