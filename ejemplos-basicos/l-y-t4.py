""" Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
los almacene en una  lista y los muestre por pantalla ordenados de menor a mayor. """

lista=[]

while True:
    num = input("\nOprime 'S' para salir :D\nIngresa los numeros de la loteria:\n ")
    if num.isdigit():
        lista.append(num)  
    elif num =='s':
        break    
    else:
        print("------->Introduce un digito!<--------")

lista.sort()
print(f"Los numeros ganadores son:",lista)
    
