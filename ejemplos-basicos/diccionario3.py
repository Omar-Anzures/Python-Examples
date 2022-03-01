""" Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese
número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. """

precios = { 'platano' : 1.35,
            'manzana': 0.80,
            'pera' : 0.85,
            'naranja': 0.70  
          }

fruta = input("¿Que fruta vas a comprar?: ")
kilos = float(input("kilos a comprar: "))

if fruta in precios:
    precio=precios[fruta]*kilos
    print(f"Total a pagar ${precio} pesos")
else:
    print("No existe en el diccionario")