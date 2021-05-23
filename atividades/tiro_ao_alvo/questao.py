# 2021-03-25, lucas.mayer.almeida@ccc.ufcg.edu.br
# Imprime a distância de cara tiro e calcula a média entre eles

tiros = []
acumulo = 0 

while True :
    eixos = input().split(", ")
    if len(eixos) == 1 :
        eixos = eixos[0].split(" ")
    if len(eixos) == 1 :
        eixos = eixos[0].split(",")
    eixo_x = float(eixos[0])
    eixo_y = float(eixos[1])
    distancia = (eixo_x ** 2 + eixo_y ** 2) **(1/2)
    if distancia > 200 :
        break
    tiros.append(distancia)
    acumulo += distancia

if len(tiros) == 0 :
    media = 0
else:
    media = acumulo / len(tiros)


for i in range(len(tiros)) :
    print(f"{tiros[i]:.2f}")

print("--")
print(f"num disparos: {len(tiros)}")
print(f"distancia media: {media:.2f}")
