""" Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista 
las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las 
asignaturas que el usuario tiene que repetir. """

materias=['Matemáticas','Física', 'Química', 'Historia','Lengua']
score_l =[]

for i in materias:
    print("\nMateria: \n", i)
    score = float(input("Ingresa la calificacion: "))
    if score <7:
      score_l.append(i)
      
print(score_l)
  
    
          
