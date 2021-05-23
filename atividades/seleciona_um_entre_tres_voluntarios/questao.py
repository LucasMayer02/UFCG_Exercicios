# 2021-03-23, lucas.mayer.almeida@ccc.ufcg.edu.br
# Define qual tem prioridade por ordem alfabética ou ordem de chegada

pessoa1 = input()
pessoa2 = input()
pessoa3 = input()
caso_1 = False

if pessoa1[0] < pessoa2[0] and pessoa1[0] < pessoa3[0] :
    primeira_pessoa = pessoa1
    caso_1 = True

elif pessoa2[0] < pessoa1[0] and pessoa2[0] < pessoa3[0] :
    primeira_pessoa = pessoa2
    caso_1 = True

elif pessoa3[0] < pessoa1[0] and pessoa3[0] < pessoa2[0] :
    primeira_pessoa = pessoa3
    caso_1 = True

elif pessoa1[0] == pessoa2[0] or pessoa1[0] == pessoa3[0] :
    primeira_pessoa = pessoa1

elif pessoa2[0] == pessoa3[0] :
    primeira_pessoa = pessoa2


if caso_1 :
    print(f"{primeira_pessoa} (1)")

else:
    print(f"{primeira_pessoa} (2)")
