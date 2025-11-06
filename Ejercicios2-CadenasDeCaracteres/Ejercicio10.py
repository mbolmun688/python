#Escribir un programa que pregunte por consola por los productos de una cesta de la
#compra, separados por comas, y muestre por pantalla cada uno de los productos en
#una línea distinta.
products = str(input("Ingrese los productos de la cesta separado por comas: "))
print(*products.split(","), sep="\n")