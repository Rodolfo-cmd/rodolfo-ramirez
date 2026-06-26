class Mamifero:
    def __init__(self,nombre):
        print(nombre,'es un animal de sangre caliente')

class Leon(Mamifero):
    def __init__(self,):
        print('el leon es un animal carnivoro')
        super().__init__('simba')


nuevo_leon = Leon()
        