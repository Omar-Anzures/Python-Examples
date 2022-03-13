#Crear un vector con valores dentro del rango 10 a 49
import numpy as np 

a= np.arange(10,50)
print(a,"\n")

#Invertir el vector
print(a[::-1],"\n")

#Crear una matriz 3x3 con valores de 0 a 8
a=np.arange(0,9).reshape(3,3)
print(a,"\n")

#Encontrar los indices que no son ceros del arreglo [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]
a = np.array([1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0])
p = np.argwhere( a!=0 )
print(p,"\n")

#Crear una matriz identidad de 6x6
a=np.identity(6)
print(a,"\n")

#Crear una matriz con valores al azar con forma 3x3x3
r = np.random.random((3,3,3))
print(r,"\n")

#Encontrar los indices de los valores minimos y maximos de la anterior matriz
print( r.argmax() )
print( r.ravel()[r.argmax()] )
print(r,"\n")
print(np.unravel_index(r.argmax(), r.shape))
r=r[np.unravel_index(r.argmax(), r.shape)]
print(r,"\n")

#Crear una matriz de 10x10 con 1's en los bordes y 0 en el interior (con rangos de indices)
z = np.ones((10,10))

z[1:-1,1:-1] = 0
print(z,"\n")

#Crear una matriz de 5x5 con valores en los renglones que vayan de 0 a 4
r=np.tile( np.arange(0,5) , 5).reshape(5,5)
print(r,"\n")

#Crear dos arreglos al azar A y B, verificar si son iguales
a = np.random.random((3,3))
b = np.random.random((3,3))

print(a == b )

