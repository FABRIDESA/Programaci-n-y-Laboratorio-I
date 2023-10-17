import pygame

# setup display
pygame.init()
WIDTH, HEIGHT = 800,500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i)])

#fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 30)

#load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw ():
    win.fill((WHITE))

    #draw buttons
    for letter in letters:
        x, y, ltr = letter
        pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
        text = LETTER_FONT.render(ltr, 1, BLACK)
        win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status],(150,100))
    pygame.display.update()


while run:
    clock.tick(FPS) #para q vayamos a esta velocidad del reloj

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #sirve para salir con la cruz de la ventanita
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN: #sirve para identificar donde hacemos clic con el mouse en pantalla
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()