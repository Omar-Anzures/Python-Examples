
actual=2022
edad = int(input("¿Ingresa el año de nacimiento? : "))
r= actual-edad


if (r >= 25):
    print(f'La edad es de {r}, por lo tanto es posible')
    
else:
    print("No es posible, es menor de edad")