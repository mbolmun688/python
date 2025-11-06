#Los teléfonos de una empresa tienen el siguiente formato
#prefijo-número-extension donde el prefijo es el código del país +34, y la
#extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un
#programa que pregunte por un número de teléfono con este formato y muestre por
#pantalla el número de teléfono sin el prefijo y la extensión.
telefono = input("Inserta el numero de telefono con formato prefijo-numero-extension: ")
Ntelefono = telefono[4:-3]
print("El número sin el prefijo ni la extension es ",Ntelefono)