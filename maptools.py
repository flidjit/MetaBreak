from prototyping import *
from modes import MasterMode


# ToDo :
#  * Everything.


class MapToolbar(MasterMode):
    def __init__(self, master=None, user_=User(), ui_=None):
        super().__init__(master=master, user_=user_, ui_=ui_)


    def take_input(self):
        print('take the input')


class MapMode(MapToolbar):
    def __init__(self, user_=User(), master_key=False):
        super().__init__()

    def draw_scene(self):
        print('draw the scene.')
