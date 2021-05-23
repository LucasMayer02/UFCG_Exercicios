# 2021-03-25, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe quantas palavras vêm alfabeticamente 
# antes e depois da palavra referência 

vezes = int(input())
palavras = []
antes = depois = 0

for _ in range(vezes) :
    palavra = input()
    palavras.append(palavra)

print("---")

referencia = input()

for i in range(len(palavras)) :
    if referencia > palavras[i]:
        antes += 1
    elif referencia < palavras[i]:
        depois += 1

print(f"{antes} antes")
print(f"{depois} depois")
