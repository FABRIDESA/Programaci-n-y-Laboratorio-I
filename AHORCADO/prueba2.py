import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configura la ventana
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Ejemplo de Agregar Teclas a una Lista en Pygame")

# Inicializa una lista para almacenar las teclas presionadas
teclas_presionadas = []

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            teclas_presionadas.append(key_name)  # Agrega la tecla a la lista
            print(f"Tecla presionada: {key_name}")
            print("Teclas en la lista:", teclas_presionadas)

    # Resto del bucle del juego

# Esto se ejecuta cuando sales del bucle principal
pygame.quit()