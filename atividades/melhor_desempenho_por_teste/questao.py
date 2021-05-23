# 2021-03-22, lucas.mayer.almeida@ccc.ufcg.edu.br
# Define qual aluno acertou mais questões

alunos = int(input())
maior_nota = 0
aluno = 1

for i in range(alunos) :
    nota = 0
    resultado = input()

    for i in resultado :
        if i == ".":
            nota += 1

    if nota > maior_nota :
        maior_nota = nota
        melhor_aluno = aluno

    aluno += 1


if maior_nota == 0 :
    print(-1)
else:
    print(melhor_aluno)
