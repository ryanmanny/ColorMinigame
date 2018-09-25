import pygame
import util

RESOLUTION = 800, 800

STARTING_SIZE = 13
SIZE_LIMIT = 200
SIZE_STEP = 3
MOVEMENT_SPEED = 7


def main():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    buffer = pygame.Surface(RESOLUTION)

    size = STARTING_SIZE

    background = util.get_random_color()
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

            color = util.get_random_color()
            char = util.get_random_char(size, color)

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
    main()


# rainbow mystical T
