# 2021-03-24, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a quantidade de água congelada no produto

congelado = float(input())
descongelado = float(input())

porcentagem = 100 - (descongelado / congelado) * 100 

print(f"{porcentagem:.1f}% do peso do produto é de água congelada.")

if porcentagem < 5:
    print("Produto qualis A.")

elif porcentagem < 10 :
    print("Produto em conformidade.")

else:
    print("Produto não conforme.")
