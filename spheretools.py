from prototyping import *
from modes import MasterMode


# ToDo :
#  * Everything.


class SphereTBW(MasterMode):
    def __init__(self, master=None, user_=User(), ui_=None):
        super().__init__()

    def take_input(self):
        print('take the input')


class SphereMode(SphereTBW):
    def __init__(self, user_=User(), master_key=False):
        super().__init__()

    def draw_scene(self):
        print('draw the scene.')
