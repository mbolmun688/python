#Escribir un programa que pida al usuario un número entero y muestre por pantalla
#un triángulo rectángulo como el de más abajo, de altura el número introducido.
#*
#**
#***
#****
#*****
num  = int(input("Introduce un número: "))
cont = 1
simbol = "*"
while num + 1 > cont:
    print((simbol * cont))
    cont = cont + 1