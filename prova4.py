#a =  [1, "a", "Capça", [2], 1, "a"]
a = [10, 9, 8, 7, 6, 5, 1, 2, 3, 4]
# Passar els elements de la llista a string
for i in range(len(a)):
    a[i]=str(a[i])
# Crear un únic string separat per guió
print("-".join(a))







"""
b = a.copy()
b[0]=100
print(a)
print(a[::-1]) # Retorna una llista invertida, però no modifica l'original
print(a)
print(a.reverse()) # No retorna res, però modifica la llista original
print(a)
a.sort()
print(a)
for i in range(len(a)):
    a[i]=str(a[i])
a.sort()
print(a)
for e in a:
    if a.count(e)>1:
        print(e)
c = a.count("a")
print(c)

c = "capça" in a
print(c)
print(len(a))
c = a.pop(2)
a.clear()
a.remove([2])
a[0]= "Hola, som en Ramis"
del a[:]
a.insert(-2,[3, 2])
a.append(10)
a.append("Cadena nova")
a.append([10, 11, 12])
a.extend([10, "Cadena nova", [10, 11, 12]])
print(a)
"""

"""
for e in a:
    print(e)
for i in range(len(a)):
    a[i]*=2 # --> a[i]= a[i]*2
    print("La posició {} té el valor {}".format(i,a[i]))
for i,e in enumerate(a):
    print("La posició {} té el valor {}".format(i,e))
"""
