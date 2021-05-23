# 2021-03-16, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a velocidade média em km/h de um corredor e o classifica

kilometros = float(input())
horas = float(input())


velocidade = kilometros / horas

if velocidade < 10 :
    corredor = "amador"

elif velocidade <= 15 :
    corredor = "aspirante"

else :
    corredor = "profissional"


print("Velocidade: %.1fkm/h. Corredor %s." % (velocidade, corredor))
