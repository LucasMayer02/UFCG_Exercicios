# 2021-03-31, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a média e adiciona notas até que a média
# das duas maiores notas seja o suficiente para aprovar

print("Mastery Learning")
print("Cálculo da nota na unidade")

nota1 = float(input("\nNota? "))
nota2 = float(input("Nota? "))
aprovado = False
penalizacao = -0.5

if nota1 > nota2 :
    primeira_nota = nota1
    segunda_nota = nota2
else :
    primeira_nota = nota2
    segunda_nota = nota1

while True :
    media = (primeira_nota + segunda_nota) / 2
    penalizacao += 0.5
    if media >= 6 :
        aprovado = True
    if aprovado :
        print(f"Média: {media:.1f} (aprovado)")
        print(f"Penalização: {penalizacao:.1f}")
        break
    else:
        print(f"Média: {media:.1f} (cursando)")
        print(f"Penalização: {penalizacao:.1f}")
    nota = float(input("\nNota? "))
    if nota > primeira_nota :
        segunda_nota = primeira_nota
        primeira_nota = nota
    elif nota > segunda_nota:
        segunda_nota = nota

media_final = media - penalizacao

print("\n===")
print(f"Notas válidas: {primeira_nota:.1f} e {segunda_nota:.1f}")
print(f"Média parcial na unidade: {media:.1f}")
print(f"Penalizações: {penalizacao:.1f}")
print(f"Média final na unidade: {media_final:.1f}")
