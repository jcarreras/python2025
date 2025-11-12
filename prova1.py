a = float(input("Escriure el primer nombre: "))
b = float(input("Escriure el segon nombre: "))
d = float(input("Escriure el tercer nombre: "))
c = a + b + d
print("El resultat de la suma {} + {} + {} és {}".format(a, b, d, c))
if c>20:
    print("La suma és major que 20, que és {}".format(c))
else:
    print("La suma és menor que 20, que és {}".format(c))
    
c = a * b * d
print("El resultat de la multiplicació {} * {} * {} és {}".format(a, b, d, c))

