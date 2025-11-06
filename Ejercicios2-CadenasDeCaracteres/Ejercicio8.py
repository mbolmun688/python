#Escribir un programa que pregunte por consola el precio de un producto en euros
#con dos decimales y muestre por pantalla el número de euros y el número de
#céntimos del precio introducido.
precio = str(input("Introduzca el precio: "))
cadena = precio.split(".")
print ("Los euros introducidos son", cadena[0], "y los centimos son", cadena[1])