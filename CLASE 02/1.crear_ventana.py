import pygame, sys

#inicializador
pygame.init() 

#crear una ventana, donde se ejecutará el juego
pygame.display.set_mode((500,500))#pixeles (500->width,largo 500->height,alto)

#setear título
pygame.display.set_caption("Mi primer ventana en pygame")

flag = True
while flag == True:
    lista_eventos = pygame.event.get() #pregunto eventos disparados, clic con el mouse, clic en x de la ventana, etc
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: #hizo clic en la x de la ventana?
            sys.exit() #dejo de ejecutar el bucle

pygame.quit() #cierro el módulo de pygame
