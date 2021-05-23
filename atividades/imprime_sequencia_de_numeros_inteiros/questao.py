# 2021-04-05, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe as sequẽncias que a maioria dos seus 
# números é maior que um limite definido

posicao = []
string = []
ordem = 0
limite = int(input())

while True :
    maiores = 0
    sequencia = input()
    if sequencia == "fim" :
        break
    lista = sequencia.split()
    ordem += 1
    for i in lista :
        if int(i) > limite :
            maiores += 1
    if maiores > len(lista) / 2 :
        posicao.append(ordem)
        string.append(sequencia)

for i in range(len(posicao)) :
    print(f"sequencia {posicao[i]}: {string[i]}")
