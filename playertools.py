from prototyping import *
from modes import MasterMode


# ToDo :
#  * Everything.


class PlayerMode(MasterMode):
    def __init__(self, master=None, user_=User(), ui_=None):
        super().__init__()

    def take_input(self):
        print('take the input')

    def draw_scene(self):
        print('draw the scene.')
