# 2021-03-12, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula quantos campos de futebol cabem em 3 diferentes campos e mostra a média entre eles

campo1 = float(input())
campo2 = float(input())
campo3 = float(input())

tamanho1 = campo1 / 4000
tamanho2 = campo2 / 4000
tamanho3 = campo3 / 4000

media = (tamanho1 + tamanho2 + tamanho3) / 3

print("%.2f"% tamanho1)
print("%.2f"% tamanho2)
print("%.2f"% tamanho3)
print("%.2f"% media)


