import pygame, sys
from pygame.locals import *

pygame.init()

PANTALLA = pygame.display.set_mode((500,400))
pygame.display.set_caption('Mi primer juego :D')

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)

PANTALLA.fill(AZUL)

rectangulo1 = pygame.draw.rect(PANTALLA,BLANCO,(100,50,100,50))
print(rectangulo1)

pygame.draw.line(PANTALLA, VERDE, (100,104), (199,104), 10) #100 x /199 final de linea /104 inclina linea a izq o der /10 grosor

pygame.draw.circle(PANTALLA, NEGRO, (122,250), 20, 0) #122 x/250 y/20 radio/0 relleno (10 quedaria una donut)

pygame.draw.ellipse(PANTALLA, ROJO, (275,200,40,80),10) #275 pos x/200 pos y/ 40 tamaño x/80 tamaño/10 grueso

puntos = [(100,300),(100,100),(150,100)]
pygame.draw.polygon(PANTALLA,(0,150,255), puntos, 8)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

