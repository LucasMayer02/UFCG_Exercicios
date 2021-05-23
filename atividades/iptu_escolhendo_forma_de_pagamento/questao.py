# 2021-03-24, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o preço a ser pago e as parcelas de pagamento

area = float(input())
metro = float(input())
pagamento = input()

if pagamento == "vista" :
    preco = area * metro * 0.8

elif pagamento == "2x" :
    preco = area * metro * 0.9
    parcelas = preco / 2

elif pagamento == "3x" :
    preco = area * metro * 0.95
    parcelas = preco / 3

if pagamento == "vista" :
    print(f"Total: R$ {preco:.2f}")

else:
    print(f"Total: R$ {preco:.2f}. Parcelas: R$ {parcelas:.2f}")
