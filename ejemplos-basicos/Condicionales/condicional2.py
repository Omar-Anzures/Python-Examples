""" Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el 
usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.  """
cadena = 'contraseña'

contra = input("Ingresa la contraseña: ")

if (cadena == contra.lower()):
    print("Son iguales las contraseñas")
else:
    print("No son iguales")