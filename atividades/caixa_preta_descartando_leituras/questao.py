# 2021-04-05, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe quando um valor for negativo e quantos valores foram computados

peso = combustivel = altitude = 0

while True :
    medicao = input().split()
    if int(medicao[0]) < 0 :
        print("dado inconsistente. peso negativo.")
        break
    peso += 1
    if int(medicao[1]) < 0 :
        print("dado inconsistente. combustível negativo.")
        break
    combustivel += 1
    if int(medicao[2]) < 0 :
        print("dado inconsistente. altitude negativa.")
        break
    altitude += 1

print(f"peso: {peso}")
print(f"combustível: {combustivel}")
print(f"altitude: {altitude}")
