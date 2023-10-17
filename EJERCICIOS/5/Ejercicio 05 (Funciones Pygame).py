import math
import pygame, sys
from pygame.locals import *

'''
NOMBRE: FABRICIO
APELLIDO: DE SA TORRES
DIVISION: B
EJERCICIO: Ejercicio 05 (Funciones Pygame)
ESTADO: Ejercicio entregado
'''

'''
Deberán realizar un programa que permita mostrar por una ventana pygame el 
perímetro y el área (en pixeles) de una figura, la misma podrá ser un 
triángulo rectángulo, un círculo, un rectángulo o un cuadrado.

Especificaciones técnicas:

Diccionarios
Los datos de una figura deberán estar representados en un diccionario, en 
el mismo se especificará: tipo de figura geométrica, dimensiones, posición 
inicial y el color de la figura.

Funciones
Crear funciones para:
● Calcular perímetro y área (tener en cuenta que las fórmulas son distintas 
para cada figura)
● Dibujar la figura en la ventana
● Escribir los resultados en pantalla.
● Gestionar el cálculo de área, perímetro y gráfica de la figura. 
Se sugiere que la misma reciba como mínimo una superficie que representa 
la ventana y un diccionario que represente la figura.
Todas las funciones deberán estar organizadas en módulos según su 
responsabilidad.
Recuerden los objetivos del trabajo con funciones.
'''

#Paleta de Colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
AMARILLO = (255,255,0)

#Inicialización de Pygame
pygame.init()

#Creación de Ventana
PANTALLA = pygame.display.set_mode((500,400))

#Rellenado de Ventana
PANTALLA.fill(BLANCO)

#Agregado de Título
pygame.display.set_caption("FIGURAS")

#########LISTA#########
lista_figuras = [
    {                                   
        "tipo":"circulo",               
        "dimensiones": 70,              
        "posicion inicial": (250,160),
        "color": VERDE
    },
    {                                   #posicion -> lista_figuras[0] ingresa a primer diccionario
        "tipo":"rectangulo",
        "dimensiones": (100,50),        #entrar por key -> lista_figuras[0]["dimensiones"] #entrar al largo -> lista_figuras[0]["dimensiones"][0]
        "posicion inicial": (200,150),
        "color": VERDE
    },
    {
        "tipo":"cuadrado",
        "dimensiones": (100,100),
        "posicion inicial": (200,150),
        "color": VERDE   
    },
    {
        "tipo":"triangulo",
        "dimensiones": [(300,250),(300,60)],
        "posicion inicial": [(150,250)],
        "color": VERDE
    }
]

#########FUNCIONES#########
def dibujar_figura_geometrica(tipo_de_figura:str):
    for datos in lista_figuras:
        if datos["tipo"] == "rectangulo":
            if tipo_de_figura == "rectangulo":
                pygame.draw.rect(PANTALLA,datos["color"],datos["posicion inicial"]+datos["dimensiones"])
        elif datos["tipo"] == "cuadrado":
            if tipo_de_figura == "cuadrado":
                pygame.draw.rect(PANTALLA,datos["color"],datos["posicion inicial"]+datos["dimensiones"])
        elif datos["tipo"] == "circulo":
            if tipo_de_figura == "circulo":
                pygame.draw.circle(PANTALLA,datos["color"],datos["posicion inicial"],datos["dimensiones"])
        elif datos["tipo"] == "triangulo":
            if tipo_de_figura == "triangulo":
                pygame.draw.polygon(PANTALLA,datos["color"],datos["posicion inicial"]+datos["dimensiones"])

def mensajes_en_pantalla(figura_geometrica:str):
    dibujar_figura_geometrica(figura_geometrica)
    if figura_geometrica == "rectangulo":
        PANTALLA.blit(texto_area_rectangulo,(100,300))
        PANTALLA.blit(texto_perimetro_rectangulo,(80,350))
    elif figura_geometrica == "cuadrado":
        PANTALLA.blit(texto_area_cuadrado,(100,300))
        PANTALLA.blit(texto_perimetro_cuadrado,(80,350))
    elif figura_geometrica == "circulo":
        PANTALLA.blit(texto_area_circulo,(100,300))
        PANTALLA.blit(texto_perimetro_circulo,(80,350))
    elif figura_geometrica == "triangulo":
        PANTALLA.blit(texto_area_triangulo,(100,300))
        PANTALLA.blit(texto_perimetro_triangulo,(80,350))

