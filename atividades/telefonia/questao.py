# 2021-03-24, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o preço por meio da quantidade de minutos

minutos = int(input())

if minutos <= 3 :
    preco = 1 + minutos * 0.5

else:
    preco = 1 + (minutos // 5) * 3 + (minutos % 5) * 0.7


print(f"R$ {preco:.2f}")
