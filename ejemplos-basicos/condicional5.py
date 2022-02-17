"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos
iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad
y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no."""

edad = int(input("¿Cuantos años tienes?: "))
ingresos = float(input("¿Cuales son tus ingresos mensuales?: "))

if ((edad >=16) and (ingresos >= 10000)):
    print("Si paga inpuestos")
    
else:
    print("Actualmente no disponible!")
    