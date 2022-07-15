from prototyping import *
from modes import MasterMode


# ToDo :
#  * ???.


class SpriteTBW(MasterMode):
    def __init__(self, master=None, user_=User(), ui_=None, master_key=False):
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
        self.type_selected.set('Tile Set')
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
            self.section_4, bg='black', fg='white', text=' X: ')
        self.tile_off_x_lbl.grid(column=0, row=1)
        self.tile_off_x_num = tk_.StringVar()
        self.tile_off_x_sbx = ttk.Spinbox(
            self.section_4, width=3, from_=1, to=500,
            textvariable=self.tile_off_x_num)
        self.tile_off_x_sbx.grid(column=1, row=1)
        self.tile_off_x_sbx.set('1')
        # __________________________________________________________
        self.tile_off_y_lbl = tk_.Label(
            self.section_4, bg='black', fg='white', text=' Y: ')
        self.tile_off_y_lbl.grid(column=2, row=1)
        self.tile_off_y_num = tk_.StringVar()
        self.tile_off_y_sbx = ttk.Spinbox(
            self.section_4, width=3, from_=1, to=500,
            textvariable=self.tile_off_y_num)
        self.tile_off_y_sbx.grid(column=3, row=1)
        self.tile_off_y_sbx.set('1')
        # __________________________________________________________
        self.tile_off_z_lbl = tk_.Label(
            self.section_4, bg='black', fg='white', text=' Y: ')
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
        self.cell_siz_lbl = tk_.Label(
            self.section_5, bg='black', fg='white', textvariable=self.size_of_cells)
        self.cell_siz_lbl.grid(column=1, row=1)
        self.size_of_cells.set(' 000 ')
        # __________________________________________________________
        self.section_5.grid(column=0, row=4, padx=10, pady=10)
        self.grid()

    def set_access(self, *args):
        if self.type_selected.get() == 'Tile Set':
            self.name_ent.config(state=tk_.NORMAL)
            self.name_lbl.config(fg='white')
            self.description_ent.config(state=tk_.NORMAL)
            self.description_lbl.config(fg='white')
            self.author_ent.config(state=tk_.NORMAL)
            self.row_num_lbl.config(fg='white')
            self.row_num_sbx.config(state=tk_.NORMAL)
            self.col_num_lbl.config(fg='white')
            self.col_num_sbx.config(state=tk_.NORMAL)
            self.con_x_lbl.config(fg='white')
            self.con_x_sbx.config(state=tk_.NORMAL)
            self.con_y_lbl.config(fg='white')
            self.con_y_sbx.config(state=tk_.NORMAL)
            self.tile_off_lbl.config(fg='white')
            self.tile_off_x_lbl.config(fg='white')
            self.tile_off_y_lbl.config(fg='white')
            self.tile_off_z_lbl.config(fg='white')
            self.tile_off_x_sbx.config(state=tk_.NORMAL)
            self.tile_off_y_sbx.config(state=tk_.NORMAL)
            self.tile_off_z_sbx.config(state=tk_.NORMAL)
        elif self.type_selected.get() == 'Character Sprite':
            self.name_ent.config(state=tk_.NORMAL)
            self.name_lbl.config(fg='white')
            self.description_ent.config(state=tk_.NORMAL)
            self.description_lbl.config(fg='white')
            self.author_ent.config(state=tk_.NORMAL)
            self.row_num_lbl.config(fg='white')
            self.row_num_sbx.config(state=tk_.NORMAL)
            self.col_num_lbl.config(fg='white')
            self.col_num_sbx.config(state=tk_.NORMAL)
            self.con_x_lbl.config(fg='white')
            self.con_x_sbx.config(state=tk_.NORMAL)
            self.con_y_lbl.config(fg='white')
            self.con_y_sbx.config(state=tk_.NORMAL)
            self.tile_off_lbl.config(fg='grey4')
            self.tile_off_x_lbl.config(fg='grey4')
            self.tile_off_y_lbl.config(fg='grey4')
            self.tile_off_z_lbl.config(fg='grey4')
            self.tile_off_x_sbx.config(state=tk_.DISABLED)
            self.tile_off_y_sbx.config(state=tk_.DISABLED)
            self.tile_off_z_sbx.config(state=tk_.DISABLED)
        if self.type_selected.get() == 'UI Element':
            self.name_ent.config(state=tk_.NORMAL)
            self.name_lbl.config(fg='white')
            self.description_ent.config(state=tk_.NORMAL)
            self.description_lbl.config(fg='white')
            self.author_ent.config(state=tk_.NORMAL)
            self.row_num_lbl.config(fg='grey4')
            self.row_num_sbx.config(state=tk_.DISABLED)
            self.col_num_lbl.config(fg='grey4')
            self.col_num_sbx.config(state=tk_.DISABLED)
            self.con_x_lbl.config(fg='grey4')
            self.con_x_sbx.config(state=tk_.DISABLED)
            self.con_y_lbl.config(fg='grey4')
            self.con_y_sbx.config(state=tk_.DISABLED)
            self.tile_off_lbl.config(fg='grey4')
            self.tile_off_x_lbl.config(fg='grey4')
            self.tile_off_y_lbl.config(fg='grey4')
            self.tile_off_z_lbl.config(fg='grey4')
            self.tile_off_x_sbx.config(state=tk_.DISABLED)
            self.tile_off_y_sbx.config(state=tk_.DISABLED)
            self.tile_off_z_sbx.config(state=tk_.DISABLED)
        if self.type_selected.get() == 'Effect':
            self.name_ent.config(state=tk_.NORMAL)
            self.name_lbl.config(fg='white')
            self.description_ent.config(state=tk_.NORMAL)
            self.description_lbl.config(fg='white')
            self.author_ent.config(state=tk_.NORMAL)
            self.row_num_lbl.config(fg='grey4')
            self.row_num_sbx.config(state=tk_.DISABLED)
            self.col_num_lbl.config(fg='grey4')
            self.col_num_sbx.config(state=tk_.DISABLED)
            self.con_x_lbl.config(fg='grey4')
            self.con_x_sbx.config(state=tk_.DISABLED)
            self.con_y_lbl.config(fg='grey4')
            self.con_y_sbx.config(state=tk_.DISABLED)
            self.tile_off_lbl.config(fg='grey4')
            self.tile_off_x_lbl.config(fg='grey4')
            self.tile_off_y_lbl.config(fg='grey4')
            self.tile_off_z_lbl.config(fg='grey4')
            self.tile_off_x_sbx.config(state=tk_.DISABLED)
            self.tile_off_y_sbx.config(state=tk_.DISABLED)
            self.tile_off_z_sbx.config(state=tk_.DISABLED)
        print('Set enabled/disabled state according to sprite type')


class SpriteMode(SpriteTBW):
    def __init__(self, user_=User(), master_key=False):
        super().__init__()

    def take_input(self, event):
        print('take the input')

    def draw_scene(self, view):
        print('draw the scene.')