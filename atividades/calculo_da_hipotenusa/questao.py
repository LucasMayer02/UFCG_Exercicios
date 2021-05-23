# 2021-03-12, lucas.mayer.almeida@ccc.ufcg.edu.br
# Calcula a hipotenusa por meio de dois catetos 

cateto1 = float(input("Medida do Cateto 1? "))
cateto2 = float(input("Medida do Cateto 2? "))

hipotenusa = ((cateto1 **2) + (cateto2 **2))**(1/2)

print("Medida da Hipotenusa: %.2f"% hipotenusa)
