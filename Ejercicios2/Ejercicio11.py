#Escribir un programa que pregunte el nombre el un producto, su precio y un número
#de unidades y muestre por pantalla una cadena con el nombre del producto seguido
#de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
#tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
producto = str(input("Ingrese el producto: "))
precio = float(input("Ingrese el precio: "))
unidades = int(input("Ingrese las unidades: "))
print("El producto {} tiene un precio unitario de {:06.2f}, con {:03d} unidades, el coste total es de {:08.2f}".format(producto, precio, unidades, precio * unidades))