# 2021-03-29, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe as melhores opções para valor, tamanho e conforto

melhor_valor = melhor_tamanho = melhor_conforto = 0

while True :
    registro = input().split(",")
    if registro == ["---"] :
        break
    valor = float(registro[0])
    tamanho = int(registro[1])
    conforto = int(registro[2])
    empresa = str(registro[3])
    if valor < melhor_valor or melhor_valor == 0:
        melhor_valor = valor
        quarto_valor = empresa
    if tamanho > melhor_tamanho :
        melhor_tamanho = tamanho
        quarto_tamanho = empresa
    if conforto > melhor_conforto :
        melhor_conforto = conforto
        quarto_conforto = empresa

while True :
    operacao = input()
    if operacao == "valor" :
        print(quarto_valor)
    elif operacao == "tamanho" :
        print(quarto_tamanho)
    elif operacao == "conforto" :
        print(quarto_conforto)
    else:
        break
