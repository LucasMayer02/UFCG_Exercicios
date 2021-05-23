# 2021-03-26, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula aproximações de pi

sequencia = int(input())
while sequencia != 0 :
    pi = 0
    divisor = 1
    while sequencia > 0:
        pi += (1 / divisor)
        if divisor > 0 :
            divisor = - divisor - 2
        elif divisor < 0 :
            divisor = - divisor + 2
        sequencia -= 1
    pi *= 4
    print(f"{pi:.6f}")
    sequencia = int(input())
