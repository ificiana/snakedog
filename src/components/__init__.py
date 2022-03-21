import random

import pygame

from loaders import imageManager


class BaseTile(pygame.sprite.Sprite):
    def __init__(self, image=None):
        super().__init__()
        self.screen = pygame.display.get_surface()
        if image:
            self.image = image
            self.rect = self.image.get_rect()

    def update(self, offset=pygame.math.Vector2(0, 0)):
        if self.image:
            self.screen.blit(self.image, self.rect.topleft + offset)


class TileEntity(BaseTile):
    def __init__(self, type, x, y):
        # Implement loading many other images too
        super().__init__(imageManager.get_resource(type))
        self.x, self.y = pygame.math.Vector2(x, y)  # where it is in the game engine

        self.render_vx = 0
        self.render_vy = 0

    def update(self):
        # make sure to move rendering pos to physical pos gradually
        # use vx and vy
        pass


class Tile(BaseTile):
    def __init__(self, type):
        super().__init__(imageManager.get_resource(type))


class Grid(pygame.sprite.Group):
    def __init__(self, x, y, rows, cols, cell_width, cell_height):
        super().__init__()
        self.x = x
        self.y = y
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.width = cell_width * cols
        self.height = cell_height * rows
        self.rows = rows
        self.cols = cols
        self.grid = [[None for y in range(cols)] for x in range(rows)]

    def check(self, x, y):
        if x >= 0 and y >= 0 and x < self.width and y < self.height:
            return True
        raise Exception("Invalid cell coordinates")

    def set_cell(self, x, y, cell: BaseTile):
        self.check(x, y)
        self.remove(self.grid[x][y])
        self.grid[x][y] = cell
        self.add(cell)
        cell.rect.x = self.x + x * self.cell_width
        cell.rect.y = self.y + y * self.cell_height

    def get_cell(self, x, y):
        self.check(x, y)
        return self.grid[y][x]

    def update(self, *args, **kwargs):
        for sprite in sorted(self.sprites(), key=lambda x: x.rect.centery):
            sprite.update(
                *args,
                **kwargs,
                #offset=pygame.Vector2(0, -pygame.game.animations.bounce.value)
            )
