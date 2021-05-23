# 2021-03-22, lucas.mayer.almeida@ccc.ufcg.edu.br
# Define a menor sequência de DNA

dna1 = input()
dna2 = input()
dna3 = input()

if len(dna1) <= len(dna2) and len(dna1) <= len(dna3) :
    print(f"{dna1} {len(dna1)}")

elif len(dna2) <= len(dna1) and len(dna2) <= len(dna3) :
    print(f"{dna2} {len(dna2)}")

elif len(dna3) <= len(dna1) and len(dna3) <= len(dna2) :
    print(f"{dna3} {len(dna3)}")
