# 2021-03-14, lucas.mayer.almeida@cc.ufcg.edu.br
# Definir se o docente tem a promocão deferida ou inferida e os motivos;

semestres = int(input())
a_ensino = int(input())
prdc_intelectual = int(input())
a_orientacao = int(input())
a_administrativas = int(input())
deferimento = True
pont_minima = True

media = (a_ensino + prdc_intelectual + a_orientacao + a_administrativas) / 4

if semestres < 4 :
    deferimento = False

elif a_ensino < 320 :
    deferimento = False
    pont_minima = False

elif prdc_intelectual < 100 :
    deferimento = False
    pont_minima = False

elif a_orientacao < 20 :
    deferimento = False
    pont_minima = False

elif media < 140 :
    deferimento = False


if deferimento:
    print("Promoção deferida. Parabéns!")
    
else:
    if semestres < 4:
        print("Promoção indeferida. Número de semestres insuficiente.")

    elif not pont_minima:
       print("Promoção indeferida. Pontuação mínima não alcançada.")
       
    else:
        print("Promoção indeferida. Média insuficiente.")
