#Escribir un programa que pida al usuario un número entero y muestre por pantalla si
#es par o impar.
numer = int(input("Ingrese número para saber si es par o impar: "))
if (numer % 2) == 0:
    print("Es par")
else:
    print("Es impar")