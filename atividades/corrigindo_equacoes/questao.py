# 2021-03-25, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula as raízes de uma equação de segundo grau

a = int(input())
b = int(input())
c = int(input())

delta = b **2 - 4 * a * c

if delta < 0 :
    print("sem raizes reais")

elif delta == 0 :
    raiz = (-b + delta**(1/2)) / (2 * a)
    
    print(f"x = {raiz:.2f}")

else:
    raiz1 = (-b + delta**(1/2)) / (2 * a)
    raiz2 = (-b - delta**(1/2)) / (2 * a)
    
    print(f"x1 = {raiz1:.2f}")
    print(f"x2 = {raiz2:.2f}")
