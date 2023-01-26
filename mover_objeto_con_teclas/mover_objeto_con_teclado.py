from pygame import key

def mover_objeto_con_teclado(objeto):
    tecla_presionada = key.get_pressed()
    izquierda = tecla_presionada[ord('a')]
    derecha = tecla_presionada[ord('d')]
    arriba = tecla_presionada[ord('w')]
    abajo = tecla_presionada[ord('s')]


    velocidad = objeto.obtener_velocidad()

    condiciones_de_movimiento = [izquierda, derecha, arriba, abajo]
    direccion_con_velocidad = [[-1,0],[1,0],[0,-1],[0,1]]

    for condicion,j in zip(condiciones_de_movimiento, direccion_con_velocidad):
        if condicion:
            x, y = objeto.obtener_posicion()
            objeto.asignar_posicion((x + j[0] *velocidad, y + j[1] *velocidad))
