from prototyping import *
from modes import MasterMode


# ToDo :
#  * ???.


class TutorialTBW(MasterMode):
    def __init__(self):
        super().__init__()

    def take_input(self):
        print('take the input')


class TutorialMode(TutorialTBW):
    def __init__(self, user_=User()):
        super().__init__()

    def draw_scene(self):
        print('draw the scene.')
