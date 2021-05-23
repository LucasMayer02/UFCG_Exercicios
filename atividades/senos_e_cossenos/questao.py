# 2022-03-22, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula os senos e cossenos dos ângulos pedidos

import math

angulo = float(input())
delta = float(input())
linhas = int(input())

print("|Angulo|   Seno|Cosseno|")

for i in range(linhas) :
    radiano = math.radians(angulo)
    seno = math.sin(radiano)
    cosseno = math.cos(radiano)

    print(f"| {angulo:5.1f}|{seno:.5f}|{cosseno:.5f}|")
    
    angulo += delta
