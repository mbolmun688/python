#Escribir un programa que pida al usuario que introduzca una frase en la consola y
#una vocal, y después muestre por pantalla la misma frase pero con la vocal
#introducida en mayúscula.
frase = str(input("Introduce una frase: "))
vocal = input("Introduce una vocal: ")
fraseRep = frase.replace(vocal, vocal.upper())
print(fraseRep)