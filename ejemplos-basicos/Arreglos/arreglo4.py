"""Dado el siguiente arreglo

array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])

Selecciona la segunda fila
Selecciona la primera y tercera fila
Selecciona las tres columnas de enmedio"""

import numpy as np

ejemplo = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])

#Selecciona la segunda fila
print(ejemplo[1],"\n")

#Selecciona la primera y tercera fila
print(ejemplo[[0,2]],"\n")

#Selecciona las tres columnas de enmedio
print(ejemplo[:,1:4],"\n")