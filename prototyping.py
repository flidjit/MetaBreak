import os
import math
import pickle
import base64
import sys
import tkinter as tk_
from tkinter import ttk
import pygame as pg_
from pygame.locals import *

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


class Sprite:
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


class Tile:
    def __init__(self):
        self.tile_sheet = 'default'
        self.cel_id = 0
        self.scr_x_ = 0
        self.scr_y_ = 0
        self.height = 0


class TileStack:
    def __init__(self):
        self.map_x_ = 0
        self.map_y_ = 0
        self.scr_x_ = 0
        self.scr_y_ = 0
        self.floor_height = 0
        self.stack_ = [Tile()]


class GameMap:
    def __init__(self, x_size=10, y_size=15):
        self.name = '_name_'
        self.description = ' ... '
        self.creation_date = ''
        self.size = [x_size, y_size]
        self.iso_offset = [43, 24]
        self.sprite_list = ['default', 'pawns', 'symbols']
        self.array_ = [[TileStack() for i in range(x_size)] for j in range(y_size)]