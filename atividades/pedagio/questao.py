# 2021-03-15, lucas.mayer.almeida@ccc.ufcg.edu.br
# Determina a taxa de pedágio por meio do 
# tipo de veiculo e quantidade de eixos

veiculo = input()

if veiculo == "Ônibus" or veiculo == "Caminhão" :
    eixos = int(input())


if veiculo == "Automóvel utilitário" :
    print("Valor a pagar: R$ 11.40.")

elif veiculo == "Ônibus" :
    print("Valor a pagar: R$ %.2f." % (eixos * 11.40))

elif veiculo == "Caminhão" :
    print("Valor a pagar: R$ %.2f." % (eixos * 9.60))

elif veiculo == "Motocicleta" :
    print("Valor a pagar: R$ 5.70.")

else:
    print("Veículo não cadastrado.")
