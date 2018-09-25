import pygame
import random

RESOLUTION = 800, 800

STARTING_SIZE = 13
SIZE_LIMIT = 200
SIZE_STEP = 3
MOVEMENT_SPEED = 7


def get_random_char(size, color):
    char = chr(random.randint(33, 127))
    return pygame.font.Font(pygame.font.get_default_font(), size).render(char, False, color)


def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def play():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    buffer = pygame.Surface(RESOLUTION)

    size = STARTING_SIZE

    background = get_random_color()
    screen.fill(background)

    while True:
        buffer.blit(screen, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        pressed = pygame.mouse.get_pressed()
        if pressed[0]:
            if size > SIZE_LIMIT:
                size = STARTING_SIZE

            color = get_random_color()
            char = get_random_char(size, color)

            w, h = char.get_size()
            pos = pygame.mouse.get_pos()
            pos = pos[0] - w // 2, pos[1] - h // 2

            buffer.blit(char, pos)
            size += SIZE_STEP
        else:
            size = STARTING_SIZE

        if MOVEMENT_SPEED:
            screen.fill(background)
        screen.blit(buffer, (-MOVEMENT_SPEED, 0))

        pygame.display.update()
        pygame.time.delay(25)


if __name__ == '__main__':
    play()


# rainbow mystical T
