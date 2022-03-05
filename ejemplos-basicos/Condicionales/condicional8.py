""" En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados 
pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada 
por la puntuación del nivel. 

Nivel	    Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
así como la cantidad de dinero que recibirá el usuario.
"""
ina = 0
acep = 0.4
meri = 0.6
nivel = 2400
puntuacion =  float(input("Ingresa los puntos obtenidos del empleado: "))

if puntuacion == ina:
    print(f"Tu nivel de rendimiento es INACEPTABLE, total a pagar: {nivel} ")
    

elif puntuacion == acep:
    print(f"Tu nivel de rendimiento es ACEPTABLE, total a pagar: {nivel*acep} ")
    

elif puntuacion == ina:
    print(f"Tu nivel de rendimiento es MERITORIO, total a pagar: {nivel*meri} ")
    
else:
    print(f"Tu nivel de rendimiento es MERITORIO, total a pagar: {nivel*puntuacion} ")
