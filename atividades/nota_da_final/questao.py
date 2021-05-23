# 2021-03-16, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a nota mínima necessária na final para ser aprovado

media_parcial = float(input())


nota_minima = (5.0 - media_parcial * 0.6) / 0.4


print("%.1f" % nota_minima)
