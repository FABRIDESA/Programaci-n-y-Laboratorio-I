import pygame, sys
from pygame.locals import *

#inicializador
pygame.init() 

BLANCO = (255,255,255) #brillo máximo(RED-GREEN-BLUE) (buscar en paleta de colores internet e ir combinando rojo verde y azul)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0) #ausencia de color

#crear una ventana, donde se ejecutará el juego
ventana = pygame.display.set_mode((900,500))#pixeles (500->width,largo 500->height,alto)
#setear título
pygame.display.set_caption("Mi primer ventana en pygame")
icono = pygame.image.load('CLASE 02\imagen.png') #cargamos una imagen, la convertimos en una superficie y la cargamos en la variable ícono
pygame.display.set_icon(icono)
#ponerle color a la ventana
ventana.fill(CELESTE)

#CREAMOS UNA FUENTE
fuente = pygame.font.SysFont("Arial",30)
#hacemos superficie al texto
texto = fuente.render("Hola estudiantes de 1BD",False,ROJO,VERDE)
#hacer blit en la ventana (poner una superficie sobre la ventana)



flag = True
while flag == True:
    lista_eventos = pygame.event.get() #pregunto eventos disparados, clic con el mouse, clic en x de la ventana, etc
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: #hizo clic en la x de la ventana?
            flag = False
            #sys.exit() #dejo de ejecutar el bucle
    ventana.blit(texto,(50,50))
    pygame.display.update() #actualizamos la pantalla

pygame.quit() #cierro el módulo de pygame