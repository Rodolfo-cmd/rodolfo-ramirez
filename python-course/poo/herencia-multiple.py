class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print('llamando...')

    def ocupado(self):
        print('ocupado...')

class Camara:
    def __init__(self):
        pass
    
    def fotografia(self):
        print('capturando...')


class Reproduccion:
    def __init__(self):
        pass
    def reproduccionmusica(self):
        print('reproducion musica')
    

    def reproduccionvideo(sef):
        print('reproducciendo video')


class smartphone(Telefono,Camara,Reproduccion):
    def __del__(self):
        print('telefono apagado')


movil = smartphone()
print(movil.fotografia())