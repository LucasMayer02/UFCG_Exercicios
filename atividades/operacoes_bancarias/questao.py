# 2021-04-08, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula o saldo da conta de uma pessoa após saques e depositos

pessoa = input().split()
nome = pessoa[0]
saldo = float(pessoa[1])

while True :
    operacao = input().split()
    codigo = int(operacao[0])
    if codigo == 3 :
        break
    valor = float(operacao[1])
    if codigo == 1 :
        saldo -= valor
    elif codigo == 2 :
        saldo += valor

print(f"Saldo de R$ {saldo:.2f} na conta de {nome}")
