import pygame
import logging

from config import Color, Font


class BaseText(pygame.Surface):
    """A much better text system"""

    def __init__(
        self,
        text="",
        font=Font.default,
        text_color=Color.TEXT_COLOR,
        horizontal_center=False,
        *args,
        **kwargs
    ):
        """
        The max size of this text box is calculated by the initial text provided
        """
        super().__init__(
            (font.render(text)[1].size[0], font.get_sized_height()), *args, **kwargs
        )
        self.font = font
        self.text_color = text_color
        self.horizontal_center = horizontal_center

        self.render_cache = None
        self.text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self.render_cache = self.font.render(value, self.text_color)
        self.fill((0, 0, 0, 0))
        self.blit(*self.render_cache)
        self._text = value

    def blit_to(self, surface, pos):
        x, y = pos
        surface.blit(
            self.render_cache[0],
            (
                x
                + self.render_cache[1].left
                - (self.render_cache[1].width // 2 if self.horizontal_center else 0),
                y + self.font.size - self.render_cache[1].top,
            ),
        )
