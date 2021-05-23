# 2021-04-06, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe o número de alunos que superou o limite de faltas

alunos = 0

while True :
    sequencia = input()
    if sequencia == "-" :
        break
    i = 0
    faltas = 0
    while i < len(sequencia) :
        if sequencia[i] == "f" :
            faltas += 1
        i += 1
    if faltas > 8 :
        alunos += 1

print(f"{alunos} aluno(s) reprovado(s) por falta.")
