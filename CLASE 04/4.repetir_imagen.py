import pygame, sys
from pygame.locals import *

BLANCO = (255,255,255) #brillo máximo(RED-GREEN-BLUE) (buscar en paleta de colores internet e ir combinando rojo verde y azul)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0) #ausencia de color

pygame.init()

ventana = pygame.display.set_mode((1500,1000))
pygame.display.set_caption("Mi primer ventana")

imagen = pygame.image.load("CLASE 04\serpiente.png")
# imagen = pygame.transform.rotate(imagen, 240)
imagen = pygame.transform.scale(imagen, (100,100))
# imagen = pygame.transform.flip(imagen,True,False)

# otra_imagen = pygame.image.load("CLASE 04\control.png")
# otra_imagen = pygame.transform.scale(otra_imagen, (200,200))

flag_run = True
ventana.fill(ROJO)
x=50
while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False

    ventana.blit(imagen, (x,50))
    # ventana.blit(otra_imagen, (200,200))
    x+=110
    if x > 1400:
        x = 50

    pygame.display.update()
pygame.quit()