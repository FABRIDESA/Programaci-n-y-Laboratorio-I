import pygame
import sys

pygame.init()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Eventos de Teclado")

bandera = True

clock = pygame.time.Clock()

while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        # elif event.type == pygame.KEYDOWN: #identifica cualquier tecla del teclado
        #     print(f"Tecla presionada: {event.key}")
        elif event.type == pygame.KEYDOWN:
            nombre = pygame.key.name(event.key)
            print(f"Tecla liberada: {nombre}")
    clock.tick(15)

pygame.quit()
sys.exit()