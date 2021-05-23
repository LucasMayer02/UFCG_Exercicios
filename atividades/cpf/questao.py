# 2021-03-12, lucas.mayer.almeida@ccc.ufcg.edu.br
# Completa um cpf ao juntar suas partes e calcular o resultado da última parte

parte1 = input()
parte2 = input()
parte3 = input()

parte4 = str(int(parte3[0]) + int(parte3[1]) + int(parte3[2]))

if len(parte4) < 2 :
    parte4 = "0" + parte4

cpf = parte1 + "." + parte2 + "." + parte3 + "-" + parte4

print(cpf)
