"""  
Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista
de la compra y el coste total, con el siguiente formato

Lista de la compra	
"""
r=0
compra={}

while True:
    agregar = input("\n¿Desea agregar un articulo?   s(si) n(no): " )
    
    if agregar == 's':
       articulo = input("\nAgregar articulo: ")
       precio = float(input("Precio del articulo: "))
       compra[articulo] = precio
       
       for i in compra.values():
           r+=i          
    else:
        break

print("\n~~~~~~~~Lista de articulos:~~~~~~~~~")

for articulo,precio in compra.items():
    print(articulo,precio)  
    
print("El total de su compra es de: ",r)
        

    
    