import pygame

import math
import itertools

RESOLUTION = 512, 512


def rainbow(freq=.01):  # RAINBOW GENERATOR
    # https://krazydad.com/tutorials/makecolors.php
    pi = math.pi
    offset = 2 * pi / 3

    for i in itertools.count():
        r = 128 + 127 * math.sin(freq*i)
        g = 128 + 127 * math.sin(freq*i + offset)
        b = 128 + 127 * math.sin(freq*i + offset * 2)

        yield r, g, b


def get_diagonals(resolution=RESOLUTION):
    diagonals = []
    for i in range(max(resolution) * 2):  # Gets longest dimension of screen
        diagonals.append(
            (i, j) for i, j
            in zip(range(i), range(i)[::-1])
            if i < resolution[0]
            if j < resolution[1]
        )

    return diagonals


def demo():
    pygame.init()

    screen = pygame.display.set_mode(RESOLUTION)
    colors = rainbow()
    diagonals = get_diagonals()

    for i in itertools.count():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        for color, diagonal in zip(colors, diagonals):
            for pixel in diagonal:
                screen.set_at(pixel, color)

        pygame.display.update()
        pygame.time.delay(25)


if __name__ == '__main__':
    demo()


# RGB is a cube
