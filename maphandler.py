#!/usr/bin/env python

from gamewindows import ViewPort
import pygame as pg
from tkinter import *
from tkinter import filedialog, scrolledtext, ttk
import pickle
import sys
import io
import base64


class Tile:
    def __init__(self):
        self.tile_sheet = 'default'
        self.image_id = 0
        self.screen_x = 0
        self.screen_y = 0
        self.height = 0


class TileStack:
    def __init__(self):
        self.map_x = 0
        self.map_y = 0
        self.screen_x = 0
        self.screen_y = 0
        self.floor_height = 0
        self.stack = [Tile()]


class GameMap:
    def __init__(self, x_size=10, y_size=15):
        self.name = '_name_'
        self.description = ' ... '
        self.creation_date = ''
        self.size = [x_size, y_size]
        self.tile_sets = ['default']
        self.sprites = ['pawns', 'symbols']
        self.tile_array = [[TileStack() for i in range(x_size)] for j in range(y_size)]


class InputWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master, bg='black')
        self.resizable(False, False)
        self.current_map = GameMap()

    def calculate_offsets(self):
        print('calculate the initial screen positions for each tilestack')


class MapToolz:
    def __init__(self):
        self.view = ViewPort()
        self.root = Tk()
        self.root.withdraw()
        self.tool_window = InputWindow(self.root)

    def draw_map(self):
        print('draw the map')

    def update(self):
        self.tool_window.update()
        self.view.update()


M_T = MapToolz()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    M_T.update()