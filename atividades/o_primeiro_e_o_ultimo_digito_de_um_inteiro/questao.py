# 2021-03-12, lucas.mayer.almeida@ccc.ufcg.edu.br
# Identifica o primeiro e o último dígito de um número de 4 dígitos

numero = int(input())

primeiro = numero // 1000
ultimo = numero % 10

print("%d %d" % (primeiro, ultimo))
