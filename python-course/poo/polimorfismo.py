class Animales:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def tipo_animal(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        print('animal salvaje')

class Perro(Animales):
    def tipo_animal(self):
        print('animal domestico')

nuevo_animal = Perro('scartface')
nuevo_animal.tipo_animal()

nuevo_animal2 = Leon('baraka')
nuevo_animal2.tipo_animal()