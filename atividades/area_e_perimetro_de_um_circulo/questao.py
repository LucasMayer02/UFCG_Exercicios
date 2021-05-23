# 2021-03-12, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a área e o perímetro de um círculo por meio do diâmetro 

import math

diametro = int(input())

pi = math.pi
raio = diametro / 2

perimetro = 2 * pi * raio
area = pi * raio**2

print("A: %.5f"% area)
print("P: %.5f"% perimetro)

