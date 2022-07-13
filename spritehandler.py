#!/usr/bin/env python

from gamewindows import ViewPort
from prototyping import Sheet
import pygame as pg
from tkinter import *
from tkinter import filedialog, scrolledtext, ttk
import pickle
import sys
import io
import base64


class InputWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master, bg='black')
        self.resizable(False, False)
        self.sheet = Sheet()
        self.filename = None
        self.name_lbl = Label(
            self, text=' Sprite Name: ', bg='black', fg='white')
        self.name_lbl.grid(column=0, row=0, sticky='e', padx=5)
        self.name_ent = Entry(
            self, bg='black', fg='green')
        self.name_ent.grid(column=1, row=0, columnspan=2, sticky='w')
        self.arts_lbl = Label(
            self, text=' Artist Name: ', bg='black', fg='white')
        self.arts_lbl.grid(column=0, row=1, sticky='e')
        self.arts_ent = Entry(
            self, bg='black', fg='green')
        self.arts_ent.grid(column=1, row=1, columnspan=2, sticky='w')
        self.desc_lbl = Label(
            self, text=' Description: ', bg='black', fg='white')
        self.desc_lbl.grid(column=0, row=2, sticky='e')
        self.desc_ent = scrolledtext.ScrolledText(
            self, bg='black', fg='green', height=5, width=30)
        self.desc_ent.grid(column=1, row=2, columnspan=2, sticky='w')
        self.rows_lbl = Label(
            self, text=' # of rows: ', bg='black', fg='white')
        self.rows_lbl.grid(column=0, row=3, sticky='e')
        self.rows_spb = ttk.Spinbox(self, width=3, from_=1, to=30)
        self.rows_spb.grid(column=1, row=3, sticky='w')
        self.cel_num_lbl = Label(
            self, bg='black', fg='pink', text=' # of Cells:')
        self.cel_num_lbl.grid(column=2, row=3, sticky='w')
        self.cols_lbl = Label(
            self, text=' # of columns: ', bg='black', fg='white')
        self.cols_lbl.grid(column=0, row=4, sticky='e')
        self.cols_spb = ttk.Spinbox(self, width=3, from_=1, to=30)
        self.cols_spb.grid(column=1, row=4, sticky='w')
        self.cel_siz_lbl = Label(
            self, bg='black', fg='pink', text=' Cell Size:')
        self.cel_siz_lbl.grid(column=2, row=4, sticky='w')
        self.cont_frm = Frame(self)
        self.cont_lbl = Label(
            self.cont_frm, bg='black', fg='white', text='Contact Point - X:')
        self.cont_lbl.grid(column=0, row=0)
        self.cont_x_spb = ttk.Spinbox(self.cont_frm, width=4, from_=1, to=300)
        self.cont_x_spb.grid(column=1, row=0)
        self.cont_lbl_2 = Label(
            self.cont_frm, bg='black', fg='white', text=' Y:')
        self.cont_lbl_2.grid(column=2, row=0)
        self.cont_y_spb = ttk.Spinbox(self.cont_frm, width=4, from_=1, to=300)
        self.cont_y_spb.grid(column=3, row=0, sticky='w')
        self.cont_frm.grid(column=0, row=5, columnspan=4)
        self.iso_frm = Frame(self)
        self.iso_lbl = Label(
            self.iso_frm, bg='black', fg='white', text='Isometric Offset - X:')
        self.iso_lbl.grid(column=0, row=0)
        self.iso_x_spb = ttk.Spinbox(self.iso_frm, width=4, from_=1, to=300)
        self.iso_x_spb.grid(column=1, row=0)
        self.iso_lbl_2 = Label(
            self.iso_frm, bg='black', fg='white', text=' Y:')
        self.iso_lbl_2.grid(column=2, row=0)
        self.iso_y_spb = ttk.Spinbox(self.iso_frm, width=4, from_=1, to=300)
        self.iso_y_spb.grid(column=3, row=0, sticky='w')
        self.iso_frm.grid(column=0, row=6, columnspan=4)
        self.butt_frm = Frame(self, bg='black')
        self.aply_but = Button(
            self.butt_frm, text=' Apply ', bg='#39114f',
            fg='#69f002', command=self.apply)
        self.aply_but.grid(column=0, row=0)
        self.new_but = Button(
            self.butt_frm, text=' New ', command=self.new_sprite)
        self.new_but.grid(column=1, row=0)
        self.save_but = Button(
            self.butt_frm, text=' Save ', command=self.save_sprite)
        self.save_but.grid(column=2, row=0)
        self.load_but = Button(
            self.butt_frm, text=' load ', command=self.load_sprite)
        self.load_but.grid(column=3, row=0)
        self.butt_frm.grid(column=1, row=7, columnspan=2)
        self.grid()
        self.show_data()

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
        self.sheet.image = pg.image.load(tmp_img)
        self.deiconify()
        self.show_data()

    def new_sprite(self):
        self.withdraw()
        self.filename = filedialog.askopenfilename()
        self.sheet.image = pg.image.load(self.filename).convert_alpha()
        with open(self.filename, 'rb') as img:
            img = img.read()
            self.sheet.image_string = base64.b64encode(img)
        self.deiconify()
        self.show_data()

    def apply(self):
        self.sheet.name = self.name_ent.get()
        self.sheet.artist = self.arts_ent.get()
        self.sheet.description = self.desc_ent.get(1.0, END)
        self.sheet.cell_size = [
            int(self.cols_spb.get()), int(self.rows_spb.get())]
        self.sheet.cell_size[0] = int(self.cols_spb.get())
        self.sheet.contact_point = [
            int(self.cont_x_spb.get()), int(self.cont_y_spb.get())]
        self.calc_dim()
        self.show_data()
        self.make_cells()

    def show_data(self):
        self.name_ent.delete(1, END)
        self.name_ent.insert(END, self.sheet.name)
        self.arts_ent.delete(1, END)
        self.arts_ent.insert(END, self.sheet.artist)
        self.desc_ent.delete(1.0, END)
        self.desc_ent.insert(END, self.sheet.description)
        self.cols_spb.set(self.sheet.num_of_cols)
        self.rows_spb.set(self.sheet.num_of_rows)
        self.cont_x_spb.set(self.sheet.contact_point[0])
        self.cont_y_spb.set(self.sheet.contact_point[1])
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
        self.root = Tk()
        self.root.withdraw()
        self.view = ViewPort()
        self.input_window = InputWindow(self.root)

    def update(self):
        self.input_window.update()
        self.view.scene.fill((10, 0, 10))
        if self.input_window.sheet.image:
            self.view.scene.blit(self.input_window.sheet.image, (0, 0))
        for square in self.input_window.sheet.cells:
            pg.draw.rect(self.view.scene, 'red', square, 1)
        cp = self.input_window.sheet.contact_point
        pg.draw.line(self.view.scene, 'yellow', (
            cp[0]-10, cp[1]), (cp[0]+10, cp[1]), 1)
        pg.draw.line(self.view.scene, 'yellow', (
            cp[0], cp[1]-10), (cp[0], cp[1]+10), 1)
        self.view.update()


S_T = SpriteToolz()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    S_T.update()
