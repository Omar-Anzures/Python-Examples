"""Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por comas."""

numb=int(input("ingresa un numero entero: "))

for i in range (1,numb,2):
    print(i, end=", ")