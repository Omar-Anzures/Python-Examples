""" Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta 
que el usuario escriba “salir” que terminará. """

frase =""

while frase != 'salir':
    frase = input("Ingresa algo: ")
    if frase == 'salir':
        break
    else:
        print(frase)
        