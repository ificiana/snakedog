import logging
import pygame

import config
from config import Color
import scenes

from animations import Shake, Bounce


class Game:
    def __init__(self):
        logging.info("Starting game object initialization")
        # Inject self
        pygame.game = self

        self.running = False

        # screen has to be loaded first because of some of the
        # utilities we are using
        self.screen = config.screen

        # Add many more screens later
        class Scenes(object):
            start_screen = scenes.StartScreen(self)
            menu = scenes.Menu(self)
            game_scene = scenes.GameScene(self)
            level_select = scenes.LevelSelect(self)
            uitest = scenes.UITest(self)

        self.scenes = Scenes()

        self.hotkeys = [
            self.scenes.start_screen,
            self.scenes.menu,
            self.scenes.game_scene,
            self.scenes.level_select,
            self.scenes.uitest,
        ]

        class Animations(object):
            bounce = Bounce(120, 0, 20)
            shake = Shake(-5, 5)
            pass

        self.animations = Animations()

        # set first scene
        self.scene = self.scenes.uitest

        self.level = 1

        self.clock = pygame.time.Clock()

        logging.info("Finished game object initialization")

    def update_animations(self):
        # Have to manually enumerate animations and add conditions
        self.animations.bounce.update()
        self.animations.shake.update()

    def main(self):
        """
        Blocking entry point for the entire game
        """
        logging.info("Staring main game loop")

        self.running = True

        while self.running:
            self.fps = self.clock.get_fps()

            for event in pygame.event.get():
                if self.event(event):
                    continue
                if self.scene.event(event):
                    continue
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(Color.BACKGROUND)

            self.update_animations()

            self.scene.render()

            self.draw_fps()

            pygame.display.update()

            self.clock.tick(60)

        logging.info("Main game loop terminated successfully")

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self.scenes.game_scene.level = level
        self._level = level

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                self.scene = self.scenes.start_screen
                return True
            if event.key == pygame.K_F2:
                self.scene = self.scenes.menu
                return True
            if event.key == pygame.K_F3:
                self.scene = self.scenes.game_scene
                return True
            if event.key == pygame.K_F4:
                self.scene = self.scenes.level_select
                return True
            if event.key == pygame.K_F5:
                self.scene = self.scenes.uitest
                return True

    def draw_fps(self):
        fps_text = config.Font.default.render(
            "FPS: " + str(int(self.fps)), Color.TEXT_COLOR
        )

        self.screen.blit(
            fps_text[0], (fps_text[1].left, config.Font.default.size - fps_text[1].top)
        )
