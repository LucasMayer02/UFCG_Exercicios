# 2021-03-12, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe as informações fornecidas e faz a média de preço dos produtos

valor_total = float(input())
data = input()
quantidade_de_produtos = int(input())

media = valor_total / quantidade_de_produtos

print("Data: %s" % data)
print("O valor total da compra foi de R$ %.2f. A média do preço dos produtos é de %.1f." % (valor_total, media))
