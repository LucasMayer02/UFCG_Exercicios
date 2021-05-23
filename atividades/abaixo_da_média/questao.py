# 2021-03-25, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a média e mostra quais notas estão abaixo dela

notas = []
acumulo = 0

while True :
    nota = input()
    if nota == "fim":
        break
    nota = int(nota)
    notas.append(nota)
    acumulo += nota


media = acumulo / len(notas)


print(f"{media:.2f}")

for i in range(len(notas)) :
    if notas[i] < media :
        print(f"{i+1} {notas[i]}")
