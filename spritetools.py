from prototyping import *
from modes import MasterMode
from celldata import cell_data_


# ToDo :
#  * Create at least 1 PGui() object, so I can start making the
#    ui system work.
#  * Activate/Deactivate widget functionality.
#  * Build GridEntry() form.
#  * Add animation editing


class UserEntry:
    def __init__(self, master=None):
        self.window = tk_.Toplevel(master, bg='black')
        self.n_label = tk_.Label(self.window, bg='black', fg='white', text=' Name the sprite : ')
        self.n_label.grid(row=0, column=0)
        self.n_string = tk_.StringVar()
        self.n_entry = tk_.Entry(self.window, bg='black', fg='green', textvariable=self.n_string)
        self.n_entry.grid(row=0, column=1, columnspan=2)
        self.ok_btn = tk_.Button(self.window, bg='black', fg='pink', text=' OK ',
                                 command=self.window.destroy)
        self.ok_btn.grid(row=3, column=1, sticky='we')
        self.nope_btn = tk_.Button(self.window, bg='black', fg='pink', text=' Cancel ')
        self.nope_btn.grid(row=3, column=2, sticky='we')
        self.window.grid()

    def adopt(self, sprite=Sprite()):
        self.window.deiconify()
        self.window.wait_window()
        sprite.name_ = self.n_string.get()
        return sprite


class GridEntry:
    def __init__(self, master=None):
        self.window = tk_.Toplevel(master)
        self.label = tk_.Label(self.window, bg='black', fg='white', text='Text')
        self.label.grid()
        self.window.grid()

    def adopt(self, sprite=Sprite()):
        self.window.deiconify()
        self.window.wait_window()
        sprite.name_ = 'Ben'
        return sprite


