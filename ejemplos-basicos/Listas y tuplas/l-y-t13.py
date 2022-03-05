""" Escribir un programa que pregunte por una muestra de números, separados por comas, 
los guarde en una lista y muestre por pantalla su media y desviación típica.
 """
import math

lista=[]
rango = int(input("Ingresa un rango: "))
res=0
varianza = 0
v2=0

for i in range (rango):
    muestra = float(input("Ingresa un numero: "))
    lista.append(muestra)

for r in range (len(lista)):
    res += lista[r]
    media = res/len(lista)
    
for j in range (len(lista)):
        varianza += (lista[j]-media)**2
        v2 = ((varianza)/(len(lista)-1))
        
print("La media es de : {}\nLa desviacion tipica es de: {:.2f}".format(media,math.sqrt(v2)))
        
