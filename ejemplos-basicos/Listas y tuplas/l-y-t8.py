"""  Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo. """

palabra = input("Ingresa una palabra: ")


if palabra.replace(" ", "") == palabra[::-1].replace(" ", ""):
    print("Es palindromo" )

else:
    print("No es palindromo")
    