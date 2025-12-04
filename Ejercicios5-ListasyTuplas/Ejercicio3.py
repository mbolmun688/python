#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
#nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
#mensaje En <asignatura> has sacado <nota> donde <asignatura> es
#cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
#notas introducidas por el usuario.

lista1 = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
contador = len(lista1)
notas = []
for i in range (0,contador):
    quest = float(int(f"Que sacaste en{ lista1[i]}:"))
    notas.append(quest)

for i in range (0,contador):
    print ("En", lista1[i], "sacaste un", notas[i])