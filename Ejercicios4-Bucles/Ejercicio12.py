# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = str(input("Ingrese una frase: "))
letra = input("¿Qué letra seleccionas? ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra",letra,"aparece",contador,"veces en la frase.")