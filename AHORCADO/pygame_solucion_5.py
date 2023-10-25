'''
Objetivo:
Hacer el juego en el loop principal (no salió, solo una parte la hice ahi),
conseguir que el puntaje negativo y vida negativa
se refleje en el juego superando el update constante (nop)
y que la vida coincida con la imagen del cuerpo en el ahorcado (sip).
En general muy bien, funcionar funciona y tiene una corrección
que no es notoria, bien oculta.
'''

from gdb_python import*
from datos import diccionario_de_temas
import pygame

#Inicializar
pygame.init()

#Medidas
ANCHO = 800
ALTO = 800

#Colores
BLANCO = (255,255,255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Ventana
VENTANA = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("AHORCADO")

#Texto
fuente = pygame.font.SysFont("Arial Black",20)
fuente_oculta = pygame.font.SysFont("Arial Black",55)
fuente_tiempo = pygame.font.SysFont("Arial Black",30)

#Tiempo
FPS = 30
clock = pygame.time.Clock()

#Carga imagen de fondo
fondo = pygame.image.load("AHORCADO\\fondos-png-1.jpg")  # Reemplaza con la ruta de tu imagen
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

#Carga de imágenes cuerpo
imagenes = []
for i in range(7):
    imagen = pygame.image.load("AHORCADO\\ahorcado" + str(i) + ".png")
    imagen = pygame.transform.scale(imagen, (450,450))
    imagenes.append(imagen)

#Carga de imágenes vidas
corazon_lleno = pygame.image.load("AHORCADO\corazon_lleno.png")
corazon_vacio = pygame.image.load("AHORCADO\corazon_vacio.png")
tamaño_corazon = (40,40)
corazon_lleno = pygame.transform.scale(corazon_lleno,tamaño_corazon)
corazon_vacio = pygame.transform.scale(corazon_vacio,tamaño_corazon)

#Seteo música
pygame.mixer.music.load("AHORCADO\TrackTribe - New Morning (Bright).mp3")
pygame.mixer.music.play(-1) #1 o vacio-> reproduce una sola vez /-1 lo repite en bucle
pygame.mixer.music.set_volume(0.5)#seteamos el volumen

#Temporizador
tiempo_inicial = pygame.time.get_ticks()
tiempo_limite = 20000 #60 segundos en milisegundos

#Funciones
# def actualizar_tiempo():
#     # tiempo_en_segundos + x = 60
#     x = 60 - tiempo_en_segundos
#     tiempo_limite = x + tiempo_en_segundos
#     return tiempo_limite

#Variables In Game
jugando = True    
flag_aleatorios_iniciales = True
flag_puntaje = True
flag_vidas = True
puntaje = 0
vidas = 6
teclas_presionadas = []
previa_palabra_oculta = ''
tema = ''
palabra = ''
palabra_oculta = ''

#Bucle Principal
while jugando:
    #Tiempo
    clock.tick(FPS)
    tiempo_actual = pygame.time.get_ticks()
    tiempo_en_segundos = (tiempo_limite - tiempo_actual)//1000

    #Verificar si se ha agotado el tiempo
    if tiempo_en_segundos == 0:    
        jugando = False
        
    #Eventos
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            jugando = False
        if event.type == pygame.KEYDOWN:
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                key_name = chr(event.key).upper()
                teclas_presionadas.append(key_name)
                if palabra != previa_palabra_oculta: 
                    previa_palabra_oculta = palabra_oculta      
                    palabra_oculta = reemplazar_letras(palabra,teclas_presionadas)      
                if palabra_oculta == previa_palabra_oculta:
                    vidas -= 1
                    puntaje -= 5
                    
                else:
                    puntaje += 10
                if vidas == 0:
                    jugando = False
                
                if palabra == previa_palabra_oculta:
                    flag_puntaje = True
                    puntaje += 100
                    flag_puntaje = False
                    flag_aleatorios_iniciales = True
                    teclas_presionadas.clear()
                    vidas += 1
                    puntaje += 5
                
    if flag_aleatorios_iniciales:
        tema = obtener_tema(diccionario_de_temas)
        palabra = obtener_palabra(diccionario_de_temas,tema)
        palabra_oculta = reemplazar_letras(palabra,teclas_presionadas)
        flag_aleatorios_iniciales = False

    #Ventana
    # VENTANA.fill(BLANCO)
    VENTANA.blit(fondo,(0,0))

    #Texto
    mensaje_puntaje= "Score: "
    mensaje_puntaje_superficie = fuente.render(mensaje_puntaje,True,NEGRO)
    VENTANA.blit(mensaje_puntaje_superficie,(350,0))
    puntaje_superficie = fuente.render(str(puntaje),True,NEGRO)
    VENTANA.blit(puntaje_superficie,(420,0))

    mensaje_categoria = "Temática: "
    mensaje_categoria_superficie = fuente.render(mensaje_categoria,True,NEGRO)
    VENTANA.blit(mensaje_categoria_superficie,(0,0))
    tema_superficie = fuente.render(tema,True,NEGRO)
    VENTANA.blit(tema_superficie,(110,0))

    # mensaje_vidas = "Vidas: "
    # mensaje_vidas_superficie = fuente.render(mensaje_vidas,True,NEGRO)
    # VENTANA.blit(mensaje_vidas_superficie,(700,0))
    # vidas_superficie = fuente.render(str(vidas),True,NEGRO)
    # VENTANA.blit(vidas_superficie,(770,0))

    mensaje_categoria = "Letras ya ingresadas: "
    mensaje_categoria_superficie = fuente.render(mensaje_categoria,True,NEGRO)
    VENTANA.blit(mensaje_categoria_superficie,(0,740))
    lista_letras_superficie = fuente.render(str(teclas_presionadas),True,NEGRO)
    VENTANA.blit(lista_letras_superficie,(235,740))

    palabra_oculta_superficie = fuente_oculta.render(palabra_oculta,True,NEGRO)
    VENTANA.blit(palabra_oculta_superficie,(160,550))

    tiempo_superficie = fuente_tiempo.render(str(tiempo_en_segundos),True,NEGRO)
    VENTANA.blit(tiempo_superficie,(700,700))
    #Dibujos
    VENTANA.blit(imagenes[vidas],(200,100))
    x_corazon = 530
    
    for i in range(vidas,6):  # Suponiendo que tienes 6 vidas máximas
        VENTANA.blit(corazon_vacio, (x_corazon, 0))
        x_corazon += tamaño_corazon[0] + 5
    for i in range(vidas):
        VENTANA.blit(corazon_lleno, (x_corazon, 0))
        x_corazon += tamaño_corazon[0] + 5
    #Actualizar
    pygame.display.update()

#Salir
pygame.quit()

