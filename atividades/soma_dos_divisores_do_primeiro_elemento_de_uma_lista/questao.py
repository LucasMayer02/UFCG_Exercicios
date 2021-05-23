# 2021-03-26, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe a soma de determinados divisores de um número referência

acumulo = 0
referencia = int(input())

for _ in range(10) :
    num = int(input())
    if referencia % num == 0 :
        acumulo += num

print(acumulo)
