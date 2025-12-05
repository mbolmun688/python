#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
#letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista
#resultante.

import string

abecedario = list(string.ascii_lowercase)
abecedario = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 != 0]
print(abecedario)
