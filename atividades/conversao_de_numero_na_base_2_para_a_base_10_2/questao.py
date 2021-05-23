# 2021-03-24, lucas.mayer.almeida@ccc.ufcg.edu.br
# Converte número binário em número decimal 
# e mostra a decomposição dessa conversão

binario = input()
decimal = 0
valores = []


multiplicador = 2 ** (len(binario) - 1)

for i in range(len(binario)) :
    valor = int(binario[i]) * multiplicador
    decimal += valor
    valores.append(valor)
    multiplicador /= 2

multiplicador = 2 ** (len(binario) - 1)


for i in range(len(valores)) :
    print("%s * %d = %d" % (binario[i], multiplicador, valores[i]))
    multiplicador /= 2

print("%s(2) = %d(10)" % (binario, decimal))
