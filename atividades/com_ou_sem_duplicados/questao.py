# 2021-03-24, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe se existem números duplicados

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5 :
    duplicados = True

elif num2 == num3 or num2 == num4 or num2 == num5 :
    duplicados = True

elif num3 == num4 or num3 == num5 :
    duplicados = True

elif num4 == num5 :
    duplicados = True

else:
    duplicados = False


if duplicados :
    print("com duplicados")

else:
    print("sem duplicados")
