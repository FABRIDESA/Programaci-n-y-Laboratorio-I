import pygame


BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

ANCHO = 800
ALTO = 600

FPS = 30

pygame.init()

#creamos 2 superficies, una se mueve en vertical y otra en horizontal
#un rectangulo se mueve horizontalmente y otro verticalmente

#IMAGEN VERTICAL
imagen_vertical = pygame.Surface((100,100))
imagen_vertical.fill(VERDE)
rectangulo_vertical = imagen_vertical.get_rect()
#pygame clase/Surface metodo constructor/imagen_vertical objeto/get_rect() método
#ahora quiero que este rectángulo esté en el centro, a través de una propiedad del rectángulo vamos a setear ese centro
rectangulo_vertical.center = (ANCHO//2, ALTO//2)

#IMAGEN HORIZONTAL
imagen_horizontal = pygame.Surface((100,100))
imagen_horizontal.fill(AZUL_CLARO)
rectangulo_horizontal = imagen_horizontal.get_rect()
rectangulo_horizontal.center = (ANCHO-100,ALTO//2)

PANTALLA = pygame.display.set_mode((800,600))

#clock para establecer los fps
clock = pygame.time.Clock()

bandera = True

while bandera:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False

    PANTALLA.fill(NEGRO)

    #tengo que blitear la superficie y el rectángulo
    PANTALLA.blit(imagen_vertical,rectangulo_vertical)
    #modifico posicion y
    rectangulo_vertical.y += 10
    if rectangulo_vertical.top > ALTO:
        rectangulo_vertical.bottom = 0
    #CADA VEZ QUE CHOQUEN LOS RECTANGULOS QUIERO QUE CAMBIEN DE COLOR
    #hay un metodo que verifica si dos superficies o rectangulos chocaron
    if rectangulo_vertical.colliderect(rectangulo_horizontal):
        imagen_horizontal.fill(ROJO)
        imagen_vertical.fill(BLANCO)
    else:
        imagen_horizontal.fill(AZUL_CLARO)
        imagen_vertical.fill(VERDE)
    #ahora mario puede pisar a la tortuga

    PANTALLA.blit(imagen_horizontal,rectangulo_horizontal)
    rectangulo_horizontal.x += 10
    if rectangulo_horizontal.left > ANCHO:
        rectangulo_horizontal.right = 0



    #ahora vamos a crear 2 ejes, haciendo 2 líneas
    pygame.draw.line(PANTALLA,AZUL,(ANCHO//2,0),(ANCHO//2,ANCHO),2)

    pygame.draw.line(PANTALLA,AZUL,(0,ALTO//2),(ANCHO,ALTO//2),2)

    ####PARECE QUE YA VIERON EVENTOS, YO NO LO VI






    pygame.display.update() #o flip(), es lo mismo

pygame.quit()



