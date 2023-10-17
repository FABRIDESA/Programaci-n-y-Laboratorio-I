import pygame
import sys

pygame.init()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Eventos de Teclado")

bandera = True

clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 100) #genera un temporizador
mensaje = "Hola 1BD"
x,y = 100,100
font = pygame.font.SysFont("Arial",30)

player_color = (0,0,255)

tiempo_inicial = pygame.time.get_ticks()

print(tiempo_inicial)

BLANCO = (255,255,255)


while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        elif event.type == pygame.USEREVENT:
            x += 10

    screen.fill((0,0,0))
    texto = font.render(mensaje,True,BLANCO)
    screen.blit(texto,(x,y))
        



    clock.tick(60)

pygame.quit()
sys.exit()