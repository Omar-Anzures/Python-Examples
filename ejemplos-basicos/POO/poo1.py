import math
class Punto():
    x=0
    y=0
   
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
      
    def __str__(self):
        return (f"coordenadas ({self.x})({self.y})")
    
    def cuadrante(self):
        
       if (self.x > 0 and self.y > 0):
            print ("Primer cuadrante")
 
       elif (self.x < 0 and self.y > 0):
            print ("Segundo cuadrante")
         
       elif (self.x < 0 and self.y < 0):
            print ("Tercer cuadrante")
     
       elif (self.x > 0 and self.y < 0):
            print ("Cuarto cuadrante")
         
       elif self.x == 0 or self.y == 0:
            print("Esta sobre su origen")
            
    def vector(self,vec1,vec2):
       x3 = (vec1)-(self.x)
       y3 = (vec2)-(self.y)
       print(f"El resultado del vector es de ({x3},{y3}) ")
     
    def distancia(self,vec1,vec2):
        distancia = (pow(vec1-self.x,2) + pow(vec2-self.y,2))**2
        return print(distancia)


vect= Punto(2,3)
vect.vector(5,5)

cua = Punto(4,4)
cua.cuadrante()

dist = Punto(2,2)
dist.distancia(5,5)