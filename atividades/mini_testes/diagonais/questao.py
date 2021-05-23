# 2021-03-18, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula as diagonais por meio do numero de lados

lados = int(input())

diagonais = lados / 2 * (lados - 3)

print(f"{lados} lados => {diagonais:.0f} diagonais")
