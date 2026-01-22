#Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
#'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su
#símbolo o un mensaje de aviso si la divisa no está en el diccionario.

moneda = {'Euro':'€','Dollar':'$', 'Yen':'¥'}
traduccion = input("Seleccione la moneda: ")

if traduccion in moneda:
    print(moneda[traduccion])
else:
    print("La moneda no está en el diccionario")