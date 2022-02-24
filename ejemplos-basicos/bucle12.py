""" Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase. """

frase = input("Introduce una frase: ")
letra = input("¿Introduce la letra que deseas contar?: ")
c=0

for i in frase:
    if i == letra:   
        c = c+1
print(f'La letra {letra} aparece {c} veces en la oracion')



    