#########FUNCIONES-ÁREAS#########
def calculo_area_figura_geometrica(lista:list,tipo_de_figura:str):
    if tipo_de_figura == "rectangulo":
        largo = lista[1]["dimensiones"][0]
        alto = lista[1]["dimensiones"][1]
        area = largo * alto
        return round(area,2)
    elif tipo_de_figura == "cuadrado":
        largo = lista[2]["dimensiones"][0]
        alto = lista[2]["dimensiones"][1]
        area = largo * alto
        return round(area,2)
    elif tipo_de_figura == "circulo":
        radio = float(lista[0]["dimensiones"])
        pi = math.pi
        area = pi * radio ** 2
        return round(area,2)
    elif tipo_de_figura =="triangulo":
        base = calculo_base_triangulo_rectangulo(lista)
        altura = calculo_altura_triangulo_rectangulo(lista)
        area = (base * altura)/2
        return round(area,2)

#########FUNCIONES-PERÍMETROS#########
def calculo_perimetro_figura_geometrica(lista:list,tipo_de_figura:str):
    if tipo_de_figura == "rectangulo":
        largo = lista[1]["dimensiones"][0]
        alto = lista[1]["dimensiones"][1]
        perimetro = (largo + alto) * 2
        return round(perimetro,2)
    elif tipo_de_figura == "cuadrado":
        largo = lista[2]["dimensiones"][0]
        alto = lista[2]["dimensiones"][1]
        perimetro = (largo + alto) * 2
        return round(perimetro,2)
    elif tipo_de_figura == "circulo":
        #perimetro = pi x diametro
        diametro = float(lista[0]["dimensiones"]) * 2
        pi = math.pi
        perimetro = pi * diametro
        return round(perimetro,2)
    elif tipo_de_figura =="triangulo":
        cateto1 = calculo_base_triangulo_rectangulo(lista)
        cateto2 = calculo_altura_triangulo_rectangulo(lista)
        hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
        perimetro = cateto1 + cateto2 + hipotenusa
        return round(perimetro,2)

def calculo_base_triangulo_rectangulo(lista:list):
    triangulo_base_x2 = lista[3]["dimensiones"][0][0]
    triangulo_base_x1 = lista[3]["posicion inicial"][0][0]
    base = triangulo_base_x2 - triangulo_base_x1
    return base

def calculo_altura_triangulo_rectangulo(lista:list):
    triangulo_altura_y1 = lista[3]["posicion inicial"][0][1]
    triangulo_altura_y3 = lista[3]["dimensiones"][1][1]
    altura = triangulo_altura_y1 - triangulo_altura_y3
    return altura

#########LLAMADAS#########
area_del_rectangulo = calculo_area_figura_geometrica(lista_figuras,"rectangulo")
perimetro_del_rectangulo = calculo_perimetro_figura_geometrica(lista_figuras,"rectangulo")

area_del_cuadrado = calculo_area_figura_geometrica(lista_figuras,"cuadrado")
perimetro_del_cuadrado = calculo_perimetro_figura_geometrica(lista_figuras,"cuadrado")

area_del_circulo = calculo_area_figura_geometrica(lista_figuras,"circulo")
perimetro_del_circulo = calculo_perimetro_figura_geometrica(lista_figuras,"circulo")

area_del_triangulo = calculo_area_figura_geometrica(lista_figuras,"triangulo")
perimetro_del_triangulo = calculo_perimetro_figura_geometrica(lista_figuras,"triangulo")

#########TEXTO#########
fuente = pygame.font.SysFont("Arial",30)

texto_area_rectangulo = fuente.render(f"Area del Rectangulo: {str(area_del_rectangulo)}",False,ROJO,VERDE)
texto_perimetro_rectangulo = fuente.render(f"Perimetro del Rectangulo: {str(perimetro_del_rectangulo)}",False,ROJO,VERDE)

texto_area_cuadrado = fuente.render(f"Area del Cuadrado: {str(area_del_cuadrado)}",False,ROJO,VERDE)
texto_perimetro_cuadrado = fuente.render(f"Perimetro del Cuadrado: {str(perimetro_del_cuadrado)}",False,ROJO,VERDE)

texto_area_circulo = fuente.render(f"Area del Circulo: {str(area_del_circulo)}",False,ROJO,VERDE)
texto_perimetro_circulo = fuente.render(f"Perimetro del Circulo: {str(perimetro_del_circulo)}",False,ROJO,VERDE)

texto_area_triangulo = fuente.render(f"Area del Triangulo: {str(area_del_triangulo)}",False,ROJO,VERDE)
texto_perimetro_triangulo = fuente.render(f"Perimetro del Triangulo: {str(perimetro_del_triangulo)}",False,ROJO,VERDE)

#Seteo de la Imagen de Fondo
background = pygame.image.load("EJERCICIOS\constelacion.jpg").convert()
background = pygame.transform.scale(background, (500,400))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    PANTALLA.blit(background, [0,0])

    mensajes_en_pantalla("triangulo")
        
    pygame.display.update()