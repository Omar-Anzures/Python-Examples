"""Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión cada año que dura la inversión. """
amount = float(input("Ingresa una cantidad a invertir: "))
year = int(input("Ingresa los años a invertir: "))
interest = float(input("Ingresa los intereses por año: "))

total = 0

for i in range (year):
    rendimiento = interest/100
    ganancia = amount * rendimiento
    total += ganancia
    print(f"La ganancia de {i+1} años es de ${total} pesos ")

