from tkinter import *
from tkinter import ttk
import sys
import pygame as pg
from pygame.locals import *
import os
import math
import pickle
import base64
from enum import Enum



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


class MainGame:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.view = ViewPort()
        self.user_ = None
        self.tool_bar = None

    def update(self):
        self.view.camera.update()
        # kill the toolbar when you are done with it.
        if self.tool_bar.die:
            self.tool_bar.destroy()
            self.tool_bar = None
        # fill the scene with visual information
        # and update the toolbar.
        self.view.scene.fill((10, 0, 10))
        if self.tool_bar:
            self.tool_bar.update(self.view)
        # show the title screen if there is no toolbar.
        else:
            print('draw the title scene.')
        # Buttons : Host Game, Join Game,
        #           Campaign Editor, Sprite Editor, Sphere Editor,
        #           Options, Quit
        self.view.update()
