from pygame import image


class Circle:
    def __init__(self, posicion):
        self.posicion = posicion
        self.imagenes = []
        

    def obtener_posicion(self):
        return self.posicion
    def asignar_posicion(self, nueva_posicion):
        self.posicion = nueva_posicion

    def obtener_imagen(self):
        return self.imagen
    def asignar_imagen(self, nueva_imagen):
        self.imagen = image.load(f'{nueva_imagen}')