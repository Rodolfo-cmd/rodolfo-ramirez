# class Empleado:
#     def __init__(self,nombre,salario):
#         self.__nombre = nombre
#         self.__salario = salario
#     #Creacion
#     def getnombre(self):
#         return self.__nombre
    
#     def getsalario(self):
#         return self.__salario
#     #Metodo editar o modificar
#     def setnombre(self,nombre):
#         self.__nombre = nombre
        
#     def setsalario(self,salario):
#         self.__salario = salario

#     #Metodo borrar
#     def delnombre(self):
#         self.__nombre

#     def delsalario(self):
#         self.__salario
    
# empleado_uno = Empleado('rotherd',4000)
# print(empleado_uno.getnombre(),',',empleado_uno.getsalario())
# empleado_uno.setnombre('rodolfo')
# print(empleado_uno.getnombre(),',',empleado_uno.getsalario())



#Ejemplo de propiedades:

class Empleado:
    def __init__(self,nombre,salario):
        self.__nombre = nombre
        self.__salario = salario
    
    def __getnombre(self):
        return self.__nombre
    
    def __getsalario(self):
        return self.__salario
    
    def __setnombre(self,nombre):
        self.__nombre = nombre
        
    def __setsalario(self,salario):
        self.__salario = salario

    
    def __delnombre(self):
        self.__nombre

    def __delsalario(self):
        self.__salario


    nombre = property(fget=__getnombre,
                  fset=__setnombre,
                  fdel=__delnombre,
                  doc= "soy la propiedad del nombre")
    
    salario = property(fget=__getsalario)


empleado_uno = Empleado('rotherd',4000)
empleado_uno.nombre = 'rodolfo'
print(empleado_uno.nombre,empleado_uno.salario)
                       

