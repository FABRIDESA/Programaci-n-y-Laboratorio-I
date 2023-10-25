'''
Casi todo está bliteado en pantalla
Se reconoce la lista y modifica la palabra oculta
Lo que no reconoce son las letras ingresadas en la lista desde eventos
'''

from gdb_python import*
from datos import diccionario_de_temas
import pygame

#Inicializar
pygame.init()

#Medidas
ANCHO = 800
ALTO = 800

#Colores
BLANCO = (255,255,255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Ventana
VENTANA = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("AHORCADO")
fuente = pygame.font.SysFont("Arial",20)
fuente_oculta = pygame.font.SysFont("Arial",70)

#Tiempo
FPS = 30
clock = pygame.time.Clock()

#carga de imágenes
imagenes = []
for i in range(7):
    imagen = pygame.image.load("AHORCADO\\ahorcado" + str(i) + ".png")
    imagen = pygame.transform.scale(imagen, (450,450))
    imagenes.append(imagen)

def mostrar_texto(palabra:str,x:int,y:int):

    texto = fuente.render(palabra,False,NEGRO)
    VENTANA.blit(texto,(x,y))

#Variables In Game
jugando = True    
palabra_adivinada = True
ahorcado_estado = 0
puntaje = 0
vidas = 6
nombre_letra = ''
teclas_presionadas = ["A","E","I","O","U"]

#Bucle Principal
while jugando:
    #Tiempo
    clock.tick(FPS)
    #Eventos
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            jugando = False
        elif event.type == pygame.KEYDOWN:
            key_name = (pygame.key.name(event.key)).upper()
            teclas_presionadas.append(key_name)
            
            
    #Lógica

    if palabra_adivinada == True:
        tema = obtener_tema(diccionario_de_temas)
        palabra = obtener_palabra(diccionario_de_temas,tema)
        palabra_oculta = reemplazar_letras(palabra,teclas_presionadas)
        palabra_adivinada = False

        
    
    # if palabra != previa_palabra_oculta: 
    #     previa_palabra_oculta = palabra_oculta      
        # palabra_oculta = reemplazar_letras(palabra,lista_letras)
    #         if palabra_oculta == previa_palabra_oculta:
    #             vidas -= 1
    #             puntaje -= 5
    #             mensaje = (f"Te quedan {vidas} vidas")
    #         else:
    #             puntaje += 10
    #         if vidas == 0:
    #             jugando = False
    #             break

    #Ventana
    VENTANA.fill(BLANCO)

    #Texto

    mensaje_puntaje= "Score: "
    mensaje_puntaje_superficie = fuente.render(mensaje_puntaje,True,NEGRO)
    VENTANA.blit(mensaje_puntaje_superficie,(300,0))
    puntaje_superficie = fuente.render(str(puntaje),True,NEGRO)
    VENTANA.blit(puntaje_superficie,(360,0))

    mensaje_categoria = "Temática: "
    mensaje_categoria_superficie = fuente.render(mensaje_categoria,True,NEGRO)
    VENTANA.blit(mensaje_categoria_superficie,(0,0))
    tema_superficie = fuente.render(tema,True,NEGRO)
    VENTANA.blit(tema_superficie,(80,0))

    mensaje_tema = "La palabra es: "
    mensaje_tema_superficie = fuente.render(mensaje_tema,True,NEGRO)
    VENTANA.blit(mensaje_tema_superficie,(500,0))
    palabra_superficie = fuente.render(palabra,True,NEGRO)
    VENTANA.blit(palabra_superficie,(620,0))

    mensaje_categoria = "La lista de letras es: "
    mensaje_categoria_superficie = fuente.render(mensaje_categoria,True,NEGRO)
    VENTANA.blit(mensaje_categoria_superficie,(0,740))
    lista_letras_superficie = fuente.render(str(teclas_presionadas),True,NEGRO)
    VENTANA.blit(lista_letras_superficie,(150,740))

    palabra_oculta_superficie = fuente_oculta.render(palabra_oculta,True,NEGRO)
    VENTANA.blit(palabra_oculta_superficie,(225,550))

    #Dibujos
    VENTANA.blit(imagenes[ahorcado_estado],(200,100))

    #Actualizar
    pygame.display.update()

#Salir
pygame.quit()

