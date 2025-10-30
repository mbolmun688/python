#Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla la cuenta atrás desde ese número hasta cero separados por comas.
num = int(input("Ingrese un número entero positivo: "))
while num > 0:
    print(num,",",end="")
    num = num -1