import random 

intentos = 5

while intentos != 0: 

    insertar = int(input("Ingresa un numero: "))
    numero = random.randint(1,10)

    if insertar == numero:
        print("Felicidades acertaste")
    
    else:
        intentos-=1
        print("intenta de nuevo")
    
        if insertar > numero:
            print("El numero que insertaste es mayor")
        
        else:
            print('El numero que insertaste es menor')
            
    if intentos == 0:
        print('No te quedan intentos,gracias por jugar!')
            
    





    