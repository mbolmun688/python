#Escribir un programa que pida al usuario dos números enteros y muestre por
#pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde
#<n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente
#y el resto de la división entera respectivamente.
n = int(input("Introduce un número entero "))
m = int(input("Introduce otro número entero "))
c = n / m
r = n % m
print("El coeficiente y el resto de" , n , "y" , m , "es" , c ,"y" , r)