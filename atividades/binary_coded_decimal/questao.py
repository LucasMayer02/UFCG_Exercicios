# 2021-04-05, lucas.mayer.almeida@ccc.ufcg.edu.br
# Representa um valor decimal de um binário BCD válido


while True :
    parte_1 = ""
    parte_2 = ""
    sequencia = input()
    if sequencia == "fim" :
        break
    if len(sequencia) != 8 :
        print("Tente novamente.")
    else:
        for i in range(len(sequencia)) :
            if i < 4 :
                parte_1 += sequencia[i]
            else :
                parte_2 += sequencia[i]
        if int(parte_1) > 1001 or int(parte_2) > 1001 :
            print("BCD inválido.")
        else :
            parte_1 = int(parte_1, 2)
            parte_2 = int(parte_2, 2)
            print(f"{parte_1}{parte_2}")
