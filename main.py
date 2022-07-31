from modes import *
from gmtools import GmMode
from playertools import PlayerMode
from tutorialtools import TutorialMode
from spritetools import SpriteMode
from spheretools import SphereMode


#  ToDo:
#    * Add pygame UI functionality.
#    * Add popup functionality.
#    * Add Mode switching functionality.
#    ---------------------------------
#    (In this order)
#    * Begin MapMode()
#    * Begin SphereMode()
#    * Begin PlayerMode()
#    * Begin GmMode()
#    * Begin TutorialMode()
#    ---------------------------------
#    * Finish SpriteMode()


class Camera:
    """This object is to be placed in the ViewPort() object.
    Tracks the relative location of the viewer."""
    def __init__(self, x=10, y=10):
        self.location = [x, y]
        self.target = [x, y]

    def update(self):
        """If the camera is not where it should be, slowly
        and smoothly move it towards the correct location."""
        if self.location != self.target:
            print('Ease the camera towards the target.')


class ViewPort:
    """ This object represents a pygame display window.
    All images to be displayed are added to the <self.scene>
    object buffer to be handled by the MasterMode(), and MainGame()
    objects, and displayed by this ViewPort() object."""
    def __init__(self):
        pg_.init()
        pg_.font.init()
        pg_.display.set_caption("Silver Cord Project")
        self.camera = Camera()
        self.scene = pg_.display.set_mode((1280, 720))
        self.clock = pg_.time.Clock()
        self.fps = 30

    def update(self):
        """ Display all buffered images to the screen.
        Do this <self.fps> times per second."""
        pg_.display.flip()
        self.clock.tick(self.fps)


# --------------------------------------------------


class MainGame:
    """ The invisible game engine, which contains both
    tkinter windows, and pygame functionality. This
    object drives the motion of the game, and cascades
    downwards updates to its child objects. It sends
    down the <self.view> object and the <self.mode_>
    object and it's children add images to the buffer
    before being sent back up to flip the buffer to the
    screen. <self.mode_> is a <MasterMode()> type object
    or one of its children."""
    def __init__(self):
        self.root = tk_.Tk()
        self.root.withdraw()
        self.view = ViewPort()
        self.mode_ = SpriteMode()

    def update(self):
        """ Begin the update() cascade."""
        self.check_mode()
        self.view.camera.update()
        self.view.scene.fill((10, 0, 10))
        self.mode_.update()
        self.mode_.draw_scene(self.view)
        self.view.update()

    def check_mode(self):
        """ Check to see if the <self.mode_> wants to be
        destroyed and replaced with a different type of
        <MasterMode()> object. The mode will place a string,
        in <self.mode_.change_mode> if it wants to be
        destroyed. By default this variable will be <None>"""
        if self.mode_.change_mode:
            usr = self.mode_.user_
            if self.mode_.change_mode == 'Player':
                self.mode_.destroy()
                self.mode_ = PlayerMode(user_=usr)
            # ---------------------------------------------
            if self.mode_.change_mode == 'GM':
                self.mode_.destroy()
                self.mode_ = GmMode(user_=usr)
            # ---------------------------------------------
            if self.mode_.change_mode == 'Sphere':
                self.mode_.destroy()
                self.mode_ = SphereMode(user_=usr)
            # ---------------------------------------------
            if self.mode_.change_mode == 'Title':
                self.mode_.destroy()
                self.mode_ = TitleMode(user_=usr)
            # ---------------------------------------------
            if self.mode_.change_mode == 'Tutorial':
                self.mode_.destroy()
                self.mode_ = TutorialMode(user_=usr)
            # ---------------------------------------------
            if self.mode_.change_mode == 'Quit':
                pg_.quit()
                sys.exit()


M_T = MainGame()


while True:
    for event in pg_.event.get():
        if event.type == QUIT:
            pg_.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            M_T.mode_.take_input(event)
    M_T.update()

