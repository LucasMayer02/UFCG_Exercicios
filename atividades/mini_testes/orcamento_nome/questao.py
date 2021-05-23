# 2021-03-18, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o preço baseado na quantidade de letras

nome = input("Nome? ")
valor_letra = float(input("Valor da letra (R$)? "))

preco_final = len(nome) * valor_letra

print(f"Preço final: R$ {preco_final:.2f}")
