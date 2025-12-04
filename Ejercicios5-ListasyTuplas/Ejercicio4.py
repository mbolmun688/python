#Escribir un programa que pregunte al usuario los números ganadores de la lotería
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
#a mayor.

cont = input("Cuantos fueron los ganadores")
nums = []
for i in range(0,cont):
    temp = input("Cuales fueron los ganadores?")
    nums.append(temp)

nums.sort(reverse=True)

print("Los ganadores son:")
for i in nums:
    print(i)