import pygame
import random


def get_random_char(size, color):
    char = chr(random.randint(33, 127))
    return pygame.font.Font(pygame.font.get_default_font(), size).render(char, False, color)


def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
