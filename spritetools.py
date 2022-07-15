from prototyping import *
from modes import MasterMode


# ToDo :
#  * Add animation editing
#  * finish SpriteMode().set_access


class SpriteMode(MasterMode):
    def __init__(self, master=None, user_=User(), ui_=None):
        super().__init__(master=master)
        self.section_1 = tk_.Frame(self, bg='black')
        # __________________________________________________________
        self.type_lbl = tk_.Label(
            self.section_1, bg='black', fg='white', text=' Sprite Type: ')
        self.type_lbl.grid(column=0, row=0)
        self.type_opt = [
            'Tile Set', 'Character Sprite', 'Effect', 'UI Element']
        self.type_selected = tk_.StringVar()
        self.type_sel = tk_.OptionMenu(
            self.section_1, self.type_selected, *self.type_opt, command=self.set_access)
        self.type_selected.set(' --- ')
        self.type_sel.grid(column=1, row=0, sticky='we')
        # __________________________________________________________
        self.name_lbl = tk_.Label(
            self.section_1, bg='black', fg='white', text=' Sprite Name: ')
        self.name_lbl.grid(column=0, row=1)
        self.name_ent = tk_.Entry(
            self.section_1, bg='black', fg='green')
        self.name_ent.grid(column=1, row=1, sticky='we')
        # __________________________________________________________
        self.author_lbl = tk_.Label(
            self.section_1, bg='black', fg='white', text=' Author Name: ')
        self.author_lbl.grid(column=0, row=2)
        self.author_ent = tk_.Entry(
            self.section_1, bg='black', fg='green')
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
        # __________________________________________________________
        self.section_2 = tk_.Frame(self, bg='black')
        # __________________________________________________________
        self.row_num_lbl = tk_.Label(
            self.section_2, bg='black', fg='white', text=' # of Rows: ')
        self.row_num_lbl.grid(column=0, row=0)
        self.row_number = tk_.StringVar()
        self.row_num_sbx = ttk.Spinbox(
            self.section_2, width=3, from_=1, to=99,
            textvariable=self.row_number)
        self.row_num_sbx.grid(column=1, row=0)
        self.row_num_sbx.set('1')
        # __________________________________________________________
        self.col_num_lbl = tk_.Label(
            self.section_2, bg='black', fg='white', text=' # of Columns: ')
        self.col_num_lbl.grid(column=2, row=0)
        self.col_number = tk_.StringVar()
        self.col_num_sbx = ttk.Spinbox(
            self.section_2, width=3, from_=1, to=99,
            textvariable=self.row_number)
        self.col_num_sbx.grid(column=3, row=0)
        self.col_num_sbx.set('1')
        # __________________________________________________________
        self.section_2.grid(column=0, row=1, padx=10, pady=10)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.section_3 = tk_.Frame(self, bg='black')
        # __________________________________________________________
        self.con_x_lbl = tk_.Label(
            self.section_3, bg='black', fg='white', text=' Contact Point -   X: ')
        self.con_x_lbl.grid(column=0, row=0)
        self.con_x_num = tk_.StringVar()
        self.con_x_sbx = ttk.Spinbox(
            self.section_3, width=3, from_=1, to=500,
            textvariable=self.row_number)
        self.con_x_sbx.grid(column=1, row=0)
        self.con_x_sbx.set('1')
        # __________________________________________________________
        self.con_y_lbl = tk_.Label(
            self.section_3, bg='black', fg='white', text='   Y: ')
        self.con_y_lbl.grid(column=2, row=0)
        self.con_y_num = tk_.StringVar()
        self.con_y_sbx = ttk.Spinbox(
            self.section_3, width=3, from_=1, to=500,
            textvariable=self.con_y_num)
        self.con_y_sbx.grid(column=3, row=0)
        self.con_y_sbx.set('1')
        # __________________________________________________________
        self.section_3.grid(column=0, row=2, padx=10, pady=10)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.section_4 = tk_.Frame(self, bg='black')
        # __________________________________________________________
        self.tile_off_lbl = tk_.Label(
            self.section_4, bg='black', fg='white', text=' Tile offsets - ')
        self.tile_off_lbl.grid(column=0, row=0, columnspan=6)
        # __________________________________________________________
        self.tile_off_x_lbl = tk_.Label(
            self.section_4, bg='black', fg='white', text='   X: ')
        self.tile_off_x_lbl.grid(column=0, row=1)
        self.tile_off_x_num = tk_.StringVar()
        self.tile_off_x_sbx = ttk.Spinbox(
            self.section_4, width=3, from_=1, to=500,
            textvariable=self.tile_off_x_num)
        self.tile_off_x_sbx.grid(column=1, row=1)
        self.tile_off_x_sbx.set('1')
        # __________________________________________________________
        self.tile_off_y_lbl = tk_.Label(
            self.section_4, bg='black', fg='white', text='   Y: ')
        self.tile_off_y_lbl.grid(column=2, row=1)
        self.tile_off_y_num = tk_.StringVar()
        self.tile_off_y_sbx = ttk.Spinbox(
            self.section_4, width=3, from_=1, to=500,
            textvariable=self.tile_off_y_num)
        self.tile_off_y_sbx.grid(column=3, row=1)
        self.tile_off_y_sbx.set('1')
        # __________________________________________________________
        self.tile_off_z_lbl = tk_.Label(
            self.section_4, bg='black', fg='white', text='   Z: ')
        self.tile_off_z_lbl.grid(column=4, row=1)
        self.tile_off_z_num = tk_.StringVar()
        self.tile_off_z_sbx = ttk.Spinbox(
            self.section_4, width=3, from_=1, to=500,
            textvariable=self.tile_off_z_num)
        self.tile_off_z_sbx.grid(column=5, row=1)
        self.tile_off_z_sbx.set('1')
        # __________________________________________________________
        self.section_4.grid(column=0, row=3, padx=10, pady=10)
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
        self.cell_siz_lbl = tk_.Label(
            self.section_5, bg='black', fg='white', text=' Size of Cells: ')
        self.cell_siz_lbl.grid(column=0, row=1)
        # __________________________________________________________
        self.size_of_cells = tk_.StringVar()
        self.cell_size_lbl = tk_.Label(
            self.section_5, bg='black', fg='white', textvariable=self.size_of_cells)
        self.cell_size_lbl.grid(column=1, row=1)
        self.size_of_cells.set(' 000 ')
        # __________________________________________________________
        self.section_5.grid(column=0, row=4, padx=10, pady=10)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.section_6 = tk_.Frame(self, bg='black')
        # __________________________________________________________
        self.new_but = tk_.Button(self.section_6, text=' New ',
                                  command=self.new_sprite)
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
        # __________________________________________________________
        self.ready_state = True
        self.set_access()
        # __________________________________________________________
        self.this_sprite = Sprite()
        self.filename = None

    def set_access(self, *args):
        if self.ready_state:
            self.type_sel.config(state=tk_.DISABLED)
            self.type_lbl.config(fg='grey4')
            self.name_ent.config(state=tk_.DISABLED)
            self.name_lbl.config(fg='grey4')
            self.description_ent.config(state=tk_.DISABLED)
            self.description_lbl.config(fg='grey4')
            self.date_lbl.config(fg='grey4')
            self.date.config(fg='grey4')
            self.author_ent.config(state=tk_.DISABLED)
            self.author_lbl.config(fg='grey4')
            self.row_num_sbx.config(state=tk_.DISABLED)
            self.row_num_lbl.config(fg='grey4')
            self.col_num_sbx.config(state=tk_.DISABLED)
            self.col_num_lbl.config(fg='grey4')
            self.con_x_sbx.config(state=tk_.DISABLED)
            self.con_x_lbl.config(fg='grey4')
            self.con_y_sbx.config(state=tk_.DISABLED)
            self.con_y_lbl.config(fg='grey4')
            self.tile_off_lbl.config(fg='grey4')
            self.tile_off_x_sbx.config(state=tk_.DISABLED)
            self.tile_off_x_lbl.config(fg='grey4')
            self.tile_off_y_sbx.config(state=tk_.DISABLED)
            self.tile_off_y_lbl.config(fg='grey4')
            self.tile_off_z_sbx.config(state=tk_.DISABLED)
            self.tile_off_z_lbl.config(fg='grey4')
            self.cell_num_lbl.config(fg='grey4')
            self.cell_number_lbl.config(fg='grey4')
            self.cell_siz_lbl.config(fg='grey4')
            self.cell_size_lbl.config(fg='grey4')

        else:
            if self.type_selected.get() == 'Tile Set':
                self.type_sel.config(state=tk_.NORMAL)
                self.type_lbl.config(fg='white')
                self.name_ent.config(state=tk_.DISABLED)
                self.name_lbl.config(fg='grey4')
                self.description_ent.config(state=tk_.DISABLED)
                self.description_lbl.config(fg='grey4')
                self.date_lbl.config(fg='grey4')
                self.date.config(fg='grey4')
                self.author_ent.config(state=tk_.DISABLED)
                self.author_lbl.config(fg='grey4')
                self.row_num_sbx.config(state=tk_.DISABLED)
                self.row_num_lbl.config(fg='grey4')
                self.col_num_sbx.config(state=tk_.DISABLED)
                self.col_num_lbl.config(fg='grey4')
                self.con_x_sbx.config(state=tk_.DISABLED)
                self.con_x_lbl.config(fg='grey4')
                self.con_y_sbx.config(state=tk_.DISABLED)
                self.con_y_lbl.config(fg='grey4')
                self.tile_off_lbl.config(fg='grey4')
                self.tile_off_x_sbx.config(state=tk_.DISABLED)
                self.tile_off_x_lbl.config(fg='grey4')
                self.tile_off_y_sbx.config(state=tk_.DISABLED)
                self.tile_off_y_lbl.config(fg='grey4')
                self.tile_off_z_sbx.config(state=tk_.DISABLED)
                self.tile_off_z_lbl.config(fg='grey4')
                self.cell_num_lbl.config(fg='grey4')
                self.cell_number_lbl.config(fg='grey4')
                self.cell_siz_lbl.config(fg='grey4')
                self.cell_size_lbl.config(fg='grey4')

            elif self.type_selected.get() == 'Character Sprite':
                self.type_sel.config(state=tk_.DISABLED)
                self.type_lbl.config(fg='grey4')
                self.name_ent.config(state=tk_.DISABLED)
                self.name_lbl.config(fg='grey4')
                self.description_ent.config(state=tk_.DISABLED)
                self.description_lbl.config(fg='grey4')
                self.date_lbl.config(fg='grey4')
                self.date.config(fg='grey4')
                self.author_ent.config(state=tk_.DISABLED)
                self.author_lbl.config(fg='grey4')
                self.row_num_sbx.config(state=tk_.DISABLED)
                self.row_num_lbl.config(fg='grey4')
                self.col_num_sbx.config(state=tk_.DISABLED)
                self.col_num_lbl.config(fg='grey4')
                self.con_x_sbx.config(state=tk_.DISABLED)
                self.con_x_lbl.config(fg='grey4')
                self.con_y_sbx.config(state=tk_.DISABLED)
                self.con_y_lbl.config(fg='grey4')
                self.tile_off_lbl.config(fg='grey4')
                self.tile_off_x_sbx.config(state=tk_.DISABLED)
                self.tile_off_x_lbl.config(fg='grey4')
                self.tile_off_y_sbx.config(state=tk_.DISABLED)
                self.tile_off_y_lbl.config(fg='grey4')
                self.tile_off_z_sbx.config(state=tk_.DISABLED)
                self.tile_off_z_lbl.config(fg='grey4')
                self.cell_num_lbl.config(fg='grey4')
                self.cell_number_lbl.config(fg='grey4')
                self.cell_siz_lbl.config(fg='grey4')
                self.cell_size_lbl.config(fg='grey4')

            elif self.type_selected.get() == 'UI Element':
                self.type_sel.config(state=tk_.DISABLED)
                self.type_lbl.config(fg='grey4')
                self.name_ent.config(state=tk_.DISABLED)
                self.name_lbl.config(fg='grey4')
                self.description_ent.config(state=tk_.DISABLED)
                self.description_lbl.config(fg='grey4')
                self.date_lbl.config(fg='grey4')
                self.date.config(fg='grey4')
                self.author_ent.config(state=tk_.DISABLED)
                self.author_lbl.config(fg='grey4')
                self.row_num_sbx.config(state=tk_.DISABLED)
                self.row_num_lbl.config(fg='grey4')
                self.col_num_sbx.config(state=tk_.DISABLED)
                self.col_num_lbl.config(fg='grey4')
                self.con_x_sbx.config(state=tk_.DISABLED)
                self.con_x_lbl.config(fg='grey4')
                self.con_y_sbx.config(state=tk_.DISABLED)
                self.con_y_lbl.config(fg='grey4')
                self.tile_off_lbl.config(fg='grey4')
                self.tile_off_x_sbx.config(state=tk_.DISABLED)
                self.tile_off_x_lbl.config(fg='grey4')
                self.tile_off_y_sbx.config(state=tk_.DISABLED)
                self.tile_off_y_lbl.config(fg='grey4')
                self.tile_off_z_sbx.config(state=tk_.DISABLED)
                self.tile_off_z_lbl.config(fg='grey4')
                self.cell_num_lbl.config(fg='grey4')
                self.cell_number_lbl.config(fg='grey4')
                self.cell_siz_lbl.config(fg='grey4')
                self.cell_size_lbl.config(fg='grey4')

            elif self.type_selected.get() == 'Effect':
                self.type_sel.config(state=tk_.DISABLED)
                self.type_lbl.config(fg='grey4')
                self.name_ent.config(state=tk_.DISABLED)
                self.name_lbl.config(fg='grey4')
                self.description_ent.config(state=tk_.DISABLED)
                self.description_lbl.config(fg='grey4')
                self.date_lbl.config(fg='grey4')
                self.date.config(fg='grey4')
                self.author_ent.config(state=tk_.DISABLED)
                self.author_lbl.config(fg='grey4')
                self.row_num_sbx.config(state=tk_.DISABLED)
                self.row_num_lbl.config(fg='grey4')
                self.col_num_sbx.config(state=tk_.DISABLED)
                self.col_num_lbl.config(fg='grey4')
                self.con_x_sbx.config(state=tk_.DISABLED)
                self.con_x_lbl.config(fg='grey4')
                self.con_y_sbx.config(state=tk_.DISABLED)
                self.con_y_lbl.config(fg='grey4')
                self.tile_off_lbl.config(fg='grey4')
                self.tile_off_x_sbx.config(state=tk_.DISABLED)
                self.tile_off_x_lbl.config(fg='grey4')
                self.tile_off_y_sbx.config(state=tk_.DISABLED)
                self.tile_off_y_lbl.config(fg='grey4')
                self.tile_off_z_sbx.config(state=tk_.DISABLED)
                self.tile_off_z_lbl.config(fg='grey4')
                self.cell_num_lbl.config(fg='grey4')
                self.cell_number_lbl.config(fg='grey4')
                self.cell_siz_lbl.config(fg='grey4')
                self.cell_size_lbl.config(fg='grey4')
            print('Set enabled/disabled state according to sprite type')

    def take_input(self, event):
        print('take the input')

    def draw_scene(self, view):
        if self.this_sprite.image:
            view.scene.blit(self.this_sprite.image, (0, 0))
        print('draw the scene.')

    def new_sprite(self, *args):
        self.this_sprite = Sprite()
        self.filename = filedialog.askopenfilename()
        self.this_sprite.image = pg_.image.load(self.filename).convert_alpha()
        with open(self.filename, 'rb') as img:
            img = img.read()
            self.this_sprite.image_string = base64.b64encode(img)
        self.ready_state = False
        self.type_sel.config(state=tk_.NORMAL)
        self.type_lbl.config(fg='white')
        self.set_access()

    def save_sprite(self):
        self.apply_to_sprite()
        ts = self.this_sprite.image
        self.this_sprite.image = None
        save_file = open('Sprites/'+self.this_sprite.name+'.sptx', 'wb')
        pickle.dump(self.this_sprite, save_file)
        save_file.close()
        self.this_sprite.image = ts

    def make_cells(self):
        for i in range(int(self.this_sprite.num_of_rows)):
            for j in range(int(self.this_sprite.num_of_cols)):
                self.this_sprite.cells.append(
                    (j*self.this_sprite.cell_size[0],
                     i*self.this_sprite.cell_size[1],
                     self.this_sprite.cell_size[0],
                     self.this_sprite.cell_size[1]))

    def calc_dim(self, cols=12, rows=6):
        self.this_sprite.cell_size[0] = int(self.this_sprite.image.get_width() / cols)
        self.this_sprite.cell_size[1] = int(self.this_sprite.image.get_height() / rows)
        self.this_sprite.num_of_cols = cols
        self.this_sprite.num_of_rows = rows
        self.this_sprite.num_of_cells = rows*cols

    def apply_to_sprite(self):
        self.this_sprite.name = self.name_ent.get()
        self.this_sprite.artist = self.author_ent.get()
        self.this_sprite.description = self.description_ent.get(1.0, pg_.END)
        self.this_sprite.cell_size = [
            int(self.col_num_sbx.get()), int(self.row_num_sbx.get())]
        self.this_sprite.cell_size[0] = int(self.col_num_sbx.get())
        self.this_sprite.contact_point = [
            int(self.con_x_sbx.get()), int(self.con_y_sbx.get())]
        self.calc_dim()
        self.make_cells()

    def apply_to_form(self):
        self.name_ent.delete(1, pg_.END)
        self.name_ent.insert(pg_.END, self.this_sprite.name)
        self.author_ent.delete(1, pg_.END)
        self.author_ent.insert(pg_.END, self.this_sprite.artist)
        self.description_ent.delete(1.0, pg_.END)
        self.description_ent.insert(pg_.END, self.this_sprite.description)
        self.col_num_sbx.set(self.this_sprite.num_of_cols)
        self.row_num_sbx.set(self.this_sprite.num_of_rows)
        self.con_x_sbx.set(self.this_sprite.contact_point[0])
        self.con_y_sbx.set(self.this_sprite.contact_point[1])
        cs_1 = str(self.this_sprite.cell_size[0])
        cs_2 = str(self.this_sprite.cell_size[1])
        self.size_of_cells = ' [ '+cs_1+'x'+cs_2+' px ]'
        self.number_of_cells = str(self.this_sprite.num_of_cells)
