# 2021-04-03, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o número de questões feita por cada pessoa e o total

pessoas = []
questoes = []

while True :
    nome = input()
    total = 0
    if nome == "**" :
        break
    pessoas.append(nome)
    while True :
        num = input()
        if num == "*" :
            break
        total += int(num)
    questoes.append(total)

total_questoes = 0


print("Relatório de novas questões:\n")

for i in range(len(pessoas)) :
    print(f"{pessoas[i]}: {questoes[i]:d}")
    total_questoes += questoes[i]
print("---")
print(f"Total de novas questões: {total_questoes:d}")
