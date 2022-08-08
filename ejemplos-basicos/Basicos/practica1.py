kilos = float(input("Igresa tu peso en kilos: "))
estatura = float(input("Ingresa tu estatura en metros: "))
imc =  ((kilos/(estatura)**2))
print("Tu masa corporal es de: {:.2f}".format(imc))
