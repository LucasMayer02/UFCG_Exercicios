# 2021-03-16, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula as médias e declara qual aluno foi aprovado

escrita1 = float(input())
didatica1 = float(input())
titulacao1 = float(input())
idade1 = int(input())
escrita2 = float(input())
didatica2 = float(input())
titulacao2 = float(input())
idade2 = int(input())


media1 = escrita1 * 0.3 + didatica1 * 0.4 + titulacao1 * 0.3
media2 = escrita2 * 0.3 + didatica2 * 0.4 + titulacao2 * 0.3


if media1 > media2 :
    print("O primeiro candidato foi aprovado com média %.1f." % media1)
elif media2 > media1 :
    print("O segundo candidato foi aprovado com média %.1f." % media2)
else:
    if idade1 > idade2 :
        print("O primeiro candidato foi aprovado com média %.1f." % media1)
    elif idade2 > idade1 :
        print("O segundo candidato foi aprovado com média %.1f." % media2)
    else:
        print("Empate.")
