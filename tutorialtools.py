from prototyping import *
from modes import MasterMode


# ToDo :
#  * Everything.


class TutorialTBW(MasterMode):
    def __init__(self, master=None, user_=User(), ui_=None, master_key=False):
        super().__init__()

    def take_input(self):
        print('take the input')


class TutorialMode(TutorialTBW):
    def __init__(self, user_=User(), master_key=False):
        super().__init__()

    def draw_scene(self):
        print('draw the scene.')
