import pygame
import logging

from config import Color, Font
from managers import ui


class BaseButton(pygame.Surface):
    """
    Center text by default
    """

    def __init__(
        self,
        width,
        height,
        inner_text="Button",
        text_color=Color.TEXT_COLOR,
        font=Font.default,
        button_name=None,
    ):
        super().__init__((width, height), pygame.SRCALPHA)

        self.width, self.height = width, height
        self.text_color = text_color
        self.font = font
        self.text = inner_text
        self.selected = False
        self.pressed = False

        self.button_name = button_name or "Unnamed button"

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.font_render = self.font.render(self.text, self.text_color)
        self.font_render[1].center = self.get_rect().center

    def press(self):
        self.pressed = True
        logging.info(f"Button {self.button_name} pressed")

    def unpress(self):
        self.pressed = False

    def render_text(self):
        self.blit(*self.font_render)

    def update(self):
        self.fill((0, 0, 0, 0))

        self.render_text()


class ImageButton(BaseButton):
    def __init__(self, base_image, pressed_image=None, scale=1, *args, **kwargs):
        width, height = base_image.get_size()
        super().__init__(width, height, *args, **kwargs)
        self.base_image = base_image
        self.pressed_image = pressed_image or base_image
        self.select_arrow = ui.button_select

    def update(self):
        self.fill((0, 0, 0, 0))

        # display base image
        if self.pressed:
            self.blit(self.base_image, (0, 0))
        else:
            self.blit(self.pressed_image, (0, 0))

        # selected arrow
        if self.selected:
            self.blit(self.select_arrow, (0, 0))

        self.render_text()