class SpriteToolbar(MasterMode):
    """ SpriteMode() allows the user to transform a transparent .png
    into a custom sprite object for use within the game. """
    def __init__(self, master=None, user_=User(), ui_=None):
        super().__init__(master=master, user_=user_, ui_=ui_)
        self.s_1 = tk_.Frame(self, bg='black')
        # __________________________________________________________
        self.name_ = tk_.StringVar()
        self.nam_s_lbl = tk_.Label(self.s_1, bg='black', fg='white',
                                   text=' Sprite Name: ')
        self.nam_s_lbl.grid(column=0, row=1)
        self.nam_lbl = tk_.Label(self.s_1, bg='black', fg='green',
                                 textvariable=self.name_)
        self.nam_lbl.grid(column=1, row=1, sticky='we')
        # __________________________________________________________
        self.author_ = tk_.StringVar()
        self.ath_s_lbl = tk_.Label(self.s_1, bg='black', fg='white',
                                   text=' Author: ')
        self.ath_s_lbl.grid(column=0, row=2)
        self.ath_lbl = tk_.Label(self.s_1, bg='black', fg='green',
                                 textvariable=self.author_)
        self.ath_lbl.grid(column=1, row=2, sticky='we')
        # __________________________________________________________
        self.date_ = tk_.StringVar()
        self.dt_s_lbl = tk_.Label(self.s_1, bg='black', fg='white',
                                  text=' Creation Date: ')
        self.dt_s_lbl.grid(column=0, row=4)
        self.dt_lbl2 = tk_.Label(self.s_1, bg='black', fg='white',
                                 textvariable=self.date_)
        self.dt_lbl2.grid(column=1, row=4)
        # __________________________________________________________
        self.s_1.grid(column=0, row=0, padx=10, pady=10)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.s_2 = tk_.Frame(self, bg='black')
        # __________________________________________________________
        self.cell_number_ = tk_.StringVar()
        self.cell_num_lbl = tk_.Label(self.s_2, bg='black', fg='white',
                                      textvariable=self.cell_number_)
        self.cell_num_lbl.grid(column=1, row=0)
        # __________________________________________________________
        self.s_2.grid(column=0, row=4, padx=10, pady=10)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.s_3 = tk_.Frame(self, bg='black')
        # __________________________________________________________
        self.type_options_ = ['Tile Set', 'Custom Grid', 'Character', 'PGui']
        self.type_selected_ = tk_.StringVar()
        self.typ_s_lbl = tk_.Label(self.s_3, bg='black', fg='white',
                                   text=' Sprite Type: ')
        self.typ_s_lbl.grid(column=0, row=0)
        self.typ_sel = tk_.OptionMenu(self.s_3, self.type_selected_,
                                      *self.type_options_)
        self.typ_sel.grid(column=1, row=0, sticky='we', columnspan=6)
        # __________________________________________________________
        self.regrid_ = tk_.Button(self.s_3, text=' Edit Cell Grid ')
        self.regrid_.grid(column=0, row=1, columnspan=4, sticky='we')
        self.new_but = tk_.Button(self.s_3, text=' New ')
        self.new_but.grid(column=0, row=2, sticky='we')
        self.lod_but = tk_.Button(self.s_3, text=' Load ')
        self.lod_but.grid(column=1, row=2, sticky='we')
        self.sav_but = tk_.Button(self.s_3, text=' Save ')
        self.sav_but.grid(column=2, row=2, sticky='we')
        self.qit_but = tk_.Button(self.s_3, text=' Quit ')
        self.qit_but.grid(column=3, row=2, sticky='we')
        # __________________________________________________________
        self.s_3.grid(column=0, row=5, padx=10, pady=10)
        self.grid()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class SpriteMode(SpriteToolbar):
    """ SpriteMode allows you to create and edit sprites. """
    def __init__(self):
        super().__init__(master=None, user_=User(), ui_=PGui())
        self.working_sprite_ = Sprite()
        self.base_folder_ = 'Rec/Sprites/'
        self.type_selected_.set(' Select a Sprite Type. ')
        self.name_.set(' ... ')
        self.author_.set(self.user_.screen_name_)
        self.date_.set(' 0/0/0 ')
        self.cell_number_.set(' 000 ')
        self.new_but.config(command=self.new_sprite)
        self.sav_but.config(command=self.save_sprite)
        self.lod_but.config(command=self.load_sprite)

    def take_input(self, event):
        print(event)

    def draw_scene(self, view):
        """ Draw the sprite to the screen. """
        if self.ui_.image_:
            view.scene.blit(self.ui_.background_img_, (0, 0))
        if self.working_sprite_:
            if self.working_sprite_.image_:
                view.scene.blit(self.working_sprite_.image_, (0, 0))
        if self.working_sprite_.cells_:
            for i in self.working_sprite_.cells_:
                pg_.draw.rect(view.scene, 'red', (i[0], i[1], i[2], i[3]), 1)
        else:
            self.working_sprite_ = Sprite()

    def new_sprite(self, *args):
        """ Create a new sprite. """
        try:
            type_ = self.type_selected_.get()
            if type_ == 'PGui':
                self.working_sprite_ = PGui()
                self.working_sprite_.type_ = type_
            elif type_ == 'Tile Set':
                self.working_sprite_ = TileSet()
                self.working_sprite_.type_ = type_
            elif type_ == 'Character':
                self.working_sprite_ = Character()
                self.working_sprite_.type_ = type_
            elif type_ == 'Custom Grid':
                self.working_sprite_ = Sprite()
                self.working_sprite_.type_ = type_
            else:
                print('Not a valid sprite type.')
            self.working_sprite_ = UserEntry(self).adopt(self.working_sprite_)
            self.working_sprite_.creation_date_ = str(date.today())
            self.working_sprite_.creator_ = self.user_.screen_name_
            dir_ = self.base_folder_ + type_
            image_filename_ = filedialog.askopenfilename(initialdir=dir_)
            self.working_sprite_.image_ = pg_.image.load(image_filename_).convert_alpha()
            with open(image_filename_, 'rb') as img:
                img = img.read()
                self.working_sprite_.image_string_ = base64.b64encode(img)
            self.apply_to_form()
        except TypeError:
            print(' Failed. ')

    def save_sprite(self):
        """ Save the sprite to file. """
        self.apply_to_sprite()
        ts = self.working_sprite_.image_
        self.working_sprite_.image_ = None
        type_ = self.working_sprite_.type_
        sprite_filename_ = self.base_folder_+type_+'/'
        sprite_filename_ += self.working_sprite_.name_+sprite_types[type_][0]
        save_file = open(sprite_filename_, 'wb')
        pickle.dump(self.working_sprite_, save_file)
        save_file.close()
        self.working_sprite_.image = ts

    def load_sprite(self):
        sprite_filename_ = filedialog.askopenfilename()
        self.working_sprite_ = self.acquire_sprite_object(sprite_filename_, True)

    def cell_grid(self, rows=1, columns=1):
        """ Add cells to the sprite. """
        if self.working_sprite_.image_:
            self.working_sprite_.cell_size_x_ = int(
                self.working_sprite_.image_.get_width() / columns)
            self.working_sprite_.cell_size_y_ = int(
                self.working_sprite_.image_.get_height() / rows)
            self.working_sprite_.cells_ = []
            for i in range(rows):
                for j in range(columns):
                    self.working_sprite_.cells_.append(
                        (j*self.working_sprite_.cell_size_x_,
                         i*self.working_sprite_.cell_size_y_,
                         self.working_sprite_.cell_size_x_,
                         self.working_sprite_.cell_size_y_))

    def apply_to_sprite(self):
        """ Apply information contained in the form to the sprite."""
        self.working_sprite_.name_ = self.name_.get()
        self.working_sprite_.artist_ = self.author_.get()
        self.working_sprite_.creation_date_ = self.date_.get()

    def apply_to_form(self):
        """ Apply information contained in the sprite to the form. """
        self.name_.set(self.working_sprite_.name_)
        self.author_.set(self.working_sprite_.creator_)
        self.date_.set(self.working_sprite_.creation_date_)
        try:
            self.cell_number_.set('# of cells: '+str(len(self.working_sprite_.cells_)))
        except TypeError:
            print('failed to calculate cell number.')
