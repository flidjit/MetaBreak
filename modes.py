import pygame.mouse

from prototyping import *


class MasterMode(tk_.Toplevel):
    def __init__(self, master=None, user_=User()):
        super().__init__(master=master, bg='black')
        self.resizable(False, False)
        self.map_ = None
        self.ui_ = None
        self.popup = None
        self.art_ = {}
        self.change_mode = None
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


class TitleMode(MasterMode):
    def __init__(self):
        super().__init__()
        self.intro_image = pg_.image.load('Rec/scrap/main_menu.png')
        self.intro_image = pg_.transform.scale(self.intro_image, (1000, 600))
        self.withdraw()

    def take_input(self, event):
        if event.type == pg_.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(str(pos))

    def draw_scene(self, view):
        view.scene.blit(self.intro_image, (0, 0))
