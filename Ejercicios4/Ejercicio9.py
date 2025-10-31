#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
#correcta.

passwd = str(input("Ingrese una contraseña: "))
sec = 0
while sec < 1:
    userpasswd = str(input("Ingrese una contraseña: "))
    if passwd == userpasswd:
        print("Contraseña correcta")
        sec = 1
    else:
        print("Contraseña incorrecta: ")
