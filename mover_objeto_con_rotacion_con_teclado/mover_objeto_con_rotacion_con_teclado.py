from pygame import key

def mover_objeto_con_rotacion_con_teclado(objeto):
    tecla_presionada = key.get_pressed()

    arriba = tecla_presionada[ord('w')]
    abajo = tecla_presionada[ord('s')]


    velocidad = objeto.obtener_velocidad()


    #derecha,arriba,izquierda,abajo
    direccion_con_velocidad = [[1,0],[0,-1],[-1,0],[0,1]]
    if arriba:
        for idj ,j in enumerate(direccion_con_velocidad):
            if objeto.direccion_despues_de_rotacion == idj:
                x, y = objeto.obtener_posicion()
                objeto.asignar_posicion((x + j[0] *velocidad, y + j[1] *velocidad))