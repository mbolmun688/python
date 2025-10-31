#Escribir un programa que pida al usuario un número entero y muestre por pantalla
#un triángulo rectángulo como el de más abajo.

#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1


num  = int(input("Introduce un número: "))
cont = 1
while cont <= num:
    fila = cont
    while fila >= 1:
        print(fila, end=" ")
        fila = fila - 2
    print("")
    cont = cont + 2