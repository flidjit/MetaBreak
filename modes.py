from prototyping import *


class MasterMode(tk_.Toplevel):
    def __init__(self, master=None, user_=User()):
        super().__init__(master=master, bg='black')
        self.resizable(False, False)
        self.map_ = None
        self.ui_ = None
        self.popup = None
        self.art_ = {}
        self.swap_modes = False
        self.user_copy = user_

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

    def decode_image(self, image):
        print('decode an image')

    def save_user_data(self):
        print('save the user copy to the main file')

    def render_iso(self):
        print('render an isometric map')

    def render_ui(self):
        print('render the ui')
