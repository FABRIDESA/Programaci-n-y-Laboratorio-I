import pygame, sys
from pygame.locals import *

lista_imagenes = []
imagen1 = pygame.image.load("CLASE 04\serpiente.png")
# imagen = pygame.transform.rotate(imagen, 240)
imagen1 = pygame.transform.scale(imagen1, (100,100))
# imagen = pygame.transform.flip(imagen,True,False)
lista_imagenes.append(imagen1)

imagen2 = pygame.image.load("CLASE 04\control.png")
imagen2 = pygame.transform.scale(imagen2, (100,100))
lista_imagenes.append(imagen2)

imagen3 = pygame.image.load("CLASE 04\compu.png")
imagen3 = pygame.transform.scale(imagen3, (100,100))
lista_imagenes.append(imagen3)

print(lista_imagenes)