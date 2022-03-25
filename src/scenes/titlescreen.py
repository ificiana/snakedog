from random import randrange
import pygame

import music
from .scene import BaseScene
from config import Color, Font


class TitleScreen(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.font = Font.default
        self.title_logo_font = Font.title_logo
        # Title Text
        self.title = self.font.render(
            "Team Snakedog Presents...",
            True,
            Color.TEXT_COLOR,
            Color.TEXT_BACKGROUND,
        )
        
        #Title Name(Logo?)
        self.name = self.title_logo_font.render(
            "Evil Puzzle!",
            True,
            Color.TEXT_COLOR,
            Color.TEXT_BACKGROUND,
        )
        #Press Start
        self.press_start = self.font.render(
            "Press Start",
            True,
            Color.TEXT_COLOR,
            Color.TEXT_BACKGROUND,
        )
        self.title_rect = self.title.get_rect()
        self.title_rect.midtop = self.game.screen.get_rect().midtop
        self.name_rect = self.name.get_rect()
        self.name_rect.center = self.game.screen.get_rect().center
        self.press_start_rect = self.press_start.get_rect()
        self.press_start_rect.midbottom = self.game.screen.get_rect().midbottom
        self.soundtrack = music.music
        self.soundtrack.playBgm('resources/audio/music/JazzPad.ogg',0.5, True)
    def update(self):
        self.name = self.title_logo_font.render(
            "Evil Puzzle!",
            True,
            Color.randomColor(),
            Color.TEXT_BACKGROUND,
        )
    def render(self):
        self.game.screen.blit(self.title, self.title_rect)
        self.game.screen.blit(self.name, self.name_rect)
        self.game.screen.blit(self.press_start, self.press_start_rect)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.soundtrack.stopBgm()
                self.game.scene = self.game.scenes.game_scene
