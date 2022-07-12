from gamewindows import ViewPort
import pygame as pg
import pickle
import sys
import io
import base64
from pillow import Image
from itertools import product

class Sheet:
    def __init__(self, name='~name~'):
        self.name = name
        self.description = ''
        self.artist = ''
        self.cell_size = [0, 0]
        self.cells = []
        self.animations = {}


class SpriteToolz:
    def __init__(self):
        self.view = ViewPort()
        self.sheet = Sheet()
        self.sheet_image = None

    def load_image(self, filename='name'):
        filename = 'Sprites/New/'+filename+'.png'
        self.sheet_image = pg.image.load(filename).convert_alpha()

    def set_user_input(self, name='name', description='desc...', artist='unknown'):
        self.sheet.name = name
        self.sheet.description = description
        self.sheet.artist = artist

    def calc_dim(self, cols=12, rows=6):
        self.sheet.cell_size[0] = self.sheet_image.get_width() / cols
        self.sheet.cell_size[1] = self.sheet_image.get_width() / rows

    def break_image(filename, dir_in, dir_out, d):
        name, ext = os.path.splitext(filename)
        img = Image.open(os.path.join(dir_in, filename))
        w, h = img.size

        grid = product(range(0, h - h % d, d), range(0, w - w % d, d))
        for i, j in grid:
            box = (j, i, j + d, i + d)
            out = os.path.join(dir_out, f'{name}_{i}_{j}{ext}')
            img.crop(box).save(out)

    # def new_sheet(self, filename='Ts_1', cols=12, rows=6):
    #     """ Turn a .png sprite sheet into a .sptx object"""
    #     filename_ = 'Sprites/'+filename+'.png'
    #     self.this_sheet = pg.image.load(filename_).convert_alpha()
    #     self.sheet_save = Sheet(filename)
    #     self.sheet_save.size = [self.this_sheet.get_width()/cols,
    #                   self.this_sheet.get_height()/rows]
    #     for i in range(cols):
    #         for j in range(rows):
    #             x = j*self.sheet_save.size[0]
    #             y = i*self.sheet_save.size[1]
    #             self.this_sheet.set_clip(pg.Rect(
    #                 x, y, self.sheet_save.size[0], self.sheet_save.size[1]))
    #             clip = pg.image.tostring(
    #                 self.this_sheet.subsurface(self.this_sheet.get_clip()), 'RGBA')
    #             self.sheet_save.cells.append(clip)
    #     outgoing = open('Sprites/'+filename+'.sptx', 'wb')
    #     pickle.dump(self.sheet_save, outgoing)
    #     outgoing.close()

    def update(self):
        self.view.scene.fill((20, 0, 20))
        self.view.scene.blit(self.this_sheet, (0, 0))
        mg = io.BytesIO(base64.b64decode(photo))
        pepeImg = pygame.image.load(output)
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
