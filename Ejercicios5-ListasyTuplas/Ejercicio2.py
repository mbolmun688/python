# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y 
# la muestre por pantalla el mensaje Yo estudio <asignatura>, 
# donde <asignatura> es cada una de las asignaturas de la lista.

array = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
longitudArray = len(array)
contador = 0
i = 0
while contador < longitudArray:
    print("Yo estudio",array[i])
    i += 1
    contador += 1