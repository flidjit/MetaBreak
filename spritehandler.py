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
    def __init__(self, master=None):
        super().__init__(master=master, bg='black')
        self.sheet = Sheet()
        self.sheet_image = None
        self.name_lbl = tk.Label(
            self, text=' Sprite Name: ', bg='black', fg='white')
        self.name_lbl.grid(column=0, row=0)
        self.name_ent = tk.Entry(
            self, bg='black', fg='green')
        self.name_ent.grid(column=1, row=0)
        self.arts_lbl = tk.Label(
            self, text=' Artist Name: ', bg='black', fg='white')
        self.arts_lbl.grid(column=0, row=1)
        self.arts_ent = tk.Entry(
            self, bg='black', fg='green')
        self.arts_ent.grid(column=1, row=1)
        self.desc_lbl = tk.Label(
            self, text=' Description: ', bg='black', fg='white')
        self.desc_lbl.grid(column=0, row=2)
        self.desc_ent = tk.Entry(
            self, bg='black', fg='green')
        self.desc_ent.grid(column=1, row=2)
        self.aply_but = tk.Button(
            self, text=' Apply ', command=self.set_data)
        self.aply_but.grid(column=1, row=3)
        self.grid()
        self.load_image()

    def load_image(self):
        self.withdraw()
        filename = filedialog.askopenfilename()
        self.sheet_image = pg.image.load(filename).convert_alpha()
        self.deiconify()

    def calc_dim(self, cols=12, rows=6):
        self.sheet.cell_size[0] = self.sheet_image.get_width() / cols
        self.sheet.cell_size[1] = self.sheet_image.get_width() / rows

    def set_data(self):
        self.sheet.name = self.name_ent.get()
        self.sheet.artist = self.arts_ent.get()
        self.sheet.description = self.desc_ent.get()
        self.calc_dim()


class SpriteToolz:
    def __init__(self):
        self.view = ViewPort()
        self.root = tk.Tk()
        self.root.withdraw()
        self.winder = InputWindow(self.root)

    def update(self):
        self.winder.update()
        self.view.scene.fill((10, 0, 10))
        if self.winder.sheet_image:
            self.view.scene.blit(self.winder.sheet_image, (0, 0))
        self.view.update()


S_T = SpriteToolz()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    S_T.update()
