"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error."""



num1 = float(input("ingresa el primer numero: "))
num2 = float(input("ingresa el segundo numero: "))

if num2 == 0:
    print("Error ingresa un valor correcto!")
else:
    print(f"El valor de la divicion es: {num1/num2}")

