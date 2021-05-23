# 2021-03-29, lucas.mayer.almeida@ccc.ufcg.edu.br
# Define se uma sequência esta dentro de um determinado padrão

sequencia = input().split()
erro = False

for i in range(1, len(sequencia)) :
    if int(sequencia[i]) % 2 == 1 and int(sequencia[i - 1]) % 2 == 0 :
        erro = True

if erro :
    print("erro")
else:
    print("ok")
