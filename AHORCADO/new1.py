import pygame,sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,800])
base_font = pygame.font.Font(None,32)
user_text = ''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            user_text += event.unicode 

    screen.fill((0,0,0))
    text_surface = base_font.render(user_text,True,(255,255,255))
    screen.blit(text_surface,(0,0))

    pygame.display.flip()
    clock.tick(60)