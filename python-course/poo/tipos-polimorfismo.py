#polimorfismo de funcion

#class Tomate:
 #   def tipo(self):
  #      print('vegetal')
    
   # def color(self):
    #    print('rojo')

#class Manzana:
 #   def tipo(self):
  #      print('fruta')
    
   # def color(self):
    #    print('verde')

#def funcion(objeto):
 #   objeto.tipo()
  #  objeto.color()

#nuevo_tomate = Tomate()
#funcion(nuevo_tomate)

#nueva_manzana = Manzana()
#funcion(nueva_manzana)

#Polimorfismo con metodo

# class Colombia:
#     def capital(self):
#         print('bogota')

#     def idioma(self):
#         print('español')

# class Francia:
#     def capital(self):
#         print('paris')

#     def idioma(self):
#         print('frances')

# colombiano = Colombia()
# frances = Francia()
# for pais in (colombiano,frances):
#     pais.capital()
#     pais.idioma()

#polimorfismo con herecia



class Aves:
    def volar(self):
        print('las mayorias de las aves vuelan otras no ')


class Aguila(Aves):
    def volar(self):
        print('las anguilas son expertas voladora')

class Gallina(Aves):
    def volar(self):
        print('pero las gallinas no pueden volar')

obj_ave = Aves()
obj_aguila = Aguila()
obj_gallina = Gallina()
obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()