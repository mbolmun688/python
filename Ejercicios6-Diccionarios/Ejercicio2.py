#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
#y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
#<nombre> tiene <edad> años, vive en <dirección> y su número de
#teléfono es <teléfono>.

nombre=input("Ingrese su nombre: ")
edad=input("Ingrese su edad: ")
direccion=input("Ingrese su direccion: ")
telefono=input("Ingrese su telefono: ")

dicc={'nom':nombre,'age':edad,'direcc':direccion,'tlf':telefono}

print ("Su nombre es:",dicc['nom'])
print ("Su edad es:",dicc['age'])
print ("Su dirección es:",dicc['direcc'])
print ("Su teléfono es:",dicc['tlf'])