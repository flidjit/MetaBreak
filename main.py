import tkinter as tk
from tkinter import ttk
import sys
import pygame as pg
from pygame.locals import *
import os
import math
import pickle
import base64


class TileSheet:
    def __init__(self, filename='Ts_1', cols=12, rows=6):
        filename = 'Sprites/' + filename + '.png'
        self.sheet = pg.image.load(filename).convert_alpha()
        self.cols = cols
        self.rows = rows
        self.celPos = []  # Cell Position List
        self.tileHeight = self.sheet.get_height() / self.rows
        self.tileWidth = self.sheet.get_width() / self.cols
        for i in range(self.cols):
            for j in range(self.rows):
                self.celPos.append([int(self.tileWidth * j), int(self.tileHeight * i)])

    def get_cell(self, id):
        self.sheet.set_clip(
            pg.Rect(self.celPos[id][0], self.celPos[id][1], self.tileWidth, self.tileHeight))
        return self.sheet.subsurface(self.sheet.get_clip())


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


class Camera():
    def __init__(self, x, y):
        self.location = [x, y]
        self.target = [x, y]

    def update(self):
        print('Ease the camera towards the target.')


