#nombre = 'victor'
#edad = 30
#print(f"mi nombre es {nombre} y mi edad es {edad}")




class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    

    def __str__(self):
        return f"hola soy  {self.nombre} {self.apellido} y mi edad es {self.edad}"

    
nuevo_estudiante = Estudiante('rotherd','ramirez',30)
print(f"{nuevo_estudiante}")