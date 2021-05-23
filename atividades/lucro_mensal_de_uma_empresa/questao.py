# 2021-03-25, lucas.mayer.almeida@ccc.ufcg.edu.br
#
lista = []

for _ in range(12) :
    ganho, despesa = input().split()
    ganho = float(ganho)
    despesa = float(despesa)

    lucro = ganho - despesa
    lista.append(lucro)

for i in range(12) :
    print(f"{lista[i]:>4.1f}")
