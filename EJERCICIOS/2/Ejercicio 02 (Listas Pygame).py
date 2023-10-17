import pygame
from pygame.locals import *

'''
NOMBRE: FABRICIO
APELLIDO: DE SA TORRES
DIVISIÓN: B
EJERCICIO: Ejercicio 02-Listas pygame
ESTADO: Ejercicio entregado
'''

'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo
desarrollo en python,
que promete revolucionar el mercado.
Las posibles aplicaciones son las siguientes:
    # Inteligencia artificial (IA),
    # Realidad virtual/aumentada (RV/RA),
    # Internet de las cosas (IOT) o
    # Procesamiento de lenguaje natural (NLP).


Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:


A) Los datos a ingresar por cada empleado encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT, NLP)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
    1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y
    50 años inclusive.
    2) - Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea
    Femenino o su edad se encuentre entre los 33 y 40.
    3) - Nombre y tecnología que votó, de los empleados de género masculino con mayor edad.
    de ese género.
'''


lista_nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta",
                    "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]


lista_edades = [25, 30, 45, 38, 42, 25, 49, 32, 19, 49,
                    32, 22, 29, 27, 19, 49, 27, 22, 49, 27]

lista_generos = ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
                        "Otro", "Femenino", "Masculino", "Otro", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
                        "Femenino", "Masculino", "Otro"]

lista_tecnologias = ["IOT", "RV/RA", "NLP", "IA", "NLP", "IOT", "RV/RA", "IOT", "IA", "NLP",
                    "RV/RA", "RV/RA", "NLP", "RV/RA", "IA", "IOT", "NLP", "IOT", "IA", "IA"]  


for i in range(len(lista_nombres)):
    nombre = lista_nombres[i]
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]
    print(f"{nombre:15}{edad:}\t{genero:15}\t{tecnologia}")

contador = 0

#1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y
#50 años inclusive.
for i in range(len(lista_tecnologias)):
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]

    if genero == "Masculino":
        if tecnologia == "IOT" or tecnologia == "IA":
            if edad >= 25 and edad <=50:
                contador += 1
    elif genero == "Femenino":
        pass
print(f"Cantidad de empleados que cumplen el criterio: {contador}")

#2) - Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea
#Femenino o su edad se encuentre entre los 33 y 40.

contador_ia = 0
for i in range(len(lista_tecnologias)):
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]

    if tecnologia != "IA" and (genero != "Femenino" or (edad >= 33 and edad <= 40)):
        contador_ia += 1

porcentaje = (contador_ia * 100) / len(lista_nombres)
print(f"El porcentaje de empleados que cumplen con el criterio es: {porcentaje:0.2f}%")

#3) - Nombre y tecnología que votó, de los empleados de género masculino con mayor edad.
#de ese género.

bandera = True
maximo_edad = 0

for i in range(len(lista_tecnologias)):
    edad = lista_edades[i]
    genero = lista_generos[i]
    if genero == "Masculino":
        if bandera == True or edad > maximo_edad:
            maximo_edad = edad
            bandera = False

for i in range(len(lista_nombres)):
        nombre = lista_nombres[i]
        edad = lista_edades[i]
        genero = lista_generos[i]
        tecnologia = lista_tecnologias[i]
        if genero == "Masculino" and edad== maximo_edad:
            print(f"-> {nombre:15}{tecnologia:15}{edad} años")

#PYGAME
BLANCO = (255,255,255) #brillo máximo(RED-GREEN-BLUE) (buscar en paleta de colores internet e ir combinando rojo verde y azul)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0) #ausencia de color

#inicializador
pygame.init() 

#crear una ventana, donde se ejecutará el juego
ventana = pygame.display.set_mode((900,500))#pixeles (500->width,largo 500->height,alto)
#setear título
pygame.display.set_caption("Integrador-Informes-Pygame")
icono = pygame.image.load('CLASE 02\imagen.png') #cargamos una imagen, la convertimos en una superficie y la cargamos en la variable ícono
pygame.display.set_icon(icono)
#ponerle color a la ventana
ventana.fill(NEGRO)

#CREAMOS UNA FUENTE
fuente = pygame.font.SysFont("Arial",15)
#hacemos superficie al texto
texto = fuente.render("Hola estudiantes de 1BD",False,ROJO,VERDE)
#hacer blit en la ventana (poner una superficie sobre la ventana)

flag = True
while flag == True:
    y = 20
    lista_eventos = pygame.event.get() #pregunto eventos disparados, clic con el mouse, clic en x de la ventana, etc
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: #hizo clic en la x de la ventana?
            flag = False

    for i in range(len(lista_generos)):
        nombre = lista_nombres[i]
        edad = lista_edades [i]
        genero = lista_generos[i]
        tecnologia = lista_tecnologias[i]
        
        titulo_nombre = fuente.render("Nombres",False,BLANCO,AZUL)
        ventana.blit(titulo_nombre,(5,5))
        texto_nombre = fuente.render(nombre,False,BLANCO,AZUL)
        ventana.blit(texto_nombre,(5,y))

        titulo_edad = fuente.render("Edades",False,BLANCO,AZUL)
        ventana.blit(titulo_edad,(105,5))
        texto_edad = fuente.render(str(edad),False,BLANCO,AZUL)
        ventana.blit(texto_edad,(105,y))
        
        titulo_genero = fuente.render("Generos",False,BLANCO,AZUL)
        ventana.blit(titulo_genero,(205,5))
        texto_genero = fuente.render(genero,False,BLANCO,AZUL)
        ventana.blit(texto_genero,(205,y))
        
        titulo_tecnologia = fuente.render("Tecnologias",False,BLANCO,AZUL)
        ventana.blit(titulo_tecnologia,(305,5))
        texto_tecnologia = fuente.render(tecnologia,False,BLANCO,AZUL)
        ventana.blit(texto_tecnologia,(305,y))

        consigna_1_parte_1 = fuente.render("Cantidad empleados género masculino que votaron por IOT o IA,",False,BLANCO,AZUL)
        ventana.blit(consigna_1_parte_1,(5,330))
        consigna_1_parte_2 = fuente.render("cuya edad este entre 25 y 50 años inclusive:",False,BLANCO,AZUL)
        ventana.blit(consigna_1_parte_2,(5,345))
        texto_contador = fuente.render(str(contador),False,BLANCO,AZUL)
        ventana.blit(texto_contador,(305,345))

        consigna_2_parte_1 = fuente.render("Porcentaje de empleados que no votaron por IA, siempre y cuando",False,BLANCO,AZUL)
        ventana.blit(consigna_2_parte_1,(5,375))
        consigna_2_parte_2 = fuente.render("su género no sea Femenino o su edad se encuentre entre los 33 y 40:",False,BLANCO,AZUL)
        ventana.blit(consigna_2_parte_2,(5,390))
        texto_porcentaje = fuente.render(str(porcentaje)+"%",False,BLANCO,AZUL)
        ventana.blit(texto_porcentaje,(155,405))

        y += 15
    
    y = 455
    for i in range(len(lista_nombres)):
        nombre = lista_nombres[i]
        edad = lista_edades[i]
        genero = lista_generos[i]
        tecnologia = lista_tecnologias[i]
        if genero == "Masculino" and edad== maximo_edad:
            consigna_3 = fuente.render("Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género:",False,BLANCO,AZUL)
            ventana.blit(consigna_3,(5,425))
            maximo_nombre = nombre
            maxima_tecnologia = tecnologia
            maxima_edad = edad
            texto_maximo_nombre = fuente.render("-> " + maximo_nombre,False,BLANCO,AZUL)
            ventana.blit(texto_maximo_nombre,(5,y))
            texto_maxima_tecnologia = fuente.render(maxima_tecnologia,False,BLANCO,AZUL)
            ventana.blit(texto_maxima_tecnologia,(105,y))
            texto_maxima_edad = fuente.render(str(maxima_edad) + " años",False,BLANCO,AZUL)
            ventana.blit(texto_maxima_edad,(205,y))

            y +=15

    pygame.display.update() #actualizamos la pantalla

pygame.quit() #cierro el módulo de pygame




