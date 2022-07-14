import pygame as pg
from pygame.locals import *


class Camera:
    def __init__(self, x=10, y=10):
        self.location = [x, y]
        self.target = [x, y]

    def update(self):
        print('Ease the camera towards the target.')


class ViewPort:
    def __init__(self):
        """ This object represents a pygame display window."""
        pg.init()
        pg.font.init()
        pg.display.set_caption("MetaBreak")
        self.camera = Camera()
        self.scene = pg.display.set_mode((1000, 600))
        self.clock = pg.time.Clock()
        self.fps = 30

    def update(self):
        pg.display.flip()
        self.clock.tick(self.fps)
