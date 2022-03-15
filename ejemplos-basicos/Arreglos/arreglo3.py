""" Usa el generador de numeros aleatoreos de numpy (np.random.randint) 
para crear una rreglo de 12 calificaciones aleatorias del 60 al 100, y luego 
dale forma en una matriz de 3x4. Calcula el promedio de todas las calificaciones,
el promedio de cada columna y de cada fila. """

import numpy as np
import random


calificacion = np.random.randint(60,100,12).reshape(3,4)

#promedio
r = calificacion.mean()
print(r)

#promedio por columnas
r = calificacion.mean(axis = 1)
print(r)

#promedio por filas
r = calificacion.mean(axis = 0)
print(r)