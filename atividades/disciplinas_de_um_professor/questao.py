# 2021-05-05, lucas.mayer.almeida@ccc.ufcg.edu.br
# 

def disciplinas(alocacao, professor) :
    materias = []
    creditos = 0
    for k, v in alocacao.items() :
        for i in v :
            if i == professor :
                materias.append(k[0])
                creditos += k[1]
    return (materias, creditos)
