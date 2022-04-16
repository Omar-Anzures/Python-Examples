"""Escribir una función que reciba una muestra de números en una lista y devuelva un
diccionario con su media, varianza y desviación típica."""


def varios(*numeros):
    dicc={}
    varianza=0
    v2=0
    #La media es la media aritmética de un conjunto de números. suma/longitud
    media=(sum(numeros)/(len(numeros)))
 
    for j in numeros:
        varianza = varianza + (j-media)**2
    v2=varianza/(len(numeros))
    desviacion=v2**(1/2)    
    print(desviacion)
        
        
varios(10, 32, 24, 26, 40, 30)  