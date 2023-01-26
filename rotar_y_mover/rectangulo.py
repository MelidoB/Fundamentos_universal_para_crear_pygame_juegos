from pygame import image


class Rectangulo:
    def __init__(self, posicion):
        self.posicion = posicion
        self.imagenes = []
        self.imagen_usandose = 0
        self.direccion_despues_de_rotacion = 0
        self.CONTANTE_DE_ROTACION = 20
        self.tiempo_de_rotacion = 100
        self.velocidad = 5


    def obtener_velocidad(self):
        return self.velocidad

    def obtener_posicion(self):
        return self.posicion
    def asignar_posicion(self, nueva_posicion):
        self.posicion = nueva_posicion

    def obtener_imagen_usada(self):
        return self.imagenes[self.imagen_usandose]
    def asignar_imagen(self, nuevas_imagenes):
        sostener_nuevas_imagenes = []
        for imagen in nuevas_imagenes:
            sostener_nuevas_imagenes.append(image.load(f'{imagen}'))

        self.imagenes = sostener_nuevas_imagenes

    def modificar_imagenes(self, nuevas_imagenes):
        sostener_nuevas_imagenes = []
        for imagen in nuevas_imagenes:
            sostener_nuevas_imagenes.append(imagen)

        self.imagenes = sostener_nuevas_imagenes