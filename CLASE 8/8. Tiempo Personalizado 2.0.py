import pygame
import sys
import random

pygame.init()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Eventos de Teclado")



clock = pygame.time.Clock()



player_color = (0,0,255)

tiempo_inicial = pygame.time.get_ticks()

print(tiempo_inicial)

BLANCO = (255,255,255)

CAMBIO_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CAMBIO_COLOR, 2000) 

bandera = True
background = (0,0,0)
while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        elif event.type == CAMBIO_COLOR:
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)

            background = (red,green,blue)


    screen.fill((0,0,0))
    
        



    clock.tick(60)

pygame.quit()
sys.exit()