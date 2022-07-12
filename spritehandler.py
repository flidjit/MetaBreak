from gamewindows import *


class Sheet:
    def __init__(self, name):
        self.name = name
        self.size = [0, 0]
        self.cells = []


class SpriteTools:
    @staticmethod
    def new_sheet(filename='Ts_1', cols=10, rows=10):
        """ Turn a .png sprite sheet into a .sptx object"""
        view = ViewPort()
        filename_ = 'Sprites/' + filename + '.png'
        sheet_img = pg.image.load(filename_).convert_alpha()
        sheet = Sheet(filename)
        sheet.size = [sheet_img.get_width()/cols,
                      sheet_img.get_height()/rows]
        for i in range(cols):
            for j in range(rows):
                x = j*sheet.size[0]
                y = i*sheet.size[1]
                sheet_img.set_clip(pg.Rect(x, y, sheet.size[0], sheet.size[1]))
                clip = pg.image.tostring(
                    sheet_img.subsurface(sheet_img.get_clip()), 'RGBA')
                sheet.cells.append(clip)
        outgoing = open('Sprites/'+filename+'.sptx', 'wb')
        pickle.dump(sheet, outgoing)
        outgoing.close()