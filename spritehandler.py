from gamewindows import ViewPort
import pygame as pg
import pickle
import sys


class Sheet:
    def __init__(self, name):
        self.name = name
        self.description = ''
        self.artist = ''
        self.size = [0, 0]
        self.cells = []


class SpriteToolz:
    def __init__(self):
        self.view = ViewPort()
        self.this_sheet = None
        self.view_sheet = None
        self.sheet_save = None

    def new_sheet(self, filename='Ts_1', cols=12, rows=6):
        """ Turn a .png sprite sheet into a .sptx object"""
        filename_ = 'Sprites/'+filename+'.png'
        self.this_sheet = pg.image.load(filename_).convert_alpha()
        self.sheet_save = Sheet(filename)
        self.sheet_save.size = [self.this_sheet.get_width()/cols,
                      self.this_sheet.get_height()/rows]
        for i in range(cols):
            for j in range(rows):
                x = j*self.sheet_save.size[0]
                y = i*self.sheet_save.size[1]
                self.this_sheet.set_clip(pg.Rect(
                    x, y, self.sheet_save.size[0], self.sheet_save.size[1]))
                clip = pg.image.tostring(
                    self.this_sheet.subsurface(self.this_sheet.get_clip()), 'RGBA')
                self.sheet_save.cells.append(clip)
        outgoing = open('Sprites/'+filename+'.sptx', 'wb')
        pickle.dump(self.sheet_save, outgoing)
        outgoing.close()

    def update(self):
        self.view.scene.fill((20, 0, 20))
        self.view.scene.blit(self.this_sheet, (0, 0))
        mg = pg.image.fromstring(
            self.sheet_save.cells[0], (
                self.sheet_save.size[0], self.sheet_save.size[0]), 'RGBA')
        self.view.scene.blit(mg, (40, 40))
        self.view.update()


this = SpriteToolz()
this.new_sheet()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    this.update()
