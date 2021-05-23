# 2021-03-29, lucas.mayer.almeida@ccc.ufcg.edu.br
# Exibe uma operação inválida e calcula o saldo

limite = int(input())
saldo = float(input())
erro = False

while True :
    operacao = input().split()
    operador = str(operacao[0])
    valor = float(operacao[1])
    if operador == "depósito" :
        if valor > 1000 :
            erro = True
            break
        saldo += valor
    elif operador == "saque" :
        if valor > saldo or limite == 0 :
            erro = True
            break
        saldo -= valor
        limite -= 1

if erro :
    print(f"Operação inválida: {operador} {valor:.2f}.")

print(f"Seu saldo é R$ {saldo:.2f}.")
