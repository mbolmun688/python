palabra = str(input("Inserte una palabra: "))
inversa = palabra[::-1]

if (palabra == inversa):
    print ("Es un palindromo")
else:
    print("No es un palidromo")