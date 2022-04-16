"""Escribir una función que reciba una muestra de números en una lista y devuelva su media."""



def media(*numeros):
    return sum(numeros)/len(numeros)

print(media(10,10,10))

""" mi funcion fea xc
def media(*numeros):
    resultado=0
    for i in numeros:
        resultado+=i/len(numeros)
    return resultado
              
print(media(10,10,10))
"""