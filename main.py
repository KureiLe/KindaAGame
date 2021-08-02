import pygame

# game
WIDTH, HEIGHT = 900, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
programIcon = pygame.image.load('assets/red.png')
pygame.display.set_icon(programIcon)
pygame.display.set_caption("ClayZe~")
FPS = 60

# rectangle in the left
BORDER_L = pygame.Rect(20, 20, 500, 760)

# player
SQUARE_RED = pygame.image.load('assets/red.png')
SQUARE_RED = pygame.transform.scale(SQUARE_RED, (40, 40))
velocity = 8
                 #location  size
red = pygame.Rect(250, 700, 45, 45)

#background
BACKGROUND = pygame.image.load('assets/bg.png')

def draw_window(red):
    # layers from top to bottom (layer 1, 2, 3, ...)
    WIN.fill((255, 255, 255))

    #                      color
    pygame.draw.rect(WIN, (0, 0, 0), BORDER_L)

    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(SQUARE_RED, (red.x, red.y))
    
def keybinds(red, velocity):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LSHIFT]:
        velocity = velocity - 3

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
    if keys_pressed[pygame.K_UP] and red.y > BORDER_L.y + 5: #up
        red.y -= velocity
    if keys_pressed[pygame.K_LEFT] and red.x > BORDER_L.x + 5: #left
        red.x -= velocity
    if keys_pressed[pygame.K_DOWN] and red.y < BORDER_L.y + BORDER_L.height - 45: #down
        red.y += velocity
    if keys_pressed[pygame.K_RIGHT] and red.x < BORDER_L.x + BORDER_L.width - 45: #right
        red.x += velocity


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keybinds(red, velocity)
        draw_window(red)

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
