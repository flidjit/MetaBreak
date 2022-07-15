from prototyping import *
from modes import MasterMode


# ToDo :
#  * ???.


class SpriteTBW(MasterMode):
    def __init__(self, master=None, user_=User(), ui_=None, master_key=False):
        super().__init__(master=master)
        self.section_1 = tk_.Frame(self, bg='black')
        # __________________________________________________________
        self.s_name = tk_.StringVar()  # <--- Edit this variable.
        self.name_lbl = tk_.Label(
            self.section_1, bg='black', fg='white', text=' Sprite Name: ')
        self.name_lbl.grid(column=0, row=0)
        self.name_ent = tk_.Entry(
            self.section_1, bg='black', fg='white', textvariable=self.s_name)
        self.s_name.set(' sprite name ')
        self.name_ent.grid(column=1, row=0)
        # __________________________________________________________
        self.s_author = tk_.StringVar()  # <--- Edit this variable.
        self.author_lbl = tk_.Label(
            self.section_1, bg='black', fg='white', text=' Author Name: ')
        self.author_lbl.grid(column=0, row=1)
        self.author_ent = tk_.Entry(
            self.section_1, bg='black', fg='white', textvariable=self.s_author)
        self.s_author.set(' author name ')
        self.author_ent.grid(column=1, row=1)
        # __________________________________________________________
        self.s_description = tk_.StringVar()  # <--- Edit this variable.
        self.description_lbl = tk_.Label(
            self.section_1, bg='black', fg='white', text=' Author Name: ')
        self.description_lbl.grid(column=0, row=1)
        self.description_ent = tk_.Text(
            self.section_1, bg='black', fg='white')
        self.s_description.set(' author name ')
        self.description_ent.grid(column=1, row=1)
        # __________________________________________________________
        self.section_1.grid(column=0, row=0)
        self.grid()


class SpriteMode(SpriteTBW):
    def __init__(self, user_=User(), master_key=False):
        super().__init__()

    def take_input(self, event):
        print('take the input')

    def draw_scene(self, view):
        print('draw the scene.')