# class Matematica:
#     def suma (self):
#         self.n1 = 10
#         self.n2 = 10

# s = Matematica()
# s.suma()

# print(s.n1 + s.n2)

#Metodo __init__ (self)

# class Ropa:
#     def __init__(self):
#         self.marca = 'prada'
#         self.talla = 'L'
#         self.color = 'azul'

# poloche = Ropa()
# print(poloche.marca)
# print(poloche.talla)

class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicacion = n1 * 2
        self.divicion = n1 / n2

operacion = Calculadora(2,5)
print(operacion.suma)
    