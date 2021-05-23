# 2021-03-16, lucas.mayer.almeida@ccc.ufcg.edu.br
# Define se um ano é ou não bissexto

ano = int(input())
bissexto = False


if ano % 400 == 0 :
    bissexto = True

elif ano % 4 == 0 and ano % 100 != 0 :
    bissexto = True


if bissexto :
    print("%d é bissexto" % ano)

else :
    print("%d não é bissexto" % ano)
