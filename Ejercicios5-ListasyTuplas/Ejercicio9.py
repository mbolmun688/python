#Escribir un programa que pida al usuario una palabra y muestre por pantalla el
#número de veces que contiene cada vocal.

frase = str(input("Ingrese una palabra: "))
letra = input("¿Qué letra seleccionas? ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra",letra,"aparece",contador,"veces en la frase.")