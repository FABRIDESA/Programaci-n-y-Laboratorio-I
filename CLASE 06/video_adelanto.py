#FIGURAS GEOMÉTRICAS

import pygame, sys
from pygame.locals import *

pygame.init()

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
FONDO = (0,140,60)
AMARILLO = (255,255,0)

PANTALLA = pygame.display.set_mode((500,400))
pygame.display.set_caption("FIGURAS")

PANTALLA.fill(BLANCO)

pygame.draw.line(PANTALLA, FONDO, (100,200 ), (400,200), 5)
pygame.draw.line(PANTALLA, FONDO, (250,10), (250,390), 5)
pygame.draw.line(PANTALLA, NEGRO, (100,200), (250,10), 5)
pygame.draw.line(PANTALLA, NEGRO, (250,10), (400,200), 5)
pygame.draw.line(PANTALLA, NEGRO, (100,200), (250,390), 5)
pygame.draw.line(PANTALLA, NEGRO, (250,390), (400,200), 5)

pygame.draw.rect(PANTALLA,AMARILLO,(0,0,100,400),49)
pygame.draw.rect(PANTALLA,AMARILLO,(400,0,100,400),49)
pygame.draw.rect(PANTALLA,AMARILLO,(100,0,300,10),4)
pygame.draw.rect(PANTALLA,AMARILLO,(100,390,300,10),4)

pygame.draw.circle(PANTALLA,AZUL,(250,200),30,5)

pygame.draw.ellipse(PANTALLA,VERDE,(100,190,100,20),5)
pygame.draw.ellipse(PANTALLA,VERDE,(300,190,100,20),5)
pygame.draw.ellipse(PANTALLA,VERDE,(240,10,20,100),5)
pygame.draw.ellipse(PANTALLA,VERDE,(240,290,20,100),5)

puntos = [(100,200),(250,200),(250,10)]
puntos2 = [(250,200),(400,200),(250,10)]
puntos3 = [(100,200),(250,200),(250,390)]
puntos4 = [(250,200),(250,390),(400,200)]
pygame.draw.polygon(PANTALLA,VERDE,puntos,1)
pygame.draw.polygon(PANTALLA,VERDE,puntos2,1)
pygame.draw.polygon(PANTALLA,VERDE,puntos3,1)
pygame.draw.polygon(PANTALLA,VERDE,puntos4,1)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
