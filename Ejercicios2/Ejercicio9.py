#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
#dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
#anterior para que también funcione cuando el día o el mes se introduzcan con un
#solo carácter.
fecha = str(input("Ingresa tu fecha de nacimiento en formato dd/mm/aaaa: "))
separacion = fecha.split("/")
print("El dia es",separacion[0],"el mes es",separacion[1], "y el año es",separacion[2])