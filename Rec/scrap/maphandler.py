#!/usr/bin/env python

from Rec.scrap.gamewindows import ViewPort
import pygame as pg
from tkinter import *
import sys


class Tile:
    def __init__(self):
        self.tile_sheet = 'default'
        self.cel_id = 0
        self.scr_x_ = 0
        self.scr_y_ = 0
        self.height = 0


class TileStack:
    def __init__(self):
        self.map_x_ = 0
        self.map_y_ = 0
        self.scr_x_ = 0
        self.scr_y_ = 0
        self.floor_height = 0
        self.stack_ = [Tile()]


class GameMap:
    def __init__(self, x_size=10, y_size=15):
        self.name = '_name_'
        self.description = ' ... '
        self.creation_date = ''
        self.size = [x_size, y_size]
        self.iso_offset = [43, 24]
        self.sprite_list = ['default', 'pawns', 'symbols']
        self.array_ = [[TileStack() for i in range(x_size)] for j in range(y_size)]


class MapEditorToolbar(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master, bg='black')
        self.resizable(False, False)
        self.map_ = GameMap()
        self.art_ = {}
        self.calculate_offsets()

    def calculate_offsets(self):
        x_offset = self.map_.iso_offset[0]
        y_offset = self.map_.iso_offset[1]
        for i in range(len(self.map_.array_)):
            for j in range(len(self.map_.array_[i])):
                self.map_.array_[i][j].map_x_ = i
                self.map_.array_[i][j].map_y_ = j
                self.map_.array_[i][j].scr_x_ = i*x_offset
                self.map_.array_[i][j].scr_y_ = j*y_offset
                self.map_.array_[i][j].stack_[0].scr_x_ = i*x_offset
                self.map_.array_[i][j].stack_[0].scr_y_ = j*y_offset

    def prepare_sprites(self):
        for i in self.map_.sprite_list:
            self.art_[i] = 'poop'
        print('change the sprite list into a dictionary and load sprites into them.')


class MapToolz:
    def __init__(self):
        self.view = ViewPort()
        self.root = Tk()
        self.root.withdraw()
        self.tool_window = MapEditorToolbar(self.root)

    def draw_map(self):
        for i in range(len(self.tool_window.map_.array_)):
            for j in range(len(self.tool_window.map_.array_[i])):
                for k in range(len(self.tool_window.map_.array_[i][j].stack_)):
                    this_tile = self.tool_window.map_.array_[i][j].stack_[k]
                    sht_id = this_tile.tile_sheet
                    sht_img = self.tool_window.art_[sht_id]
                    cel_id = this_tile.cel_id
                    cel_img = 'this cell'
                    cam_x = self.view.camera.location[0]
                    cam_y = self.view.camera.location[1]
                    self.view.scene.blit()

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