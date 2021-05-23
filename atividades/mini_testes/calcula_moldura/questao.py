# 2021-03-18, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o preco por meio da largura e comprimento

comprimento = float(input())
largura = float(input())

metro = comprimento * 2 / 100 + largura * 2 / 100
preco = metro * 120

print(f"R$ {preco:.1f}")
