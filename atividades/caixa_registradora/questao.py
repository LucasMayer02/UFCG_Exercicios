# 2021-05-08, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a soma das vendas, a comissão e se 
# foi o suficiente para gerar lucro ou prejuizo

lista = [1000.0, 2000.0, 5000.0, 2500.0, 950.0]
meta = 2000.0

def caixa_registradora(lista, meta) :
    resultado = []
    total = comissao = 0
    for n in lista :
        if n < 1000 :
            parcela = n * 0.05
        elif n < 5000 :
            parcela = n * 0.10
        else :
            parcela = n * 0.15
        total += n
        comissao += parcela
    resultado.append(total)
    resultado.append(comissao)
    if total - comissao > meta :
        resultado.append("Lucro")
    else :
        resultado.append("Prejuizo")
    return resultado
