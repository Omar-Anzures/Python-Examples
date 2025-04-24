class Producto:

    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    #para decirle que es un get, tenemos que ponerle el property, forma de hacer getter y setter
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, valor):
        self.__precio = valor

    def calcular_total(self, unidades):
        return self.__precio * unidades
        
    def __str__(self):
        return 'Codigo: ' + str(self.__codigo) + ', nombre: ' +  self.__nombre + ', precio: ' + str(self.__precio)
    

class Pedido:

    def __init__(self):
        self.__productos =  []
        self.__cantidades = []

    def aniadir_producto(self, producto, cantidad):

        if not isinstance(producto, Producto):
            raise Exception("Añadir producto: producto debe ser de la clase producto")
        
        if not isinstance(cantidad, int):
            raise Exception("Añadir cantidad: Cantidad debe ser un numero")
        
        if cantidad <= 0:
            raise Exception('Añadir producto: cantidad debe ser mayor que 0')
        
        if producto in self.__productos:
            indice = self.__productos.index(producto)
            self.__cantidades[indice] = self.__cantidades[indice] + cantidad
        else:
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)
    

    def eliminar_producto(self,producto):

        if not isinstance(producto, Producto):
            raise Exception("Eliminar producto: producto debe ser de la clase producto")
        
        if producto in self.__productos:
            indice = self.__productos.index(producto)
            del self.__productos[indice]
            del self.__cantidades[indice]

        else:
            raise Exception('No existe producto ')
        

    def total_pedidos(self):
        total = 0
        
        for p,c in zip(self.__productos, self.__cantidades):
            total = total + p.calcular_total(c)
        return total

    def mostrar_pedido(self):
        for p,c in zip(self.__productos, self.__cantidades):
            print("Producto > ", p ," , Cantidad > " + str(c))


p1 = Producto(1, "Producto 1", 5)
p2 = Producto(2, "Producto 2", 10)
p3 = Producto(3, "Producto 3", 20)

print(p1.calcular_total(5))
print(p2.calcular_total(5))
print(p3.calcular_total(5))
 
pedido = Pedido()

try:
    pedido.aniadir_producto(p1,5)
    pedido.aniadir_producto(p2,5)
    pedido.aniadir_producto(p3,5)

    print("Total pedido: " + str(pedido.total_pedidos()) + "\n")

    pedido.mostrar_pedido()

    pedido.eliminar_producto(p1)

    print("Total pedido: " + str(pedido.total_pedidos()) + "\n")

    pedido.mostrar_pedido()

except Exception as e:
    print (e)

