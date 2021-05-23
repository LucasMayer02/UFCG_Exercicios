# 2021-03-12, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula quantos reais são necessários para uma determinada quantia
# e cotação em dolar

reais = float(input("Reais? "))
cotacao = float(input("Cotação? "))

conversao = reais * cotacao

print("Conversão: $ %.2f"% conversao)
