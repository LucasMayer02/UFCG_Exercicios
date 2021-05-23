# 2021-03-26, lucas.mayer.almeida@ccc.ufcg.edu.br
# Determina qual time ganhou comparando seus critérios de desempate

pontos_a = int(input())
vitorias_a = int(input())
golspro_a = int(input())
golscontra_a = int(input())
pontos_b = int(input())
vitorias_b = int(input())
golspro_b = int(input())
golscontra_b = int(input())
time_a = False
time_b = False

gols_a = golspro_a - golscontra_a
gols_b = golspro_b - golscontra_b

if pontos_a > pontos_b :
    time_a = True
elif pontos_b > pontos_a:
    time_b = True
else:
    if vitorias_a > vitorias_b :
        time_a = True
    elif vitorias_b > vitorias_a :
        time_b = True
    else:
        if gols_a > gols_b :
            time_a = True
        elif gols_b > gols_a :
            time_b = True

if time_a :
    print("O Time A ganhou do Time B.")
elif time_b :
    print("O Time B ganhou do Time A.")
else:
    print("Os dois times terminaram empatados.")
