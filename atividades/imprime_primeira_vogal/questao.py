# 2021-03-22, lucas.mayer.almeida@ccc.ufcg.edu.br
# Define a primeira vogal de uma palavra

palavra = input()
vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vogal = ""

for i in palavra :
    if i in vogais :
        vogal = i 
        break

if vogal == "" :
    print("-")
else:
    print(vogal)
