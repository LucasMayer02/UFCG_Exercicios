# 2021-03-12, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a média das notas de um aluno e a quantidade de minitestes para determinar sua situação na disciplina

minitestes = int(input())

notas = 0

for i in range(minitestes):
    valor = float(input())
    notas += valor

media = notas / minitestes

if minitestes == 1 :
    print(media)
    print("Aluno ainda não aprovado na unidade")
elif minitestes < 3 :
    print(media)
    if media < 6.0 :
        print("Aluno ainda não aprovado na unidade")
    else:
        print("Aluno aprovado na unidade")
else:
    print(media - 0.5)
    if media < 6.0 :
        print("Aluno ainda não aprovado na unidade")
    else:
        print("Aluno aprovado na unidade")
