# setup stuff here
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from . import set_logger

import pygame
from pygame import freetype

pygame.init()
pygame.freetype.init()

# def blit_text(self, text_object, font):
#     return self.blit(text_object[0],)

# pygame.Surface.blit_text =


def hex_to_rgb(value):
    value = value.lstrip("#")

    lv = len(value)
    rgb = tuple(int(value[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))

    return rgb


SCREEN_WIDTH = 720
SCREEN_HEIGHT = 560

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Font:
    acme = pygame.freetype.Font("resources/fonts/acme.ttf", 32)
    daemon = pygame.freetype.Font("resources/fonts/daemon.ttf", 32)
    comfortaa = pygame.freetype.Font("resources/fonts/comfortaa.ttf", 32)
    pixel = pygame.freetype.Font("resources/fonts/pixel.ttf", 32)


Font.default = Font.pixel


class Color:
    BACKGROUND = hex_to_rgb("#06181E")  # Background Color
    TEXT_BACKGROUND = hex_to_rgb("#460D3A")  # Text Background
    TEXT_COLOR = hex_to_rgb("#FFFFFF")  # Normal Text Color
    TEXT_INVERSE = hex_to_rgb("#00000")  # Inverted Text Color
    TEXT_RED = hex_to_rgb("#FF0000")  # Names are red
    TEXT_GREEN = hex_to_rgb("#00FF00")  # Places are green
    TEXT_BLUE = hex_to_rgb("#0000FF")  # Things are blue
    BORDER_ONE = hex_to_rgb("#0ED1F0")  # Border Color One
    BORDER_TWO = hex_to_rgb("#F0CD00")  # Border Color Two
