import pygame.image

from gamewindows import ViewPort
import pygame as pg
import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
import pickle
from enum import Enum
import os
import sys
import io
import base64
from PIL import Image
from itertools import product


class SS(Enum):
    TILES = 1
    SPRITE = 2
    EFFECT = 3


class Sheet:
    def __init__(self, name='_name_'):
        self.name = name
        self.description = ''
        self.artist = ''
        self.date = ''
        self.image = None
        self.image_string = None
        self.type = SS.TILES
        self.cell_size = [0, 0]
        self.contact_point = [0, 0]
        self.isometric = False
        self.isometric_offset = [0, 0]
        self.num_of_cells = 0
        self.num_of_cols = 0
        self.num_of_rows = 0
        self.cells = []
        self.animations = {}


class InputWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master, bg='black')
        self.resizable(False, False)
        self.sheet = Sheet()
        self.filename = None
        self.name_lbl = tk.Label(
            self, text=' Sprite Name: ', bg='black', fg='white')
        self.name_lbl.grid(column=0, row=0, sticky='e', padx=5)
        self.name_ent = tk.Entry(
            self, bg='black', fg='green')
        self.name_ent.grid(column=1, row=0, columnspan=2, sticky='w')
        self.arts_lbl = tk.Label(
            self, text=' Artist Name: ', bg='black', fg='white')
        self.arts_lbl.grid(column=0, row=1, sticky='e')
        self.arts_ent = tk.Entry(
            self, bg='black', fg='green')
        self.arts_ent.grid(column=1, row=1, columnspan=2, sticky='w')
        self.desc_lbl = tk.Label(
            self, text=' Description: ', bg='black', fg='white')
        self.desc_lbl.grid(column=0, row=2, sticky='e')
        self.desc_ent = tk.scrolledtext.ScrolledText(
            self, bg='black', fg='green', height=5, width=30)
        self.desc_ent.grid(column=1, row=2, columnspan=2, sticky='w')
        self.rows_lbl = tk.Label(
            self, text=' # of rows: ', bg='black', fg='white')
        self.rows_lbl.grid(column=0, row=3, sticky='e')
        self.rows_spb = ttk.Spinbox(self, width=3, from_=1, to=30)
        self.rows_spb.grid(column=1, row=3, sticky='w')
        self.cel_num_lbl = tk.Label(
            self, bg='black', fg='pink', text=' # of Cells:')
        self.cel_num_lbl.grid(column=2, row=3, sticky='w')
        self.cols_lbl = tk.Label(
            self, text=' # of columns: ', bg='black', fg='white')
        self.cols_lbl.grid(column=0, row=4, sticky='e')
        self.cols_spb = ttk.Spinbox(self, width=3, from_=1, to=30)
        self.cols_spb.grid(column=1, row=4, sticky='w')
        self.cel_siz_lbl = tk.Label(
            self, bg='black', fg='pink', text=' Cell Size:')
        self.cel_siz_lbl.grid(column=2, row=4, sticky='w')
        self.butt_frm = tk.Frame(self, bg='black')
        self.aply_but = tk.Button(
            self.butt_frm, text=' Apply ', bg='#39114f',
            fg='#69f002', command=self.apply)
        self.aply_but.grid(column=0, row=0)
        self.new_but = tk.Button(
            self.butt_frm, text=' New ', command=self.new_sprite)
        self.new_but.grid(column=1, row=0)
        self.save_but = tk.Button(
            self.butt_frm, text=' Save ', command=self.save_sprite)
        self.save_but.grid(column=2, row=0)
        self.load_but = tk.Button(
            self.butt_frm, text=' load ', command=self.load_sprite)
        self.load_but.grid(column=3, row=0)
        self.butt_frm.grid(column=1, row=5, columnspan=2)
        self.grid()
        self.new_sprite()

    def save_sprite(self):
        self.apply()
        ts = self.sheet.image
        self.sheet.image = None
        save_file = open('Sprites/'+self.sheet.name+'.sptx', 'wb')
        pickle.dump(self.sheet, save_file)
        save_file.close()
        self.sheet.image = ts

    def load_sprite(self):
        self.withdraw()
        filename = filedialog.askopenfilename(
            title="Select A Sprite",
            initialdir='Sprite/',
            filetypes=(("sprite files", "*.sptx"), ("sprite files", "*.spx")))
        load_file = open(filename, 'rb')
        self.sheet = pickle.load(load_file)
        load_file.close()
        tmp_img = io.BytesIO(base64.b64decode(self.sheet.image_string))
        self.sheet.image = pygame.image.load(tmp_img)
        self.deiconify()

    def new_sprite(self):
        self.withdraw()
        self.filename = filedialog.askopenfilename()
        self.sheet.image = pg.image.load(self.filename).convert_alpha()
        with open(self.filename, 'rb') as img:
            img = img.read()
            self.sheet.image_string = base64.b64encode(img)
        self.deiconify()

    def apply(self):
        self.sheet.name = self.name_ent.get()
        self.sheet.artist = self.arts_ent.get()
        self.sheet.description = self.desc_ent.get(1.0, tk.END)
        self.sheet.cell_size[1] = int(self.rows_spb.get())
        self.sheet.cell_size[0] = int(self.cols_spb.get())
        self.calc_dim()
        self.set_text()
        self.make_cells()

    def set_text(self):
        cs_1 = str(self.sheet.cell_size[0])
        cs_2 = str(self.sheet.cell_size[1])
        self.cel_siz_lbl['text'] = ' Cell Size: [ '+cs_1+'x'+cs_2+' px ]'
        self.cel_num_lbl['text'] = ' # of Cells: '+str(self.sheet.num_of_cells)

    def make_cells(self):
        for i in range(int(self.sheet.num_of_rows)):
            for j in range(int(self.sheet.num_of_cols)):
                self.sheet.cells.append(
                    (j*self.sheet.cell_size[0],
                     i*self.sheet.cell_size[1],
                     self.sheet.cell_size[0],
                     self.sheet.cell_size[1]))

    def calc_dim(self, cols=12, rows=6):
        self.sheet.cell_size[0] = int(self.sheet.image.get_width() / cols)
        self.sheet.cell_size[1] = int(self.sheet.image.get_height() / rows)
        self.sheet.num_of_cols = cols
        self.sheet.num_of_rows = rows
        self.sheet.num_of_cells = rows*cols


class SpriteToolz:
    def __init__(self):
        self.view = ViewPort()
        self.root = tk.Tk()
        self.root.withdraw()
        self.input_window = InputWindow(self.root)

    def update(self):
        self.input_window.update()
        self.view.scene.fill((10, 0, 10))
        if self.input_window.sheet.image:
            self.view.scene.blit(self.input_window.sheet.image, (0, 0))
        for square in self.input_window.sheet.cells:
            pg.draw.rect(self.view.scene, 'red', square, 1)
        self.view.update()


S_T = SpriteToolz()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    S_T.update()
