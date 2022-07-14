from prototyping import *
from modes import MasterMode


class ResourceTBW(MasterMode):
    def __init__(self):
        super().__init__()


class ResourceMode(ResourceTBW):
    def __init__(self, user_=User()):
        super().__init__()

    def draw_scene(self):
        print('draw the scene.')

    def take_input(self):
        print('take the input')

