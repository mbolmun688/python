#Escribir un programa que guarde en un diccionario los precios de las frutas de la
#tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
#precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe
#mostrar un mensaje informando de ello.

preciosFruta={'Platano':1.35,'Manzana':0.80,'Pera':0.85,'Naranaja':0.70}

frutaSelect=input("¿Qué fruta quieres? ")
kilosSelect=float(input("¿Cuantos kilos quieres? "))

if frutaSelect in preciosFruta:
    select=preciosFruta[frutaSelect]
else:
    print("Seleccione una fruta")

print ("El kilo de",frutaSelect ,"es", (kilosSelect*select))