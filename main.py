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
from gamewindows import ViewPort


class Camera:
    def __init__(self, x=10, y=10):
        self.location = [x, y]
        self.target = [x, y]

    def update(self):
        print('Ease the camera towards the target.')


class MainGame:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.view = ViewPort()
        self.tool_bar = None
        # Buttons : Host Game, Join Game,
        #           Campaign Editor, Sprite Editor, Sphere Editor,
        #           Options, Quit

    def update(self):
        if self.tool_bar.die:
            self.tool_bar = None
        self.view.scene.fill((10, 0, 10))
        if self.tool_bar:
            self.tool_bar.update(self.view)
        else:
            print('draw the title scene.')
        self.view.update()
