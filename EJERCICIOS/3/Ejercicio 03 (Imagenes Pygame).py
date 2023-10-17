import pygame, sys
from pygame.locals import *

'''
NOMBRE: FABRICIO
APELLIDO: DE SA TORRES
DIVISIÓN: B
EJERCICIO: Ejercicio 03 (Imagenes Pygame)
ESTADO: Ejercicio entregado
'''

BLANCO = (255,255,255) 
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0) 

pygame.init()

ventana = pygame.display.set_mode((1500,1000))

pygame.display.set_caption("Ejercicio 3 - Imágenes Pygame")

fuente = pygame.font.SysFont("Arial",30)

imagen1 = pygame.image.load("CLASE 04\serpiente.png")
imagen1 = pygame.transform.scale(imagen1, (100,100))

imagen2 = pygame.image.load("CLASE 04\control.png")
imagen2 = pygame.transform.scale(imagen2, (100,100))


imagen3 = pygame.image.load("CLASE 04\compu.png")
imagen3 = pygame.transform.scale(imagen3, (100,100))

a1 = {"nombre":"serpiente","edad":3,"imagen":imagen1}
a2 = {"nombre":"control","edad":11,"imagen":imagen2}
a3 = {"nombre":"compu","edad":2,"imagen":imagen3}
lista_imagenes = [a1,a2,a3]

ventana.fill(ROJO)

flag_run = True
y = 50
while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
    
    for datos in lista_imagenes:
        nombre = datos["nombre"]
        edad = str(datos["edad"])
        imagen = datos["imagen"]

        ventana.blit(imagen,(50,y))

        texto_nombre = fuente.render(nombre,False,BLANCO,NEGRO)
        ventana.blit(texto_nombre,(160,y))

        texto_edad = fuente.render(edad,False,BLANCO,NEGRO)
        ventana.blit(texto_edad,(270,y))

        y += 110

        if y > 270:
            y = 50
    
    

    pygame.display.update()
pygame.quit()