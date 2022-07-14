from prototyping import *


# ToDo :
#  * ???.


class MasterMode(tk_.Toplevel):
    def __init__(self, master=None, user_=User(), ui_=PgUI()):
        super().__init__(master=master, bg='black')
        self.resizable(False, False)
        self.map_ = None
        self.ui_ = None
        self.popup = None
        self.art_ = {}
        self.change_mode = None
        self.user_ = user_

    def prepare_art(self, user_=None):
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
        destination = open('User/'+self.user_.screen_name+'.usr', 'wb')
        pickle.dump(self.user_, destination)
        destination.close()

    def render_iso(self):
        print('render an isometric map')


class TitleMode(MasterMode):
    def __init__(self, user_=User()):
        super().__init__()
        self.intro_image = pg_.image.load('Rec/scrap/main_menu.png')
        self.intro_image = pg_.transform.scale(self.intro_image, (1000, 600))
        self.withdraw()

    def take_input(self, event):
        if event.type == pg_.MOUSEBUTTONUP:
            pos = pg_.mouse.get_pos()
            a = None
            for i in self.ui_.buttons:
                b = self.ui_.buttons[i]
                if b.x_1 < pos[1] < b.x_2:
                    if b.y_1 < pos[2] < b.y_2:
                        a = b.action
            if a is None:
                print('No button pushed...')
            elif a is 'Options':
                print('you get an options popup')
            else:
                self.change_mode = a

    def draw_scene(self, view):
        view.scene.blit(self.intro_image, (0, 0))
