from prototyping import *


# ToDo :
#  * Add MasterMode.render_iso() functionality.
#  * Add MasterMode.load_user_data() functionality.
#  * Work on MasterMode.pg_button_check().
#  * TitleMode() needs to handle art properly. Waiting for a PGui() object.


class MasterMode(tk_.Toplevel):
    """ This object represents a game mode. <MasterMode()> is the
    base class for 7 other modes, including:
    <PlayerMode()>, <GmMode()>, <TutorialMode()>, <SpriteMode()>,
    <SphereMode()>, <MapMode()>, and <TitleMode()>.
    The mode determines what gets drawn to the screen, and what
    popups are activated. All Mode objects will have a
    <.draw_scene> function that takes in the .scene buffer
    and adds images to it. """
    def __init__(self, master=None, user_=User(),
                 map_=GameMap(), ui_=PGui()):
        super().__init__(master=master, bg='black')
        self.resizable(False, False)
        self.map_ = map_
        self.ui_ = ui_
        self.ui_bg = None
        self.popup = None
        self.art_ = {}
        self.change_mode = None
        self.user_ = user_

    def prepare_art(self):
        """Load the sprites listed for this map into the <self.art_>
        dictionary, and prepare them for display."""
        st = 'Rec/Sprites/'
        if self.map_:
            if self.map_.sprite_list:
                for i in self.map_.sprite_list:
                    filename = st + 'Tile Set/' + i + '.spx1'
                    self.acquire_sprite_object(filename)
        if self.ui_:
            filename = st + 'PGui/' + self.user_.selected_theme_ + '.spx4'
            self.ui_ = self.acquire_sprite_object(filename, True)
            c = self.ui_.cells_
            self.ui_.image_.set_clip(pg_.Rect(c[0][0], c[0][1], c[0][2], c[0][3]))
            self.ui_.background_img_ = self.ui_.image_.subsurface(self.ui_.image_.get_clip())
            self.ui_.background_img_ = pg_.transform.scale(
                self.ui_.background_img_, (1280, 720))

    def acquire_sprite_object(self, filename=None, return_value_=False):
        """ Loads a custom sprite object, and convert its Sprite.image_string
        data into an image format that can be handled by pygame. """
        if filename:
            load_file = open(filename, 'rb')
            sprite = pickle.load(load_file)
            load_file.close()
            tmp_img = io.BytesIO(base64.b64decode(sprite.image_string_))
            sprite.image_string_ = None
            sprite.image_ = pg_.image.load(tmp_img)
            if return_value_:
                return sprite
            else:
                self.art_[sprite.name_] = sprite

    def save_user_data(self):
        """ Saves all user data to memory."""
        destination = open('User/'+self.user_.screen_name_+'.usr', 'wb')
        pickle.dump(self.user_, destination)
        destination.close()

    def render_iso(self):
        """ Render the <self.map_> object as isometric tiles."""
        print('render an isometric map')

    def draw_ui(self, view):
        print('draw the ui.')

    def pg_button_check(self, x, y):
        """ When the user clicks on the pygame window, this checks
        to see if the click collided with one of the buttons in
        the ui. A string containing the desired action is returned."""
        a = None
        for i in range(len(self.ui_.buttons_)):
            b = self.ui_.buttons_[i]
            if b.click_x_1 < x < b.click_x_2:
                if b.click_y_1 < y < b.click_y_2:
                    a = b.action
        print(a)
        return a


class TitleMode(MasterMode):
    """ This mode is active at startup. Allows the user to select
    among the other modes."""
    def __init__(self, user_=User(), master_key=False):
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
        view.scene.blit(self.ui_.cells_[0], (0, 0))
        self.draw_ui(view)
