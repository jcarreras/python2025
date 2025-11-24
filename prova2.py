"""for i in range(1,10,3):
    print("{} * 5 = {}".format(i, i*5))
"""
def menu_principal():
    opcio=0
    while opcio<1 or opcio>3:
        opcio = int(input(""" Elegeixi una opció: 
                        1. Calculadora decimal
                        2. Calculadora real(floats)
                        3. Sortir \n"""))
        if opcio>0 and opcio<4:
            return opcio
        else:
            print("L'opcio seleccionada no és correcte, torni-ho a provar!!\n")

menu_principal()

a = int(input("Escriu el primer operand: "))
b = int(input("Escriu el segon operand: "))
if opcio==1:
    print("La suma de {}  + {} és {}".format(a, b, a+b))
elif opcio==2:
    print()