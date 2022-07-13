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


class MainWindow:
    def __init__(self):
        self.view = ViewPort()
        self.root = Tk()
        self.root.withdraw()
        self.tool_bar = None
        # Buttons : Host Game, Join Game,
        #           Campaign Editor, Sprite Editor, Sphere Editor,
        #           Options, Quit

    def update(self):
        if self.tool_bar:
            self.tool_bar.update()
        self.view.scene.fill((10, 0, 10))
        self.view.update()
