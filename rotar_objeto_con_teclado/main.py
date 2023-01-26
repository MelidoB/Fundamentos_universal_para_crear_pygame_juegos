import pygame

from rectangulo import Rectangulo
from close_game import close_game_function
from rotar_objeto_con_teclado import rotar_objeto_con_teclado


def main():


    todo_para_dibujar = {} #guardare todo lo que se valla ah dibujar en un set llamado todo_para_dibujar. Lo mismo que una lista
                              #pero no puedo acceder el index.

    rectangulo = Rectangulo((20,20))
    rectangulo.asignar_imagen(["rectangulo.png"])
    todo_para_dibujar["rectangulo"] = rectangulo


    ############################################################
    pygame.init()
    gameDisplay = pygame.display.set_mode((1400, 800))
    clock = pygame.time.Clock()

    while True:
        # Pongo funcion para poder cerrar la applicacion
        close_game_function()
        gameDisplay.fill((255, 255, 255))  # Dibujare la blanco en toda la pantalla

        for i, j in todo_para_dibujar.items():
            x, y = j.obtener_posicion()
            imagen = j.obtener_imagen_usada()
            gameDisplay.blit(imagen, (x, y))

        clock.tick(60)
        pygame.display.update()

        ###############################################################################

        rectangulo_cambiado = todo_para_dibujar["rectangulo"]
        rotar_objeto_con_teclado(rectangulo_cambiado)

if __name__ == '__main__':
    main()