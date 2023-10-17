import pygame
import sys

pygame.init()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Eventos de Teclado")

bandera = True

clock = pygame.time.Clock()

tiempo_inicial = pygame.time.get_ticks()

print(tiempo_inicial)

custom_event = pygame.USEREVENT


while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pygame.event.post(pygame.event.Event(custom_event))

        elif event.type == custom_event:
            print("Presiono la tecla derecha mediante un evento personalizado")



    clock.tick(60)

pygame.quit()
sys.exit()