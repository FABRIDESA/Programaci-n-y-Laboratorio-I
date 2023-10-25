from ahorcado import *
from datos import diccionario_de_temas
import pygame
import sys

#seteo (configuración) de pantalla
pygame.init()
WIDTH = 800 #ANCHO
HEIGHT = 500 #ALTO
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT)) #VENTANA
pygame.display.set_caption("AHORCADO") #título ventana

#paleta de colores
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#carga de imágenes
imagenes = []
for i in range(7):
    imagen = pygame.image.load("AHORCADO\\ahorcado" + str(i) + ".png")
    imagenes.append(imagen)

# variables in game
ahorcado_estado = 0

# seteo de texto
fuente = pygame.font.SysFont("Arial",40)

def mostrar_texto(palabra:str,x:int,y:int):
    texto = fuente.render(palabra,False,BLACK)
    WINDOW.blit(texto,(x,y))

#seteo loop del juego
palabra_adivinada = True
puntaje = 0
vidas = 6
jugando = True
lista_letras = []
while jugando:

    WINDOW.fill(WHITE)
    WINDOW.blit(imagenes[ahorcado_estado],(300,100))
    pygame.display.update()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            nombre_de_letra = pygame.key.name(evento.key)      
            letra_ingresada = validar_letras(lista_letras,nombre_de_letra)
            if letra_ingresada:
                lista_letras.append(nombre_de_letra)
                letra_ingresada = False

    # if palabra_adivinada == True:
    #     tema = obtener_tema(diccionario_de_temas)
    #     palabra = obtener_palabra(diccionario_de_temas,tema)
    #     lista_letras = []
    #     palabra_oculta = reemplazar_letras(palabra,lista_letras)
    #     mensaje = (f"La categoria es:{tema} \n {palabra_oculta}")
    #     print(mensaje)
    #     mostrar_texto(mensaje,350,50)
    #     mensaje = (f"Tu puntaje es: {puntaje}")
    #     print(mensaje)
    #     mostrar_texto(mensaje,450,50)
    #     palabra_adivinada = False


    # if palabra != palabra_oculta:
    #     previa_palabra_oculta = palabra_oculta
        
    #     palabra_oculta = reemplazar_letras(palabra,lista_letras)
    #     if palabra_oculta == previa_palabra_oculta:
    #         vidas -= 1
    #         puntaje -= 5
    #         mensaje = (f"Te quedan {vidas} vidas")
    #         #print(mensaje)
    #         mostrar_texto(mensaje,550,50)

    #     else:
    #         puntaje += 10

    #     if vidas == 0:
    #         jugando = False
    #         break
        
    #     mensaje = (f"{palabra_oculta}")
    #     print(mensaje)
    #     mostrar_texto(mensaje,650,50)
    # else:
    #     palabra_adivinada = True
    #     puntaje += 100

    # mensaje = f"Tu puntaje final es: {puntaje}"
    # print(mensaje)
    # mostrar_texto(mensaje,150,50)
    # mensaje = ("Juego finalizado")
    # print(mensaje)
    # mostrar_texto(mensaje,250,50)

    # mostrar_texto("ahorcado",50,50)

pygame.quit()