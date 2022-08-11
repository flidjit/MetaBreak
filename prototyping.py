import os
import math
import pickle
import base64
import sys
import io
import tkinter as tk_
from tkinter import ttk, filedialog
import pygame as pg_
from pygame.locals import *
from pygame.locals import *
from datetime import date

from celldata import cell_data_


class User:
    def __init__(self, screen_name_='Name', email_='@mail.com',
                 last_login_='', selected_theme_='Default'):
        self.screen_name_ = screen_name_
        self.email_ = email_
        self.last_login_ = last_login_
        self.selected_theme_ = selected_theme_
        self.avatars = [None]
        self.graveyard = [None]
        self.campaigns = [None]


class Campaign:
    def __int__(self):
        self.title = 'Campaign 1'
        self.description = []
        self.deck = {}


class Avatar:
    def __int__(self):
        self.stats = {
            "Creator": None,
            "First Name": '',
            "Last Name": '',
            "Gender": '',
            "Age": 1,
            "Height": [5, 1],
            "Weight": 130,
            "Size Category": 'Medium',
            "Description": ['']}
        self.body_type = None
        self.scores = {
            "Level": 1,
            "XP": [0, 100],
            "UPs": [100, 100],
            "Mighty": 1,
            "Nimble": 1,
            "Clever": 1,
            "Alert": 1,
            "Bold": 1,
            "Defense": 1,
            "Health": [20, 20],
            "Energy": [20, 20],
            "Action Points": [5, 5],
            "Inventory Volume": [0, 0],
            "Weight Capacity": [0, 0, 0]}
        self.conditions = {}
        self.resistances = {
            "Arcane": 0,
            "Dark": 0,
            "Light": 0,
            "Shock": 0,
            "Fire": 0,
            "Ice": 0,
            "Slashing": 0,
            "Bashing": 0,
            "Stabbing": 0,
            "Ballistic": 0}
        self.deck = {}
        self.skills = {}
        self.techniques = []
        self.gear = {
            "Loadout 1": {
                "Main Hand": None,
                "Off-Hand": None},
            "Loadout 2": {
                "Main Hand": None,
                "Off-Hand": None},
            "Loadout 3": {
                "Main Hand": None,
                "Off-Hand": None},
            # [Card(), slot occupied by?]
            "Head": [None, False],
            "Face": [None, False],
            "Neck": [None, False],
            "Shoulders": [None, False],
            "Back": [None, False],
            "Cape": [None, False],
            "Torso": [None, False],
            "Arms": [None, False],
            "Hands": [None, False],
            "Fingers": [[None, False]],
            "Waist": [None, False],
            "Legs": [None, False],
            "Shins": [None, False],
            "Feet": [None, False],
            "Inventory": []}


class Card:
    def __int__(self):
        self.root_card = False
        self.branch_cards = {}
        self.unlocked = False
        self.stats = {
            "Fantasy Level": 1,
            "Technology Level": 1,
            "Stat Requirements": {},
            "Skill Requirements": {},
            "Conflicts With": [],
            "UP Cost": 10,
            "Card Type": '',
            "Weight": 1,
            "Volume": 1,
            "Tags": [],
            "Prefix": [],
            "Flavor Text": [],
            "Special Effects": [None]}


class Weapon(Card):
    def __int__(self):
        super(Weapon, self).__int__()
        self.stats["Tags"].append(["Sword", "Melee", "Steel"])
        self.stats["Card Type"] = "Weapon"
        self.stats["AP Cost"] = 3
        self.stats["Range"] = ['melee', 'single target', 5]
        self.stats["Success Roll"] = {
            "Attacker": [['!!-1-D-20', 'Nimble'], +0],
            "Defender": [['Defense', 'Nimble', 'Alert'], +0]}
        self.stats["Magnitude Roll"] = [[1, 6, "Slashing"]]
        self.stats["Success Effects"] = [None]
        self.stats["Critical Magnitude"] = [[2, 6, "Slashing"]]
        self.stats["Critical Effects"] = [None]


class Armor(Card):
    def __int__(self):
        super(Armor, self).__int__()
        self.stats["Tags"].append(["Armor", "Torso", "Steel"])
        self.stats["Card Type"] = "Armor"
        self.stats["Defense Bonus"] = +1
        self.stats["Placement"] = ['Torso']
        self.stats["Resistances"] = {
            "Magic": 0,
            "Unholy": 0,
            "Holy": 0,
            "Shock": 0,
            "Fire": 0,
            "Cold": 0,
            "Slashing": 0,
            "Bashing": 0,
            "Stabbing": 0,
            "Ballistic": 0}


class Upgrade(Card):
    def __int__(self):
        super(Upgrade, self).__int__()
        self.stats["Tags"].append(["Upgrade"])
        self.stats["Card Type"] = "Upgrade"
        self.replace_stats = []
        self.boost_stats = []


