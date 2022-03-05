""" Escribir un programa que pida al usuario un número entero 
y muestre por pantalla si es un número primo o no. """

n = int(input("Ingresa un numero entero mayor que 2: "))

for i in (2,n):
   for j in (1,n+1):
        residuo = n%i
        print(residuo)
        #resultado = ((n/j) + residuo)
        #print(resultado)
      
    
     
    
    