#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión.
inversion = float(input("Cantidad a invertir? "))
numerosaños = float(input("A cuantos años? "))
interesanual = float(input("A que interés anual? "))
resultado = inversion*(interesanual/100)*numerosaños
print("El capital obtenido de la inversion es: ",resultado)