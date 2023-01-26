from pygame import key

def aumentar_velocidad_mientras_se_presiona_una_tecla(objeto, tecla):
    tecla_presionada = key.get_pressed()

    running = tecla_presionada[ord(tecla)]
    
    if running:
        if objeto.velocidad_actual<objeto.velocidad_max:
            objeto.velocidad_actual+=objeto.constante_de_cambio_de_velocidad
        else:
            objeto.velocidad_actual = objeto.velocidad_max
    else:
        if objeto.velocidad_actual > objeto.velocidad_min:
            objeto.velocidad_actual-=objeto.constante_de_cambio_de_velocidad
        else:
            objeto.velocidad_actual = objeto.velocidad_min
    print(objeto.velocidad_actual)