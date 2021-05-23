# 2021-03-31, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula quantas sequencias são pa's com predeterminada razão

razao = int(input())
total = 0

while True :
    sequencia = input().split()
    if sequencia == ["fim"] :
        break
    pa = True
    for i in range(1, len(sequencia)) :
        if int(sequencia[i]) - razao != int(sequencia[i-1]) :
            pa = False
    if pa :
        total += 1

print(total)
