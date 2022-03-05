""" Escribir una función que convierta un número decimal en binario y otra que 
convierta un número binario en decimal."""

def decimal(numero):
    modulos=[]
    
    while numero!= 0:#mientras numero de entrada es diferente a 0
        modulo = numero % 2#guardamos el modulo 
        cociente = numero // 2#guardamos la cociente
        modulos.append(modulo)#agregamos el modulo a la lista
        numero = cociente#el cociente pasa a ser el numero de entrada por ejemplo si es 12/2 = 6 6/2= 3 ....
    return "".join(map(str,modulos[::-1]))#"".join() itera todos los elementos en el objeto map y devuelve los elementos concatenados como una cadena.
    
def binario(numero):
    numero_decimal = 0 #aquí iremos sumando el resultado de cada multiplicación
    for posicion, digito_string in enumerate(numero[::-1]):
        numero_decimal += int(digito_string) * 2 ** posicion
        
    return numero_decimal

print(decimal(86))
print(binario('1010110'))

