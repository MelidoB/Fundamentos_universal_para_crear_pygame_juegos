from pygame import image


class Circle:
    def __init__(self, posicion):
        self.posicion = posicion
        self.imagen = None

        self.direccion_despues_de_rotacion = 0
        #To Increase speed
        self.velocidad_min = 5
        self.velocidad_max = self.velocidad_min + 10
        self.velocidad = self.velocidad_min
        self.constante_de_cambio_de_velocidad = 0.2
        #
    def obtener_posicion(self):
        return self.posicion
    def asignar_posicion(self, nueva_posicion):
        self.posicion = nueva_posicion

    def obtener_velocidad(self):
        return self.velocidad
    def obtener_imagen(self):
        return self.imagen
    def asignar_imagen(self, nueva_imagen):
        self.imagen = image.load(f'{nueva_imagen}')