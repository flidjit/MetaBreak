from prototyping import *
from modes import TitleMode
from resourcetools import ResourceMode
from gmtools import GmMode
from playertools import PlayerMode
from tutorialtools import TutorialMode


class Camera:
    def __init__(self, x=10, y=10):
        self.location = [x, y]
        self.target = [x, y]

    def update(self):
        if self.location != self.target:
            print('Ease the camera towards the target.')


class ViewPort:
    def __init__(self):
        """ This object represents a pygame display window."""
        pg_.init()
        pg_.font.init()
        pg_.display.set_caption("Silver Cord Project")
        self.camera = Camera()
        self.scene = pg_.display.set_mode((1000, 600))
        self.clock = pg_.time.Clock()
        self.fps = 30

    def update(self):
        pg_.display.flip()
        self.clock.tick(self.fps)


# --------------------------------------------------


class MainGame:
    def __init__(self):
        self.root = tk_.Tk()
        self.root.withdraw()
        self.view = ViewPort()
        self.user_ = None
        self.mode_ = TitleMode()

    def update(self):
        self.view.camera.update()
        self.view.scene.fill((10, 0, 10))
        self.mode_.draw_scene(self.view)
        self.mode_.update()
        self.view.update()

    def check_mode(self):
        if self.mode_.change_mode:
            if self.mode_.change_mode == 'Player':
                self.mode_.destroy()
                self.mode_ = PlayerMode()
            if self.mode_.change_mode == 'GM':
                self.mode_.destroy()
                self.mode_ = GmMode()
            if self.mode_.change_mode == 'Resource':
                self.mode_.destroy()
                self.mode_ = ResourceMode()
            if self.mode_.change_mode == 'Title':
                self.mode_.destroy()
                self.mode_ = TitleMode()

            print('change the mode')


M_T = MainGame()


while True:
    for event in pg_.event.get():
        if event.type == QUIT:
            pg_.quit()
            sys.exit()
        else:
            M_T.mode_.take_input(event)
    M_T.update()

