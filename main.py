from prototyping import *
from resourcetools import ResourceMode
from gmtools import GmMode
from playertools import PlayerMode
from tutorialtools import TutorialMode


class Camera:
    def __init__(self, x=10, y=10):
        self.location = [x, y]
        self.target = [x, y]

    def update(self):
        print('Ease the camera towards the target.')


class ViewPort:
    def __init__(self):
        """ This object represents a pygame display window."""
        pg_.init()
        pg_.font.init()
        pg_.display.set_caption("MetaBreak")
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
        self.mode_ = None
        self.next_mode = ''

    def update(self):
        self.view.camera.update()
        # kill the toolbar when you are done with it.
        if self.mode_.swap_modes:
            m = self.mode_.swap_modes
            self.mode_.destroy()
            if m == "GM":
                self.mode_ = GmMode()
            elif m == "Player":
                self.mode_ = PlayerMode()
            elif m == "Resource":
                self.mode_ = ResourceMode()
            elif m == "Tutorial":
                self.mode_ = TutorialMode()

        # fill the scene with visual information
        # and update the toolbar.
        self.view.scene.fill((10, 0, 10))
        if self.mode_:
            self.mode_.update(self.view)
        # show the title screen if there is no toolbar.
        else:
            print('draw the title scene.')
        # Buttons : Host Game, Join Game,
        #           Campaign Editor, Sprite Editor, Sphere Editor,
        #           Options, Quit
        self.view.update()
