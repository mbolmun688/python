# Escribir un programa que pida al usuario un número entero y muestre por pantalla si
# es un número primo o no.

salida = 1

while salida >= 1:
    print("Pulse 0 para salir del programa")
    num = int(input("Elija un número para saber si es primo: "))
    if num == 0:
        print("Saliendo...")
        break
    if num < 2:
        print(f"{num} no es primo.")
        continue
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{num} es primo.")
    else:
        print(f"{num} no es primo.")2