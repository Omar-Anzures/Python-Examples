""" Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y 
la muestre por pantalla. """

lista = []

while True:
    opc=input("\n Elige una opcion\n 1.-Igresar materias\n 2.- Salir \n")
    
    if opc == "1":
        materias = input("Agregar materia: ")
        lista.append(materias)
        
    elif opc == "2":
        break
    
    else:
        print("-----Ingresa opcion correcta,intentelo de nuevo!-----")
        
    
print("Las materias son: ")
for i in lista:
    print(i) 

  
   