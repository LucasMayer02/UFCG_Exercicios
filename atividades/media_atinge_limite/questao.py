# 2021-04-05, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula e exibe a primeira média maior que o número limite

lista_medias = []
total = unidades = 0
na_media = False

while True :
    valor = input()
    if valor == "-" :
        break
    total += float(valor)
    unidades += 1
    media = total / unidades
    lista_medias.append(media)

limite = float(input())

for i in range(len(lista_medias)) :
    if lista_medias[i] > limite :
        print(f"media = {lista_medias[i]:.1f}")
        print(f"num = {i + 1}")
        na_media = True
        break

if not na_media :
    print("limite não alcançado")
