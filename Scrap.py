# def break_image(self, dir_in, dir_out):
#     d = self.sheet.cell_size
#     filename = 'Sprites/New/Ts_1.png'
#     name, ext = os.path.splitext(filename)
#     img = Image.open(os.path.join(dir_in, filename))
#     w, h = img.size
#     grid = product(range(0, h - h % d, d), range(0, w - w % d, d))
#     for i, j in grid:
#         box = (j, i, j + d, i + d)
#         out = os.path.join(dir_out, f'{name}_{i}_{j}{ext}')
#         img.crop(box).save(out)

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