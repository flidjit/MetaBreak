from prototyping import *
from modes import MasterMode


# ToDo :
#  * Add animation editing


class SpriteToolbar(MasterMode):
    """ SpriteMode() allows the user to transform a transparent .png
    into a custom sprite object for use within the game. """
    def __init__(self, master=None, user_=User(), ui_=None):
        super().__init__(master=master, user_=user_, ui_=ui_)
        self.section_1 = tk_.Frame(self, bg='black')
        # __________________________________________________________
        self.type_lbl = tk_.Label(
            self.section_1, bg='black', fg='white', text=' Sprite Type: ')
        self.type_lbl.grid(column=0, row=0)
        self.type_opt = [
            'Tile Set', 'Character',
            'Effect', 'UI']
        self.type_selected = tk_.StringVar()
        self.type_sel = tk_.OptionMenu(
            self.section_1, self.type_selected, *self.type_opt)
        self.type_sel.grid(column=1, row=0, sticky='we')
        # __________________________________________________________
        self.name_lbl = tk_.Label(
            self.section_1, bg='black', fg='white', text=' Sprite Name: ')
        self.name_lbl.grid(column=0, row=1)
        self.name_string = tk_.StringVar()
        self.name_ent = tk_.Entry(
            self.section_1, bg='black', fg='green', textvariable=self.name_string)
        self.name_ent.grid(column=1, row=1, sticky='we')
        # __________________________________________________________
        self.author_lbl = tk_.Label(
            self.section_1, bg='black', fg='white', text=' Author Name: ')
        self.author_lbl.grid(column=0, row=2)
        self.author_string = tk_.StringVar()
        self.author_ent = tk_.Entry(
            self.section_1, bg='black', fg='green', textvariable=self.author_string)
        self.author_ent.grid(column=1, row=2, sticky='we')
        # __________________________________________________________
        self.description_lbl = tk_.Label(
            self.section_1, bg='black', fg='white', text=' Description: ')
        self.description_lbl.grid(column=0, row=3)
        self.description_ent = tk_.Text(
            self.section_1, height=4, width=25, bg='black', fg='green')
        self.description_ent.grid(column=1, row=3)
        # __________________________________________________________
        self.date_lbl = tk_.Label(
            self.section_1, bg='black', fg='white', text=' Creation Date: ')
        self.date_lbl.grid(column=0, row=4)
        self.date = tk_.Label(
            self.section_1, bg='black', fg='white', text=' 0/0/0 ')
        self.date.grid(column=1, row=4)
        # __________________________________________________________
        self.section_1.grid(column=0, row=0, padx=10, pady=10)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.section_5 = tk_.Frame(self, bg='black')
        # __________________________________________________________
        self.cell_num_lbl = tk_.Label(
            self.section_5, bg='black', fg='white', text=' Number of Cells: ')
        self.cell_num_lbl.grid(column=0, row=0)
        # __________________________________________________________
        self.number_of_cells = tk_.StringVar()
        self.cell_number_lbl = tk_.Label(
            self.section_5, bg='black', fg='white', textvariable=self.number_of_cells)
        self.cell_number_lbl.grid(column=1, row=0)
        self.number_of_cells.set(' 000 ')
        # __________________________________________________________
        self.section_5.grid(column=0, row=4, padx=10, pady=10)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.section_6 = tk_.Frame(self, bg='black')
        # __________________________________________________________
        self.new_but = tk_.Button(self.section_6, text=' New ')
        self.new_but.grid(column=0, row=0, sticky='we')
        self.load_but = tk_.Button(self.section_6, text=' Load ')
        self.load_but.grid(column=1, row=0, sticky='we')
        self.sav_but = tk_.Button(self.section_6, text=' Save ')
        self.sav_but.grid(column=2, row=0, sticky='we')
        self.new_but = tk_.Button(self.section_6, text=' Quit ')
        self.new_but.grid(column=3, row=0, sticky='we')
        # __________________________________________________________
        self.section_6.grid(column=0, row=5, padx=10, pady=10)
        self.grid()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.filename = None
        self.this_sprite = Sprite()


class SpriteMode(SpriteToolbar):
    super().__init__()

    def take_input(self, event):
        print(event)

    def draw_scene(self, view):
        """ Draw the sprite to the screen. """
        if self.this_sprite.image_:
            view.scene.blit(self.this_sprite.image_, (0, 0))

    def new_sprite(self, *args):
        """ Create a new sprite. """
        self.this_sprite = Sprite()
        self.filename = filedialog.askopenfilename(initialdir='Rec/Sprites/New')
        self.this_sprite.image = pg_.image.load(self.filename).convert_alpha()
        with open(self.filename, 'rb') as img:
            img = img.read()
            self.this_sprite.image_string = base64.b64encode(img)
        self.ready_state = True
        self.apply_to_form()
        self.ready_state = False

    def save_sprite(self, file_location='Rec/Sprites/', extension='.spx1'):
        """ Save the sprite to file. """
        self.apply_to_sprite()
        ts = self.this_sprite.image
        self.this_sprite.image = None
        save_file = open(file_location+self.this_sprite.name_+extension, 'wb')
        pickle.dump(self.this_sprite, save_file)
        save_file.close()
        self.this_sprite.image = ts

    def cell_grid(self, rows=1, columns=1):
        """ Add cells to the sprite. """
        if self.this_sprite.image_:
            self.this_sprite.cell_size_x_ = int(
                self.this_sprite.image_.get_width() / columns)
            self.this_sprite.cell_size_y_ = int(
                self.this_sprite.image_.get_height() / rows)
            self.this_sprite.cells_ = []
            for i in range(rows):
                for j in range(columns):
                    self.this_sprite.cells_.append(
                        (j*self.this_sprite.cell_size_x_,
                         i*self.this_sprite.cell_size_y_,
                         self.this_sprite.cell_size_x_,
                         self.this_sprite.cell_size_y_))

    def apply_to_sprite(self):
        """ Apply information contained in the form to the sprite."""
        self.this_sprite.name = self.name_string.get()
        self.this_sprite.artist = self.author_string.get()
        self.this_sprite.description = self.description_ent.get(1.0, tk_.END)

    def apply_to_form(self):
        """ Apply information contained in the sprite to the form. """
        self.name_string.set(self.this_sprite.name_)
        self.author_string.set(self.this_sprite.creator_)
        self.description_ent.delete(1.0, tk_.END)
        self.description_ent.insert(tk_.END, self.this_sprite.description_)