class Technique(Card):
    def __int__(self):
        super(Technique, self).__int__()
        self.stats["Tags"].append(["Character Technique", "Magic", "Fire"])
        self.stats["Card Type"] = "Technique"
        self.stats["AP Cost"] = 2
        self.stats["Energy Cost"] = 2
        self.stats["Free Hands Required"] = 1
        self.stats["Verbal Component?"] = False
        self.stats["Line of Sight?"] = True
        self.stats["Range"] = ['ranged', 'single target', 20]
        self.stats["Success Roll"] = {
            "Attacker": [['!!-1-D-20', 'Nimble'], +0],
            "Defender": [['Defense', 'Nimble', 'Alert'], +0]}
        self.stats["Magnitude Roll"] = [[1, 6, "Fire"]]
        self.stats["Success Effects"] = [None]
        self.stats["Critical Magnitude"] = [[2, 6, "Fire"]]
        self.stats["Critical Effects"] = [None]
        self.stats["Special Effects"] = [None]



sprite_types = {
    # [ file location, file extension, cells]
    'Tile Set': [
        '.spx1', [0, 0],
        list],
    'Custom Grid': [
        '.spx2', [0, 0],
        list],
    'Character': [
        '.spx3', [0, 0],
        list],
    'PGui': [
        '.spx4', [0, 0],
        list]}


class Sprite():
    def __init__(self, name_='Bob', description_=' ... ',
                 creation_date_=None, creator_=None,
                 image_=None, image_string_=None,
                 type_=None,
                 cells_=None, animations_=dict):
        super().__init__(name_=name_, description_=description_,
                         creation_date_=creation_date_, creator_=creator_)
        self.type_ = type_
        self.image_ = image_
        self.image_string_ = image_string_
        self.cells_ = cells_  # [sx, sy, w, h, cx, cy]
        self.animations_ = animations_


class TileSet(Sprite):
    def __init__(self, name_=' Enter a name. ', description_=' ... ',
                 creation_date_=None, creator_=None,
                 image_=None, image_string_=None,
                 cell_size_x_=1, cell_size_y_=1,
                 isometric_offset_x_=0, isometric_offset_y_=0,
                 number_of_columns_=1, number_of_rows_=1,
                 type_='Tile Set', cells_=list, animations_=dict):
        super().__init__(name_=name_, description_=description_,
                         creation_date_=creation_date_, creator_=creator_,
                         image_=image_, image_string_=image_string_,
                         type_=type_,
                         cells_=cells_, animations_=animations_)
        self.cell_size_ = [cell_size_x_, cell_size_y_]
        self.isometric_offset_ = [isometric_offset_x_, isometric_offset_y_]
        self.number_of_columns_ = number_of_columns_
        self.number_of_rows_ = number_of_rows_


class PGui(Sprite):
    def __init__(self, name_=' Enter a name. ', description_=' ... ',
                 creation_date_=None, creator_=None,
                 image_=None, image_string_=None,
                 type_='PGui', cells_=cell_data_['PGui'],
                 animations_=dict, buttons_=list):
        super().__init__(name_=name_, description_=description_,
                         creation_date_=creation_date_, creator_=creator_,
                         image_=image_, image_string_=image_string_,
                         type_=type_,
                         cells_=cells_, animations_=animations_)
        self.buttons_ = buttons_
        self.background_img_ = None


class Character(Sprite):
    def __init__(self, name_=' Enter a name. ', description_=' ... ',
                 creation_date_=None, creator_=None,
                 image_=None, image_string_=None,
                 type_='UI', cells_=sprite_types['Character'][2],
                 animations_=dict):
        super().__init__(name_=name_, description_=description_,
                         creation_date_=creation_date_, creator_=creator_,
                         image_=image_, image_string_=image_string_,
                         type_=type_,
                         cells_=cells_, animations_=animations_)


class PgButton:
    def __init__(self, cell_id_=0, action_name_='Options',
                 screen_x_=0, screen_y_=0):
        self.cell_id_ = cell_id_
        self.action_name_ = action_name_
        self.draw_at_ = [screen_x_, screen_y_]
        self.double_scale_ = False
        self.scaled_image_ = None


class Tile:
    def __init__(self, sprite_name='default', cell_id=0,
                 screen_x_=0, screen_y_=0, height=0):
        self.sprite_name = sprite_name
        self.cell_id = cell_id
        self.screen_x_ = screen_x_
        self.screen_y_ = screen_y_
        self.height = height


class TileStack:
    def __init__(self, map_x_=0, map_y_=0,
                 screen_x_=0, screen_y_=0,
                 floor_height=0, stack=list):
        self.map_x_ = map_x_
        self.map_y_ = map_y_
        self.screen_x_ = screen_x_
        self.screen_y_ = screen_y_
        self.floor_height = floor_height
        self.stack_ = stack


class GameMap():
    def __init__(self, name_='Map Name', description_=' ... ',
                 creation_date_=None, creator_=None,
                 x_size=10, y_size=15,
                 iso_offset_x_=42, iso_offset_y_=29,
                 sprite_list=None):
        super().__init__(name_=name_, description_=description_,
                         creation_date_=creation_date_, creator_=creator_)
        self.size = [x_size, y_size]
        self.iso_offset = [iso_offset_x_, iso_offset_y_]
        self.sprite_list = sprite_list
        self.array_ = [[TileStack() for i in range(x_size)] for j in range(y_size)]



