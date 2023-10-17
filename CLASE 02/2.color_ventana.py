import pygame, sys
from pygame.locals import *

BLANCO = (255,255,255) #brillo máximo(RED-GREEN-BLUE) (buscar en paleta de colores internet e ir combinando rojo verde y azul)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0) #ausencia de color

#inicializador
pygame.init() 

#crear una ventana, donde se ejecutará el juego
VENTANA = pygame.display.set_mode((500,500))#pixeles (500->width,largo 500->height,alto)
#ponerle color a la ventana
VENTANA.fill(AZUL)

#setear título
pygame.display.set_caption("Mi primer ventana en pygame")

flag = True
while flag == True:
    lista_eventos = pygame.event.get() #pregunto eventos disparados, clic con el mouse, clic en x de la ventana, etc
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: #hizo clic en la x de la ventana?
            sys.exit() #dejo de ejecutar el bucle
    pygame.display.update() #actualizamos la pantalla

pygame.quit() #cierro el módulo de pygame