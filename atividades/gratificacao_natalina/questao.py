# 2021-03-22, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a gratificação e o salário no final do mês
# por meio do tipo de cargo e números de falta

codigo = int(input())

if codigo > 2 :
    faltas = int(input())


if codigo == 1:
    salario = 25000

elif codigo == 2:
    salario = 15000
    
elif  codigo == 3 :
    if faltas == 0 :
        gratificacao = 500

    else:
        gratificacao = (235 - faltas) * 2

    salario = 8000 + gratificacao

elif codigo == 4 :
    if faltas == 0 :
        gratificacao = 300
    
    else:
        gratificacao = (235 - faltas)

    salario = 5000 + gratificacao 

elif codigo == 5 :
    if faltas == 0 :
        gratificacao = 200

    else:
        gratificacao = (235 - faltas) * 0.7

    salario = 2800 + gratificacao


if codigo < 3 :
    print(f"Deverá receber em dezembro R$ {salario:.2f}.")
else:
    print(f"Valor da gratificação R$ {gratificacao:.2f}.")
    print(f"Deverá receber em dezembro R$ {salario:.2f}.")
