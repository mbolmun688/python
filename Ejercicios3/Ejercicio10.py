#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#Los ingredientes para cada tipo de pizza aparecen a continuación.
#● Ingredientes vegetarianos: Pimiento y tofu.
#● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
#en función de su respuesta le muestre un menú con los ingredientes disponibles
#para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
#tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
#pizza elegida es vegetariana o no y todos los ingredientes que lleva.
print("Los ingredoentes vegetarianos son: Pimiento y tofu")
print("Los ingredientes no vegetarianos son: Peperoni, Jamón y Salmón")
vegOno = str(input("Quieres pizza vegetariana o carnivora: "))
if vegOno == "vegetariana":
    ingrediente = str(input("Elige uno de los dos ingredientes: "))
    if ingrediente == "tofu":
        print("Tu opcion elegida es vegetaria y lleva: Mozzarela, Tomate y tofu")
    elif ingrediente == "pimiento":
        print("Tu opcion elegida es vegetaria y lleva: Mozzarela, Tomate y pimiento")
    else:
        print("Opción no valida")
elif vegOno == "carnivora":
    ingrediente = str(input("Elige uno de los dos ingredientes: "))
    if ingrediente == "peperoni":
        print("Tu opcion elegida es carnivora y lleva: Mozzarela, Tomate y peperoni")
    elif ingrediente == "jamon":
        print("Tu opcion elegida es carnivora y lleva: Mozzarela, Tomate y jamón")
    elif ingrediente == "salmon":
        print("Tu opcion elegida es carnivora y lleva: Mozzarela, Tomate y salmón")
    else:
        print("Opción no valida")