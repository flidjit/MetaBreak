from prototyping import *


# ToDo :
#  * ???.


class MasterMode(tk_.Toplevel):
    """ This object represents a game mode. <MasterMode()> is the
    base class for 7 other modes, including:
    <PlayerMode()>, <GmMode()>, <TutorialMode()>, <SpriteMode()>,
    <SphereMode()>, <MapMode()>, and <TitleMode()>.
    The mode determines what gets drawn to the screen, and what
    popups are activated. All child objects will have a
    <.draw_scene> function that takes in the .scene object
    and draws on it."""
    def __init__(self, master=None, user_=User(),
                 map_=GameMap(), ui_=PgUI()):
        super().__init__(master=master, bg='black')
        self.resizable(False, False)
        self.map_ = map_
        self.ui_ = ui_
        self.popup = None
        self.art_ = {}
        self.change_mode = None
        self.user_ = user_

    def prepare_art(self, user_=None):
        """Load the sprites listed for this map into the <self.art_>
        dictionary, and set prepare them for display."""
        if self.map_:
            for i in self.map_.sprite_list:
                self.load_sprite(self.map_.sprite_list[i])
        if self.ui_:
            for i in self.ui_.sprite_list:
                self.load_sprite(self.ui_.sprite_list[i])

    def load_sprite(self, name):
        """ Un-pickle a .sptx object. """
        print('load the sprite')

    def decode_image(self, image):
        """ The image in the .sptx file will be saved as a string for
        serialization. Decode the string back into an image."""
        print('decode an image')

    def save_user_data(self):
        """ Saves all user data to memory."""
        destination = open('User/'+self.user_.screen_name+'.usr', 'wb')
        pickle.dump(self.user_, destination)
        destination.close()

    def render_iso(self):
        """ Render the <self.map_> object as isometric tiles."""
        print('render an isometric map')

    def pg_button_check(self, x, y):
        a = None
        for i in range(len(self.ui_.buttons)):
            b = self.ui_.buttons[i]
            if b.click_x_1 < x < b.click_x_2:
                if b.click_y_1 < y < b.click_y_2:
                    a = b.action
        print(a)
        return a


class TitleMode(MasterMode):
    """ This mode is active at startup. Allows the user to select
    among the other modes."""
    def __init__(self, user_=User()):
        super().__init__()
        self.intro_image = pg_.image.load('Rec/scrap/main_menu.png')
        self.intro_image = pg_.transform.scale(self.intro_image, (1000, 600))
        self.withdraw()

    def take_input(self, event):
        """ All <MasterMode()> children will need to have a
        <.take_input> function."""
        if event.type == pg_.MOUSEBUTTONUP:
            pos = pg_.mouse.get_pos()
            a = self.pg_button_check(pos[0], pos[1])
            if a is None:
                print('No button pushed...')
            elif a == 'Options':
                print('you get an options popup')
            else:
                self.change_mode = a

    def draw_scene(self, view):
        """ All <MasterMode()> children will need to have a
        <.draw_scene> function."""
        view.scene.blit(self.intro_image, (0, 0))
