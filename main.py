import pygame
from time import sleep

# game
programIcon = pygame.image.load('assets/marisa.png')
pygame.display.set_icon(programIcon)
FPS = 60

WIDTH, HEIGHT = 900, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# player
red_square = pygame.image.load('assets/marisa.png')
red_square = pygame.transform.scale(red_square, (40, 60))
PLAYER = pygame.Rect(250, 700, 45, 60)
velocity = 10

# background
BACKGROUND = pygame.image.load('assets/bg.png')
BORDER = pygame.Rect(20, 20, 500, 760)

MENUIMG = pygame.image.load('assets/menubg.png')
MENUTXT = pygame.image.load('assets/menutxt.png')

def menu_screen():
    WIN.blit(MENUIMG, (0, 0))
    WIN.blit(MENUTXT, (0, 0))

def display_game():
    pygame.draw.rect(WIN, (0, 0, 0), BORDER)

    WIN.blit(red_square, (PLAYER.x, PLAYER.y))

    WIN.blit(BACKGROUND, (0, 0))

def game_keybind(velocity):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LSHIFT]:
        velocity = velocity - 4

    #vertical
    if keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_RIGHT]:
        velocity = velocity - 2
    elif keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_LEFT]:
        velocity = velocity - 2
    elif keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_DOWN]:
        velocity = velocity - 2
    elif keys_pressed[pygame.K_DOWN] and keys_pressed[pygame.K_RIGHT]:
        velocity = velocity - 2

    # left right up down
    if keys_pressed[pygame.K_UP] and PLAYER.y > BORDER.y + 5: #up
        PLAYER.y -= velocity
    if keys_pressed[pygame.K_LEFT] and PLAYER.x > BORDER.x + 5: #left
        PLAYER.x -= velocity
    if keys_pressed[pygame.K_DOWN] and PLAYER.y < BORDER.y + BORDER.height - 45: #down
        PLAYER.y += velocity
    if keys_pressed[pygame.K_RIGHT] and PLAYER.x < BORDER.x + BORDER.width - 45: #right
        PLAYER.x += velocity

def main():
    game_screen = 0

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # game screen = 0 is in main()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            game_screen = 1
        if game_screen > 0:
            display_game()
            game_keybind(velocity)
        else:
            menu_screen()

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()