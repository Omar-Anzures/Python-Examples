"""Escribir un programa que pida al usuario una palabra y 
muestre por pantalla el número de veces que contiene cada vocal. """

palabra = input("Ingresa una palabra: ")
vocales = ['a','e','i','o','u']


for v in vocales:
    a=0
    for p in palabra:
        if v==p:
            a+=1
    print(v,a)
    
            
              
            
            