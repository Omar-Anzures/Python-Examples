"""  Escribir una función que calcule el área de un círculo y otra que calcule el volumen
de un cilindro usando la primera función."""

pi=3.14
def circulo(radio):
    area = (pi*(radio)**2)
    return area

def cilindro(area,altura):
    volumen = circulo(area)*altura
    return volumen
    
print("El resultado es: ",cilindro(3,5))
    
    
