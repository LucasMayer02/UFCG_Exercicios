# 2021-03-22, lucas.mayer.almeida@ccc.ufcg.edu.br
# Define quantas palavras começam com consoante

vezes = int(input())
consoantes = 0

for i in range(vezes) :
    palavra = input()
    if palavra[0] != "a":
        if palavra[0] != "e":
            if palavra[0] != "i":
                if palavra[0] != "o":
                    if palavra[0] != "u":
                        if palavra[0] != "A":
                            if palavra[0] != "E":
                                if palavra[0] != "I":
                                    if palavra[0] != "O":
                                        if palavra[0] != "U":
                                            consoantes += 1
porcentagem = consoantes / vezes * 100

print(f"total de palavras: {vezes}")
print(f"iniciadas por consoantes: {consoantes} ({porcentagem:.2f}%)")
