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

        from .text import BaseText

        self.text_component = BaseText(
            inner_text, font=font, text_color=text_color, horizontal_center=True
        )

        self.selected = False
        self.pressed = False

        self.button_name = button_name or "Unnamed button"

    @property
    def text(self):
        return self.text_component.text

    @text.setter
    def text(self, value):
        self.text_component.text = value

    def press(self):
        self.pressed = True
        logging.info(f"Button {self.button_name} pressed")

    def unpress(self):
        self.pressed = False

    def render_text(self):
        self.text_component.blit_to(
            self, pygame.Vector2(self.get_rect().center) + (0, -30)
        )

    def update(self):
        self.fill((0, 0, 0, 0))

        self.render_text()


class ImageButton(BaseButton):
    def __init__(self, base_image, pressed_image=None, scale=1, *args, **kwargs):
        self.scale = scale
        wh = pygame.Vector2(base_image.get_size()) * scale
        super().__init__(*wh, *args, **kwargs)
        self.base_image = pygame.transform.scale(base_image, wh)
        self.pressed_image = (
            pygame.transform.scale(pressed_image, wh)
            if pressed_image
            else self.base_image
        )
        self.select_arrow = pygame.transform.scale(
            ui.button_select, pygame.Vector2(ui.button_select.get_size()) * scale
        )

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
