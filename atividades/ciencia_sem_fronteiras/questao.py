# 2021-03-24, lucas.mayer.almeida@ccc.ufcg.edu.br
# Define quais condições são satisfeitas

nota = float(input())
creditos = int(input())
enem = False
curso = False


if nota >= 600 :
    enem = True

if creditos >= 83.2 and creditos <= 374.4 :
    curso = True


if enem and curso :
    print("Todas as condições satisfeitas.")

elif enem :
    print("Condição CRÉDITOS não satisfeita.")

elif curso :
    print("Condição ENEM não satisfeita.")

else:
    print("Nenhuma condição satisfeita.")
