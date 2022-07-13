#!/usr/bin/env python

from gamewindows import ViewPort
import pygame as pg
from tkinter import *
from tkinter import filedialog, scrolledtext, ttk
import pickle
import sys
import io
import base64


class Map:
    def __init__(self, x_size=10, y_size=15):
        self.name = '_name_'
        self.description = ' ... '
        self.creation_date = ''
        self.tile_sets = []
        self.sprites = []
        self.size = [x_size, y_size]
        self.tile_array = [[0 for i in range(x_size)] for j in range(y_size)]


class InputWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master, bg='black')
        self.resizable(False, False)


class MapToolz:
    def __init__(self):
        self.view = ViewPort()
        self.root = Tk()
        self.root.withdraw()
        self.tool_window = InputWindow(self.root)

    def update(self):
        self.tool_window.update()
        self.view.update()
