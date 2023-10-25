from ahorcado import *
from datos import diccionario_de_temas
import pygame
import sys

#Inicializar
pygame.init()

#Medidas
ANCHO = 800
ALTO = 500

#Colores
BLANCO = (255,255,255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Ventana
ventana = pygame.display.set_mode((ANCHO,ALTO)) #VENTANA
pygame.display.set_caption("AHORCADO") #título ventana
fuente = pygame.font.SysFont("segoe print",30)
texto = fuente.render("CUADRADOS",True,NEGRO)

#carga de imágenes
imagenes = []
for i in range(7):
    imagen = pygame.image.load("AHORCADO\\ahorcado" + str(i) + ".png")
    imagenes.append(imagen)

# variables in game
ahorcado_estado = 0

# # seteo de texto
# fuente = pygame.font.SysFont("Arial",40)

# def mostrar_texto(palabra:str,x:int,y:int):
#     texto = fuente.render(palabra,False,NEGRO)
#     ventana.blit(texto,(x,y))

# #seteo loop del juego
# palabra_adivinada = True
# puntaje = 0
# vidas = 6
# jugando = True
# lista_letras = []

#Bucle principal

jugando = True
tecla = ""

while jugando:

    # Eventos
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            jugando = False
        # if event.type == pygame.KEYDOWN:
        #     tecla += event.unicode     
        #CÓMO FUNCIONA KEYDOWN
        if event.type == pygame.KEYDOWN:
            nombre_de_letra = pygame.key.name(event.key)
            print(nombre_de_letra) 
            superficie_nombre_de_letra = fuente.render(nombre_de_letra,False,NEGRO)
            ventana.blit(superficie_nombre_de_letra,(300,300))
    # Lógica
    ventana.fill(BLANCO)
    texto_superficie = fuente.render(tecla,True,NEGRO)
    ventana.blit(texto_superficie,(200,200))
    
    # Dibujos
    
    
    ventana.blit(texto,(100,100))

    ventana.blit(imagenes[ahorcado_estado],(300,100))

    # Actualizar
    pygame.display.update()

# Salir
pygame.quit()



#     pygame.display.update()   
#             # letra_ingresada = validar_letras(lista_letras,nombre_de_letra)
#             # if letra_ingresada:
#             #     lista_letras.append(nombre_de_letra)
#             #     letra_ingresada = False
        
#     # if palabra_adivinada == True:
#     #     tema = obtener_tema(diccionario_de_temas)
#     #     palabra = obtener_palabra(diccionario_de_temas,tema)
#     #     lista_letras = []
#     #     palabra_oculta = reemplazar_letras(palabra,lista_letras)
#     #     mensaje = (f"La categoria es:{tema} \n {palabra_oculta}")
#     #     print(mensaje)
#     #     mostrar_texto(mensaje,350,50)
#     #     mensaje = (f"Tu puntaje es: {puntaje}")
#     #     print(mensaje)
#     #     mostrar_texto(mensaje,450,50)
#     #     palabra_adivinada = False


#     # if palabra != palabra_oculta:
#     #     previa_palabra_oculta = palabra_oculta
        
#     #     palabra_oculta = reemplazar_letras(palabra,lista_letras)
#     #     if palabra_oculta == previa_palabra_oculta:
#     #         vidas -= 1
#     #         puntaje -= 5
#     #         mensaje = (f"Te quedan {vidas} vidas")
#     #         #print(mensaje)
#     #         mostrar_texto(mensaje,550,50)

#     #     else:
#     #         puntaje += 10

#     #     if vidas == 0:
#     #         jugando = False
#     #         break
        
#     #     mensaje = (f"{palabra_oculta}")
#     #     print(mensaje)
#     #     mostrar_texto(mensaje,650,50)
#     # else:
#     #     palabra_adivinada = True
#     #     puntaje += 100

#     # mensaje = f"Tu puntaje final es: {puntaje}"
#     # print(mensaje)
#     # mostrar_texto(mensaje,150,50)
#     # mensaje = ("Juego finalizado")
#     # print(mensaje)
#     # mostrar_texto(mensaje,250,50)

#     # mostrar_texto("ahorcado",50,50)

# pygame.quit()