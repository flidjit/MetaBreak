
class Sheet:
    def __init__(self, name='_name_'):
        self.name = name
        self.description = ''
        self.artist = ''
        self.date = ''
        self.image = None
        self.image_string = None
        self.type = "Tiles"
        self.cell_size = [0, 0]
        self.contact_point = [0, 0]
        self.isometric = False
        self.isometric_offset = [0, 0]
        self.num_of_cells = 0
        self.num_of_cols = 0
        self.num_of_rows = 0
        self.cells = []
        self.animations = {}


