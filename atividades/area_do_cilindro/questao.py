# 2021-03-16, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a área de um cilindro por meio do seu diâmetro e altura

import math

print("Cálculo da Superfície de um Cilindro")
print("---")

diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))

pi = math.pi
raio = diametro / 2
area_base = 2 * ( pi * raio ** 2)
perimetro = 2 * pi * raio
area_lateral = altura * perimetro
area_total = area_base + area_lateral

print("---")
print("Área calculada: %.2f" % area_total)
