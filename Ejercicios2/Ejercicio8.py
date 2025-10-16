#Escribir un programa que pregunte por consola el precio de un producto en euros
#con dos decimales y muestre por pantalla el número de euros y el número de
#céntimos del precio introducido.
precio = float(input("Introduzca el precio: "))
euros = int(precio)
centimos = (precio - euros) * 100
print("Los euros son",euros,"y los centimos son",int(centimos))