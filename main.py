import pygame

WIDTH, HEIGHT = 900, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("ClayZe~")
FPS = 60
velocity = 8

BORDER_L = pygame.Rect(20, 20, 500, 760)


SQUARE_RED = pygame.image.load('assets/red.png')
SQUARE_RED = pygame.transform.scale(SQUARE_RED, (40, 40))

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
    # if location is greater than 0??
    if keys_pressed[pygame.K_UP] and red.y > BORDER_L.y + 10: #up
        red.y -= velocity
    if keys_pressed[pygame.K_LEFT] and red.x > BORDER_L.x + 10: #left
        red.x -= velocity
    if keys_pressed[pygame.K_DOWN] and red.y < BORDER_L.y + BORDER_L.height - 45: #down
        red.y += velocity
    if keys_pressed[pygame.K_RIGHT] and red.x < BORDER_L.x + BORDER_L.width - 50: #right
        red.x += velocity
        


def main():
    #                size and position
    red = pygame.Rect(45, 45, 200, 600)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(red)
        keybinds(red, velocity)
        pygame.display.update()

    pygame.quit()

# if the name of function is main then execute main
if __name__ == "__main__":
    main()