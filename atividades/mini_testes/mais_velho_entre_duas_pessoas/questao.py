# 2021-03-26, lucas.mayer.almeida@ccc.ufcg.edu.br
# Define quais das duas pessoas é mais velha

pessoa_1 = input()
dia_1 = int(input())
mes_1 = int(input())
ano_1 = int(input())
pessoa_2 = input()
dia_2 = int(input())
mes_2 = int(input())
ano_2 = int(input())
p1 = False
p2 = False

if ano_1 < ano_2 :
    p1 = True
elif ano_2 < ano_1 :
    p2 = True
else:
    if mes_1 < mes_2 :
        p1 = True
    elif mes_2 < mes_1 :
        p2 = True
    else:
        if dia_1 < dia_2 :
            p1 = True
        elif dia_2 < dia_1 :
            p2 = True

if p1 :
    print(pessoa_1)
elif p2 :
    print(pessoa_2)
else:
    print("nenhuma")
