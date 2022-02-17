""" Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con
un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte
al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
 """
 
nombre = input("¿Cual es tu nombre?: ")
sexo = input("¿Cual es tu sexo? ------- f(Femenino) -------  m(masculino): ")

if nombre.lower() >= "a" and nombre.lower()<="n":
    if sexo == 'f':
        print("Grupo A")
        
if nombre.lower() >= "n":
     if sexo == 'm':
        print("Grupo A")
        
if nombre.lower() > "n":
    if sexo == 'f':
        print("Grupo B")
        
if nombre.lower() >= "a" and nombre.lower()<="n":
    if sexo == 'm':
        print("Grupo B")

    