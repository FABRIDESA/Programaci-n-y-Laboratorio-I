import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configura la ventana
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Juego del Ahorcado en Pygame")

# Definir la palabra a adivinar
palabra_a_adivinar = "PYTHON"
letras_adivinadas = []

# Definir la posición de la palabra en la ventana
font = pygame.font.Font(None, 36)
text_x = 20
text_y = 20

# Variables para el juego
intentos = 6
adivinadas_correctas = 0

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                letra = chr(event.key).upper()
                if letra not in letras_adivinadas:
                    letras_adivinadas.append(letra)
                    if letra in palabra_a_adivinar:
                        adivinadas_correctas += 1

    # Limpiar la pantalla
    screen.fill((255, 255, 255))

    # Mostrar la palabra a adivinar
    palabra_mostrada = ''
    for letra in palabra_a_adivinar:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += '_ '
    text_surface = font.render(palabra_mostrada, True, (0, 0, 0))
    screen.blit(text_surface, (text_x, text_y))

    # Mostrar las letras adivinadas
    letras_adivinadas_str = ', '.join(letras_adivinadas)
    letras_surface = font.render(f"Letras adivinadas: {letras_adivinadas_str}", True, (0, 0, 0))
    screen.blit(letras_surface, (text_x, text_y + 50))

    # Mostrar los intentos restantes
    intentos_restantes = intentos - (adivinadas_correctas - len(set(letras_adivinadas) - set(palabra_a_adivinar)))
    intentos_surface = font.render(f"Intentos restantes: {intentos_restantes}", True, (0, 0, 0))
    screen.blit(intentos_surface, (text_x, text_y + 100))

    # Actualizar la pantalla
    pygame.display.update()

    # Verificar si el jugador ha ganado o perdido
    if adivinadas_correctas == len(set(palabra_a_adivinar)):
        print("¡Ganaste!")
        pygame.quit()
        sys.exit()
    if intentos_restantes == 0:
        print(f"Perdiste. La palabra era '{palabra_a_adivinar}'.")
        pygame.quit()
        sys.exit()