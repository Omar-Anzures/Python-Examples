"""Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de 
aviso si la divisa no está en el diccionario. """

moneda = {'Euro':'€','Dollar':'$','Yen':'¥'}

divisa = input("Ingresa el tipo de moneda que necesita: ")

print("El tipo de moneda es: ",moneda.get(divisa.title(),"No existe esta divisa"))