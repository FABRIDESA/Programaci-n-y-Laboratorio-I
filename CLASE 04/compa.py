#Macarena Chanampa 1B
import pygame
from pygame.locals import *

NEGRO = (0,0,0)
BLANCO = (255,255,255)


pygame.init() 

VENTANA = pygame.display.set_mode((900,710)) 

fuente = pygame.font.SysFont("Arial",30)
imagen1 = pygame.image.load("CLASE 04\serpiente.png")
imagen1 = pygame.transform.scale(imagen1,(200,200))

imagen2 = pygame.image.load("CLASE 04\control.png")
imagen2 = pygame.transform.scale(imagen2,(200,200))

imagen3 = pygame.image.load("CLASE 04\compu.png")
imagen3 = pygame.transform.scale(imagen3,(200,200))


a1 = {"nombre":"Panchito","edad":2,"imagen":imagen1}
a2 = {"nombre":"Coco","edad":4,"imagen":imagen2}
a3 = {"nombre":"Lara","edad":6,"imagen":imagen3}
lista_animales = [a1,a2,a3]
pygame.display.set_caption("EJERCICIO IMAGENES PYGAME")

'''
for animal in lista_animales:
    nombre = animal["nombre"]
    edad = animal["edad"]
    edad = int(edad)
    imagen = animal["imagen"]
'''
VENTANA.fill(NEGRO)

y = 10
y2 = 95
flag = True
while flag == True:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False 

        for animal in lista_animales:
            nombre = animal["nombre"]
            edad = animal["edad"]
            imagen = animal["imagen"]
            NombreYEdad = (f"Nombre: {nombre:10} Edad: {edad}")
            VENTANA.blit(imagen,(10,y))
            texto = fuente.render(NombreYEdad,False,BLANCO)
            VENTANA.blit(texto,(300,y2))
 
            if y > 700:
                y = 0
                          
            if y2 > 700:
                y2 = 95

            y += 250
            y2 += 235



    pygame.display.update()
pygame.quit()