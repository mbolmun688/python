#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
#coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas = int(input("¿Cuantas horas trabajadas?"))
pago = int(input("¿Cuanto cobras por horas?"))
resultado = horas * pago
print("Las horas echadas son" , horas , "que se cobran a" , pago , "y has ganado", resultado)