
#metodo class

#class Pastel:
  #  def __init__(self,ingredientes):
        #self.ingredientes = ingredientes
    
    #def __repr__(self):
     #   return f' ingredientes para un pastel({self.ingredientes !r})'
        
    #@classmethod
    #def pastel_chocolate(cls):
        #return cls(['harina','polvo de hornear','leche','chocolate'])
    
    #@classmethod
    #def pastel_vainilla(cls):
        #return cls(['harina','polvo de horno','leche','vainilla'])
    
#print(Pastel.pastel_vainilla())




#Metodo estactico


import math
class Pastel:
    def __init__(self,ingredientes,tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño
    
    def __repr__(self):
        return (f'Pastel({self.ingredientes}, 'f'{self.tamaño})')
    

    def area(self):
        return self.tamaño_area(self.tamaño)
    @staticmethod
    def tamaño_area(A):
        return A ** 2 * math.pi


nuevo_pastel = Pastel(['harina','leche','vainilla'],4)
print(nuevo_pastel.tamaño_area(12))



    