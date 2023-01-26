import pygame

from circle import Circle
from close_game import close_game_function
from aumentar_velocidad_mientras_se_presiona_una_tecla import aumentar_velocidad_mientras_se_presiona_una_tecla


def main():


    todo_para_dibujar = {} #guardare todo lo que se valla ah dibujar en un set llamado todo_para_dibujar. Lo mismo que una lista
                              #pero no puedo acceder el index.

    circle = Circle((20,20))
    circle.asignar_imagen("circle.png")
    todo_para_dibujar["circle"] = circle


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
            imagen = j.obtener_imagen()
            gameDisplay.blit(imagen, (x, y))

        clock.tick(60)
        pygame.display.update()

        ###############################################################################

        circle_cambiado = todo_para_dibujar["circle"]
        aumentar_velocidad_mientras_se_presiona_una_tecla(circle_cambiado, tecla = "j")

if __name__ == '__main__':
    main()