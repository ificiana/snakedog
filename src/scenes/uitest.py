import logging

import pygame
import random

import music

from .scene import BaseScene
from config import Color, Font

from ui import ImageButton
from managers import ui
import keyboard


class UITest(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.button = ImageButton(
            ui.green_button_large, inner_text="PLAY", font=Font.comfortaa, scale=4
        )

    def render(self):
        self.button.update()
        self.game.screen.blit(
            self.button,
            pygame.Vector2(self.game.screen.get_rect().center)
            - pygame.Vector2(self.button.get_rect().center),
        )

    def event(self, event):
        if keyboard.is_select(event):
            self.button.press()
            self.button.selected = not self.button.selected
            self.button.text = random.choice(["hi", "test", "CAP"])
