# 2021-03-12, lucas.mayer.almeida@ccc.ufcg.edu.br
# Converte um valor em metros para jardas, pés e polegadas

metros = float(input())

jardas = metros * 1.093613298337708
pes = metros * 3.280839895013123
polegadas = metros * 39.37007874015758

print("Jardas: %.3f yd" % jardas)
print("Pés: %.3f ft" % pes)
print("Polegadas: %.3f in" % polegadas)
