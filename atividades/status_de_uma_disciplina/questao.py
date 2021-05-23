# 2021-03-14, lucas.mayer.almeida@cc.ufcg.edu.br
# Define a situação de um aluno na disciplina por meio das notas e faltas

nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
faltas = int(input())
aprovado = True

media = (nota1 + nota2 + nota3) / 3

if faltas > 7 :
    aprovado = False

elif media < 7.0 :
    aprovado = False


if aprovado :
    print("aprovado por media")

else:
    if faltas > 7 :
        print("reprovado por faltas")

    elif media > 4.0 :
        print("prova final")

    else:
        print("reprovado por nota")

