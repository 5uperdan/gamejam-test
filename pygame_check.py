import pygame
import os

def __main__():
    check_pygame()
    
def check_pygame():
    pygame.init()
    pygame.mouse.set_visible(0)
    clock = pygame.time.Clock()

    screen_resolution = (
        pygame.display.Info().current_w,
        pygame.display.Info().current_h,
    )

    screen = pygame.display.set_mode((800, 600))
    running = True
    daruma = pygame.image.load('./resources/Daruma.png')

    x, y = (0, 0)

    # main game loop
    while running and x < 100 and y < 100:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        x += 1
        y += 1

        screen.blit(daruma, (x, y))

        # updates game screen
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
    return True

__main__()