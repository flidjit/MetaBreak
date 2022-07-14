
class User:
    def __init__(self):
        self.screen_name = 'Name'
        self.email = '@mail.com'
        self.last_login = ''
        self.campaigns = []
        self.player_characters = []


class Character:
    def __init__(self):
        self.first_name = 'Name'
        self.last_name = 'Name'
        self.scores = {
            'Strong': 10,
            'Tough': 10,
            'Quick': 10,
            'Nimble': 10,
            'Clever': 10,
            'Pretty': 10,
            'Alert': 10}
        self.health = [10, 10]
        self.Power = [5, 5]
        self.ap = [4, 4]
        self.defence = 10
        self.attack = 2
        self.techniques = {}
        self.skills = {}
        self.portrait = None
        self.bust = None
        self.left_hand = None
        self.right_hand = None
        self.gear = {
            'Head': None,
            'Face': None,
            'Torso': None,
            'Hands': None,
            'Back': None,
            'Legs': None,
            'Feet': None}
        self.pack = []
        self.constant_effects = {}
        self.current_location = None
        self.description = {
            'Eye Color': 'Color',
            'Hair Color': 'Color',
            'Hair Style': 'Style',
            'Skin Color': 'Color',
            'Age': 'Number',
            'Build': 'Structure',
            'Gender': 'Gender'}
        self.notes = []


class Sheet:
    def __init__(self, name='_name_'):
        self.name = name
        self.description = ' ... '
        self.artist = '_name_'
        self.creation_date = ''
        self.image = None
        self.image_string = None
        self.type = "Tiles"
        self.cell_size = [1, 1]
        self.contact_point = [10, 10]
        self.isometric = False
        self.isometric_offset = [1, 1, 1]
        self.num_of_cells = 1
        self.num_of_cols = 1
        self.num_of_rows = 1
        self.cells = []
        self.animations = {}
