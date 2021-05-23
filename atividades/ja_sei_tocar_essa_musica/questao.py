# 2021-04-15, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função verifica se todas as notas na 
# lista de musica estão na de acordes

def sei_tocar_musica(musica, acordes) :
    for i in range(len(musica)) :
        possui = False
        for j in range(len(acordes)) :
            if musica[i] == acordes[j] :
                possui = True
                break
        if not possui :
            return False
    return True
