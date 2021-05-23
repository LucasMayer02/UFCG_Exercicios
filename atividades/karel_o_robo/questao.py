# 2021-04-03, lucas.mayer.almeida@ccc.ufcg.edu.br
# Movimenta um ponto em um plano cartesiano e 
# define quando o eixo x é o dobro do eixo y 

eixo_x = eixo_y = 0
chegou = False

while True :
    movimento = input().split()
    direcao = movimento[0]
    unidades = int(movimento[1])
    if unidades == 0 :
        break
    if direcao == "C" :
        eixo_y += unidades
    elif direcao == "B" :
        eixo_y -= unidades
    elif direcao == "E" :
        eixo_x -= unidades
    elif direcao == "D" :
        eixo_x += unidades
    if abs(eixo_x) * 2 == abs(eixo_y) and eixo_x != 0 :
        chegou = True
        break

if chegou :
    print(f"Parabéns, conquista do portal ({eixo_x}, {eixo_y})")
else:
    print("Fim de jogo")
