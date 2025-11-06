# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
# que el usuario escriba “salir” que terminará.

salida = ""
print("Usa la opción salir para salir del programa")
while salida != "salir":
    salida = str(input("Ingrese una frase: "))
    print(salida)
print("Saliendo...")