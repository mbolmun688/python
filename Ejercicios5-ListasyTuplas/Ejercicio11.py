#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y
#muestre por pantalla su producto escalar.

v1 = [1, 2, 3]
v2 = [-1, 0, 2]

producto_escalar = sum(a*b for a, b in zip(v1, v2))
print("El producto escalar de los vectores", v1, "y", v2, "es:", producto_escalar)
