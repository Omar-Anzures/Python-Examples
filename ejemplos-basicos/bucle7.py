"""Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.  """

for i in range(1,11):
    print(f"\n<--------------- TABLA DEL {i} ----------------> ")
    for j in range (1,11):
        r = j*i
        print(f'\n                 {i} x {j} = {r}',end=" \n")
  
