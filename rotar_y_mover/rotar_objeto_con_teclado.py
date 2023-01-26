from pygame import key, transform,image
def rotar_objeto_con_teclado(objeto):
    tecla_presionada = key.get_pressed()
    izquierda = tecla_presionada[ord('a')]
    derecha = tecla_presionada[ord('d')]



    condiciones_de_rotacion = [izquierda, derecha]
    direccion_de_rotacion = [1,-1]

    sostener_imagenes_rotadas = []
    for condicion, direccion in zip(condiciones_de_rotacion,direccion_de_rotacion) :

        if objeto.tiempo_de_rotacion > objeto.CONTANTE_DE_ROTACION:
            if condicion:
                for imagen in objeto.imagenes:
                    nueva_imagen = transform.rotate(imagen, direccion * 90)
                    sostener_imagenes_rotadas.append(nueva_imagen)
                objeto.modificar_imagenes(sostener_imagenes_rotadas)
                objeto.tiempo_de_rotacion = 0


                nuevo_valor_para_direccion = direccion + objeto.direccion_despues_de_rotacion
                if nuevo_valor_para_direccion > 3:
                    objeto.direccion_despues_de_rotacion = 0
                elif nuevo_valor_para_direccion < 0:
                    objeto.direccion_despues_de_rotacion = 3
                else:
                    objeto.direccion_despues_de_rotacion = nuevo_valor_para_direccion
                print(objeto.direccion_despues_de_rotacion)

        else:
            objeto.tiempo_de_rotacion += 1

