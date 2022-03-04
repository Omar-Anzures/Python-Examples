"""Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados."""

def cuadrado(*numeros):
    lista=[]
    resultado=0
    for i in numeros:
        resultado=i**2
        lista.append(resultado)
    return lista
        

print(cuadrado(2,4,6,54,45,7,6))