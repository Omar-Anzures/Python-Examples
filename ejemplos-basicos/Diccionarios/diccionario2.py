""" Escribir un programa que pregunte al usuario su nombre, edad, dirección y
teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje 
<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>. """

dictionary ={}

name = input("What is your name?: ")
age = input("What is your age?: ")
address = input("What is your addres: ")
phone = input("what is your phone numer?")
dictionary["Nombre"] = name
dictionary["Edad"] = age
dictionary["Direccion"] = address
dictionary["Telefono"] = phone

#<---------otra forma de ponerlo es asi--->:
""" 
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}

"""

print(f"\nSu nombre es:{dictionary['Nombre']}\ntiene: {dictionary['Edad']} años\ndireccion: {dictionary['Direccion']}\nnumero de telefono: {dictionary['Telefono']} ")


