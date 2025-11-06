#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#calcule el índice de masa corporal y lo almacene en una variable, y muestre por
#pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el
#índice de masa corporal calculado redondeado con dos decimales.
peso = float(input("Cual es tu peso en kg? "))
altura = float(input("Cual es tu altura en metros? "))
imc = (peso / (altura)**2)
imcRound = round(imc, 2)
print ("Tú indice de masa corportal es", imc ,"donde", imcRound , "es el indice de masa corporal calculado redondeado a los decimales")