
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
        self.isometric_offset = [1, 1]
        self.num_of_cells = 1
        self.num_of_cols = 1
        self.num_of_rows = 1
        self.cells = []
        self.animations = {}


