""" Escribir un programa que almacene en una lista los números del 1 al 10 y
los muestre por pantalla en orden inverso separados por comas."""

lista=[]

for i in range(1,11):
    lista.append(i)
    
lista.reverse()
print(lista)
