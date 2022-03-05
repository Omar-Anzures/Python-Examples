
from numpy import number


num= int(input("Ingresa el numero 4: "))
contador=0

while(num < 817):
    num=num*4
    contador=contador+1
    print(f'La potencia de {contador} es igual a : {num}')