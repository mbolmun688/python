#Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla todos los números impares desde 1 hasta ese número separados por
#comas.
num = int(input("Ingrese un número: "))
cont = 1
while cont <= num:
    if cont % 2 != 0:
        print(cont, ",", end="")
    cont = cont + 1