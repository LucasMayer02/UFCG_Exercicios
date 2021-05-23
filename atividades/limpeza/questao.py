# 2021-03-23, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o preço por meio do tipo de limpeza e tamanho da caixa

limpeza = int(input())

if limpeza != 3 :
    metros = float(input())

brinde = False


if limpeza == 1 :
    preco = metros * 80

elif limpeza == 2 :
    preco = metros * 50

else:
    preco = 50


if preco >= 200 :
    brinde = True


print(f"R$ {preco:.0f},00")

if brinde :
    print("Brinde!")
