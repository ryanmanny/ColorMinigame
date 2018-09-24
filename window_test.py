import pygame
import util

RESOLUTION = 400, 400

STARTING_SIZE = 13
SIZE_LIMIT = 200
SIZE_STEP = 3


def main():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)

    screen.fill(util.get_random_color())
    size = STARTING_SIZE

    while True:
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

            screen.blit(char, pos)
            size += SIZE_STEP
        else:
            size = STARTING_SIZE

        pygame.display.flip()
        pygame.time.delay(25)


if __name__ == '__main__':
    main()


# rainbow mystical T
