import pygame, sys
from pygame.locals import *

BLANCO = (255,255,255) #brillo máximo(RED-GREEN-BLUE) (buscar en paleta de colores internet e ir combinando rojo verde y azul)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0) #ausencia de color

lista_imagenes =[{"nombre":"serpiente", "edad":3,"imagen": "CLASE 04\serpiente.png"}, {"nombre":"control", "edad":11,"imagen": "CLASE 04\control.png"}, {"nombre":"compu", "edad":2,"imagen": "CLASE 04\compu.png"}]

pygame.init()


fuente = pygame.font.SysFont("Arial",30)

ventana = pygame.display.set_mode((1500,1000))
pygame.display.set_caption("Mi primer ventana")


imagen1 = pygame.image.load("CLASE 04\serpiente.png")
# imagen = pygame.transform.rotate(imagen, 240)
imagen1 = pygame.transform.scale(imagen1, (100,100))
# imagen = pygame.transform.flip(imagen,True,False)

imagen2 = pygame.image.load("CLASE 04\control.png")
imagen2 = pygame.transform.scale(imagen2, (100,100))

imagen3 = pygame.image.load("CLASE 04\compu.png")
imagen3 = pygame.transform.scale(imagen3, (100,100))


flag_run = True
ventana.fill(ROJO)
while flag_run:
    y = 50
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False

    # ventana.blit(imagen1, (50,50))
    # ventana.blit(imagen2, (50,160))
    # ventana.blit(imagen3, (50,270))  

    # for animal in lista_animales:
    #     texto = fuente.render(animal,False,ROJO,VERDE)
    #     ventana.blit(texto,(50,y)) 
    
    for datos in lista_imagenes:
        nombre = fuente.render(datos["nombre"],False,BLANCO,NEGRO)
        edad = fuente.render(str(datos["edad"]),False,BLANCO,NEGRO)
        #imagen = fuente.render(datos["imagen"]),False,BLANCO,NEGRO
        #imagen = pygame.image.load(image)
        ventana.blit(nombre, (50,y))
        ventana.blit(edad, (260,y))
        ventana.blit(imagen1, (370,50))
        ventana.blit(imagen2, (370,160))
        ventana.blit(imagen3, (370,270))
        y += 110

    pygame.display.update()
pygame.quit()