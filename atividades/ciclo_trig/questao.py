# 2021-03-15, lucas.mayer.almeida@ccc.ufcg.edu.br
# Define o quadrante de um ângulo dentro do ciclo trigonometrico

angulo = int(input())


resto = angulo % 360


if angulo == 0 or resto == 0 or resto == 90 or resto == 180 or resto == 270 :
    print("Sobre eixos")

elif resto > 0 and resto < 90 :
    print("Quadrante 1")

elif resto > 90 and resto < 180 :
    print("Quadrante 2")

elif resto > 180 and resto < 270 :
    print("Quadrante 3")

elif resto > 270 and resto < 360 :
    print("Quadrante 4")
