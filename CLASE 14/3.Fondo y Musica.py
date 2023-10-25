import pygame,sys

SIZE = (1000,500)


pygame.init()

PANTALLA = pygame.display.set_mode(SIZE)

pygame.display.set_caption("Mi juego")

icono = pygame.image.load("CLASE 14\icono_homero.png")
pygame.display.set_icon(icono)

fondo = pygame.image.load("CLASE 14\\fondo_casa.jpg")
fondo = pygame.transform.scale(fondo, SIZE)

PANTALLA.blit(fondo,(0,0))

#PONER LA MÚSICA DE LA INTRO DE LOS SIMPSON
#usamos el modulo mixer, que tiene de clase music

pygame.mixer.music.load("CLASE 14\intro.mp3")
pygame.mixer.music.play(-1) #1 o vacio-> reproduce una sola vez /-1 lo repite en bucle
pygame.mixer.music.set_volume(0.5)#seteamos el volumen

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()