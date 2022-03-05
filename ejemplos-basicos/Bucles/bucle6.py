""" Escribir un programa que pida al usuario un número entero y muestre por pantalla 
un triángulo rectángulo como el de más abajo, de altura el número introducido. 
*
**
***
****
*****
"""
num = int(input("Ingresa un numero: "))

for i in range(num+1):
    print("*"*i)

for i in range(num+1):
    espacios = num-i
    print(" "*espacios+'*'*i)
    
    