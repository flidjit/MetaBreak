import pygame as pg
from pygame.locals import *
import pickle
import sys
import os


class Camera:
    def __init__(self, x, y):
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
        self.scene = pg.display.set_mode((1000, 600))
        self.clock = pg.time.Clock()
        self.fps = 60

    def update(self):
        pg.display.flip()
        self.clock.tick(self.fps)