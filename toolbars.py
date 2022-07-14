from tkinter import *


class MasterToolbar(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master, bg='black')
        self.resizable(False, False)
        self.map_ = None
        self.ui_ = None
        self.popup = None
        self.art_ = {}
        self.die = False

    def prepare_art(self, user_=None):
        del self.art_
        self.art_ = {}
        if self.map_:
            for i in self.map_.sprite_list:
                self.load_sprite(self.map_.sprite_list[i])
        if self.ui_:
            for i in self.ui_.sprite_list:
                self.load_sprite(self.ui_.sprite_list[i])

    def load_sprite(self, name):
        print('load the sprite')
