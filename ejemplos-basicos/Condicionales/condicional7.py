""" Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes: 
Renta	                Tipo impositivo

Menos de 10000€     	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	        45%
Escribir un programa que pregunte al usuario su renta anual y
muestre por pantalla el tipo impositivo que le corresponde.
"""

renta = int(input("¿Cuanto pagas de renta?: "))


if (renta<1000):
    print(f'Tu renta es de {renta} te corresponde el 5%')
    
elif ((renta>1000) and (renta < 2000)):
    print(f'Tu renta es de {renta} te corresponde el 15%')
    
elif ((renta>2000) and (renta < 3500)):
    print(f'Tu renta es de {renta} te corresponde el 20%')
    
elif ((renta>3500) and (renta < 6000)):
    print(f'Tu renta es de {renta} te corresponde el 30%')
    
if (renta>6000):
    print(f'Tu renta es de {renta} te corresponde el 45%')

