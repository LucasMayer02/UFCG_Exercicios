# 2021-03-16, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula todos os dados necessários para formar a questão

pos_inicial = float(input("Posição inicial? "))
veloc_inicial = float(input("Velocidade inicial? "))
tempo = float(input("Tempo? "))
aceleracao = float(input("Aceleração? "))


veloc_media = veloc_inicial + aceleracao * tempo / 2
veloc_final = veloc_media * 2 - veloc_inicial
pos_final = pos_inicial + veloc_inicial * tempo + aceleracao * tempo ** 2  / 2


print()
print("Dados da questão")
print("================")
print("   Posição inicial: %.2f m" % pos_inicial)
print("Velocidade inicial: %.2f m/s" % veloc_inicial)
print("        Aceleração: %.2f m/s2" % aceleracao)
print("             Tempo: %.2f s" % tempo)
print("  Velocidade final: %.2f m/s" % veloc_final)
print("  Velocidade média: %.2f m/s" % veloc_media)
print("     Posição final: %.2f m" % pos_final)
