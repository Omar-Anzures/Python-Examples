""" Escribir una función que reciba un número entero positivo y devuelva su factorial. """

def factorial(numero):
    productoria = 1
    for i in range(2,numero+1):
        productoria = productoria*i
    return productoria
           
fact=factorial(5)
print(fact)

