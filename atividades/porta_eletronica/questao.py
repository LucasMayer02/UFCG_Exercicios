# 2021-04-01, lucas.mayer.almeida@ccc.ufcg.edu.br
# Cada consulta exibe quantos registros foram feitos em cada categoria

letras = []
registros = []
consultas = []

while True :
    possui = False
    existe = False
    identificador = input().split()
    if identificador == ["S"] :
        break
    acao = identificador[0]
    codigo = identificador[1][0]
    if acao == "R" :
        for i in range(len(letras)) :
            if letras[i] == codigo :
                registros[i] += 1
                possui = True
        if not possui :
            letras.append(codigo)
            registros.append(1)
    elif acao == "P" :
        for i in range(len(letras)) :
            if letras[i] == codigo :
                consultas.append(registros[i])
                existe = True
        if not existe :
            consultas.append(0)

for i in consultas :
    print(i)
