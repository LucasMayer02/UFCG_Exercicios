# 2021-03-23, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula quantas unidades são necessárias e o valor que será pago

produto = input()
hectares = int(input())


if produto == "Fungicida" :
    unidades = hectares // 50

    if hectares % 50 != 0 :
        unidades += 1
    
    valor = unidades * 320

elif produto == "Herbicida" :
    unidades = hectares * 0.3 // 1

    if hectares * 0.3 % 1 != 0 :
        unidades += 1

    valor = unidades * 100

elif produto == "Inseticida" :
    unidades = hectares * 2.5 // 30
    
    if hectares * 2.5 % 30 != 0 :
        unidades += 1

    valor = unidades * 400
    

print(f"{unidades:.0f} {produto}(s). {valor:.2f} reais.")
