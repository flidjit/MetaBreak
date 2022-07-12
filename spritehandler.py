from gamewindows import ViewPort
import pygame as pg
import tkinter as tk
from tkinter import filedialog
import pickle
import os
import sys
import io
import base64
from PIL import Image
from itertools import product


class Sheet:
    def __init__(self, name='_name_'):
        self.name = name
        self.description = ''
        self.artist = ''
        self.date = ''
        self.cell_size = [0, 0]
        self.cells = []
        self.animations = {}


class InputWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.name_lbl = tk.Label(text=' Sprite Name: ')
        self.name_lbl.grid()
        self.name_ent = tk.Entry()
        self.name_ent.grid()
        self.desc_lbl = tk.Label(text=' Description: ')
        self.desc_lbl.grid()
        self.desc_ent = tk.Entry()
        self.desc_ent.grid()
        self.arts_lbl = tk.Label(text=' Artist Name: ')
        self.arts_lbl.grid()
        self.arts_ent = tk.Entry()
        self.arts_ent.grid()
        self.grid()


class SpriteToolz:
    def __init__(self):
        self.view = ViewPort()
        self.sheet = Sheet()
        self.sheet_image = None
        root = tk.Tk()
        root.withdraw()
        self.load_image()
        self.set_user_input()
        self.calc_dim()

    def load_image(self):
        filename = filedialog.askopenfilename()
        self.sheet_image = pg.image.load(filename).convert_alpha()

    def set_user_input(self, name='name', description='desc...',
                       artist='unknown', date=''):
        self.sheet.name = name
        self.sheet.description = description
        self.sheet.artist = artist
        self.sheet.date = date

    def calc_dim(self, cols=12, rows=6):
        self.sheet.cell_size[0] = self.sheet_image.get_width() / cols
        self.sheet.cell_size[1] = self.sheet_image.get_width() / rows

    def update(self):
        self.view.scene.fill((10, 0, 10))
        if self.sheet_image:
            self.view.scene.blit(self.sheet_image, (0, 0))
        self.view.update()


this = SpriteToolz()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    this.update()
