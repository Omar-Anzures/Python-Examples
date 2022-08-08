#Realizar una clase que administre una agenda. 
# Se debe almacenar para cada contacto el nombre, 
# el teléfono y el email. Además deberá mostrar un
# menú con las siguientes opciones

  #   Añadir contacto
  #  Lista de contactos
  #  Buscar contacto
  #  Editar contacto
  #  Cerrar agenda

class Agenda():
    
    def __init__(self):
        self.contactos = [{'Nombre':'pedro','Telefono':'7831427100','Email':'pepe@mavi.mx'}]
        
    def añadir(self):
        nombre = input('Ingresa el nombre: ')
        telefono = input('Ingresa el telefono: ')
        email = input('Ingresa el email: ')
        self.contactos.append({'Nombre':nombre,'Telefono':telefono,'Email':email})

    def listar(self):
        for i in self.contactos:
            for key, value in i.items():
                print(key,'-----',value)
    
    def buscar(self,nombre):
        for i in range (len(self.contactos)):
            if nombre == self.contactos[i]['Nombre']:
                print(self.contactos[i]['Nombre'])
                print(self.contactos[i]['Telefono'])
                print(self.contactos[i]['Email'],'\n')
        

    def editar(self):
        opcion = int(input("¿Que deseas editar?:\n 1.-Nombre\n2-.Telefono\n3.-Email\n "))
        
        if opcion == 1:
            nombre = input('¿Que nombre deseas editar?')
            for i in range (len(self.contactos)):
                if nombre == self.contactos[i]['Nombre']:    
                    reemplazo = input('¿Por cual nombre deseas reemplazarlo?')
                    self.contactos[i]['Nombre'] = reemplazo  
           
        if opcion == 2:
            telefono = input('¿Que telefono deseas editar?')
            for i in range (len(self.contactos)):
                if telefono == self.contactos[i]['Telefono']:    
                    reemplazo = input('¿Por cual telefono deseas reemplazarlo?')
                    self.contactos[i]['Telefono'] = reemplazo  
                    
        if opcion == 3:
            email = input('¿Que email deseas editar?')
            for i in range (len(self.contactos)):
                if email== self.contactos[i]['Email']:    
                    reemplazo = input('¿Por cual emaildeseas reemplazarlo?')
                    self.contactos[i]['Email'] = reemplazo  
            
    
    def menu(self):
		
        while True:
            print('Agenda Personal\n',
                '1. Añadir Contacto\n',
			    '2. Lista de contactos\n',
			    '3. Buscar contacto\n',
			    '4. Editar contacto\n',
			    '5. Cerrar agenda\n')

            opcion=int(input("Introduzca la opción deseada: "))
      
            if opcion==1:
                self.añadir()
       
            elif opcion==2:
                self.listar()
    
            elif opcion==3:
                nombre = input('Buscar: ')
                self.buscar(nombre)
       
            elif opcion==4:
                self.editar()
       
            elif opcion==5:
                exit()
 
Imprimir = Agenda()
Imprimir.menu()
	   
 
  

       

    
