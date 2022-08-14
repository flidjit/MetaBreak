from prototyping import *
from modes import MasterMode


# ToDo :
#  * Everything.


class CardMakerMode(MasterMode):
    def __init__(self, master=None, user_=User(), ui_=None):
        super().__init__(master=master, user_=user_, ui_=ui_)
        self.deck_select = tk_.Frame(self, bg='black')
        self.new_butt = tk_.Button(
            self.deck_select, bg='black', fg='white', text="New Deck")
        self.new_butt.grid(column=0, row=0)
        self.load_butt = tk_.Button(
            self.deck_select, bg='black', fg='white', text="Load Deck")
        self.load_butt.grid(column=1, row=0)
        self.deck_select.grid()
        self.save_butt = tk_.Button(
            self, bg='black', fg='white', text='Save Deck')
        self.save_butt.grid(sticky='we')
        self.deck_name_lbl = tk_.Label(
            self, bg='black', fg='pink', text="(Select a Deck)")
        self.deck_name_lbl.grid(sticky='we')
        self.card_list = tk_.Listbox(
            self, bg='black', fg='white', width=20, height=10,
            highlightcolor='pink', highlightbackground='purple')
        self.card_list.grid(sticky='we')

    def take_input(self):
        print('take the input')

    def draw_scene(self):
        print('draw the scene.')


this = CardMakerMode()
while True:
    this.update()