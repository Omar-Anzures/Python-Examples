#Arma un arreglo de una dimensión desde una compresnidón de lista que produce todos los números nones del 1 al 30

import numpy as np 

a = np.array([n for n in range(1,30,2)])
print(a)