#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
#año que dura la inversión.
invert = float(input("Cantidad a invertir: "))
inter = float(input("Interés anual: "))
anos = int(input("Número de años: "))
cont = 1
while anos >= cont:
    invert= invert * inter
    print("En el año",cont,"ganas",invert,"€")
    cont = cont + 1