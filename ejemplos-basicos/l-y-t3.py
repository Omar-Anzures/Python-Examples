"""  Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura, y después las
muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde 
<asignatura> es cada una des las asignaturas de la lista y <nota> cada una de 
las correspondientes notas introducidas por el usuario. """
calificacion_l=[]
materias = ['Matemáticas', 'Física', 'Química', 'Historia' ,'Lengua']

for i in materias:
    print("Materia: ", i)
    calificacion = input("Ingresa la calificacion: ")
    calificacion_l.append(calificacion)
print("\n")
for j in range (len(materias)):
    print("Materia: "+materias[j]+ " / Calificacion: " + calificacion_l[j])
    
    