import pygame
from ClassImagen2 import Imagen


BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

ANCHO = 800
ALTO = 600

VELOCIDAD = 10

FPS = 30

pygame.init()

pygame.display.set_caption("Mi juego")

icono = pygame.image.load("CLASE 14\icono_homero.png")
pygame.display.set_icon(icono)

fondo = pygame.image.load("CLASE 14\\fondo_casa.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))


#creamos 2 superficies, una se mueve en vertical y otra en horizontal
#un rectangulo se mueve horizontalmente y otro verticalmente

#IMAGEN VERTICAL
imagen_vertical = Imagen((ANCHO//2, ALTO//2),(80,80),"CLASE 14\dona.png")

#IMAGEN HORIZONTAL
imagen_horizontal = Imagen((ANCHO-100,ALTO//2),(100,150),"CLASE 14\homero.png")

PANTALLA = pygame.display.set_mode((800,600))



pygame.mixer.music.load("CLASE 14\intro.mp3")
pygame.mixer.music.play(-1) #1 o vacio-> reproduce una sola vez /-1 lo repite en bucle
pygame.mixer.music.set_volume(0.5)#seteamos el volumen

#clock para establecer los fps
clock = pygame.time.Clock()

bandera = True

while bandera:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False

    PANTALLA.blit(fondo,(0,0))
    #tengo que blitear la superficie y el rectángulo
    PANTALLA.blit(imagen_vertical.superficie,imagen_vertical.rectangulo)
    PANTALLA.blit(imagen_horizontal.superficie,imagen_horizontal.rectangulo)
    #modifico posicion y
    
    #CADA VEZ QUE CHOQUEN LOS RECTANGULOS QUIERO QUE CAMBIEN DE COLOR
    #hay un metodo que verifica si dos superficies o rectangulos chocaron
    
    #imagen_vertical.detectar_colision(imagen_horizontal)

    #ahora mario puede pisar a la tortuga

    #MOVE
    imagen_vertical.mover("Vertical",VELOCIDAD,PANTALLA)

    imagen_horizontal.mover("Horizontal",VELOCIDAD,PANTALLA)


    #ahora vamos a crear 2 ejes, haciendo 2 líneas
    # pygame.draw.line(PANTALLA,AZUL,(ANCHO//2,0),(ANCHO//2,ANCHO),2)

    # pygame.draw.line(PANTALLA,AZUL,(0,ALTO//2),(ANCHO,ALTO//2),2)

    ####PARECE QUE YA VIERON EVENTOS, YO NO LO VI






    pygame.display.update() #o flip(), es lo mismo

pygame.quit()



