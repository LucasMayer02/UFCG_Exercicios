# 2021-03-12, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o preço total a ser pago por meio da quantidade de crianças, adultos e preço do ingresso

adultos = int(input())
criancas = int(input())
ingresso = float(input())

preco = (adultos * ingresso) + (criancas * ingresso/2)

print("Total: R$ %.2f"% preco)
