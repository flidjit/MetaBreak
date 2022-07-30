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


class NamedThing:
    def __init__(self, name_='Thing Name', description_=' ... ',
                 creation_date_=None, creator_=None):
        self.name_ = name_
        self.description_ = description_
        self.creation_date_ = creation_date_
        self.creator_ = creator_


class User:
    def __init__(self, screen_name_='Name', email_='@mail.com',
                 last_login_='', selected_theme_='Default'):
        self.screen_name_ = screen_name_
        self.email_ = email_
        self.last_login_ = last_login_
        self.selected_theme_ = selected_theme_


class MOB(NamedThing):
    def __init__(self, first_name_='Name', last_name_='Name',
                 description_=' ... ', creation_date_=None, creator_=None,
                 sprite_sheet_='Pawn',
                 strong_=10, tough_=10, nimble_=10,
                 clever_=10, pretty_=10, alert_=10,
                 hit_points_=10, action_points_=4, energy_points_=10,
                 defence_=10, attack_=2):
        super().__init__(name_=first_name_+'_'+last_name_,
                         description_=description_,
                         creation_date_=creation_date_, creator_=creator_)
        self.first_name_ = first_name_
        self.last_name_ = last_name_
        self.sprite_sheet_ = sprite_sheet_
        self.current_animation_ = None
        self.animation_index_ = 0
        self.frame_timer_ = 0
        self.strong_ = strong_
        self.tough_ = tough_
        self.nimble_ = nimble_
        self.clever_ = clever_
        self.pretty_ = pretty_
        self.alert_ = alert_
        self.hit_points_ = [hit_points_, hit_points_]
        self.energy_points_ = [energy_points_, energy_points_]
        self.action_points_ = [action_points_, action_points_]
        self.defence_ = defence_
        self.attack_ = attack_
        self.techniques = dict
        self.skills = dict
        self.left_hand_ = None
        self.right_hand_ = None
        self.head_gear_ = None
        self.face_gear_ = None
        self.torso_gear_ = None
        self.hand_gear_ = None
        self.back_gear_ = None
        self.leg_gear_ = None
        self.foot_gear_ = None
        self.pack = list
        self.current_location = None
        self.notes = dict


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


class Sprite(NamedThing):
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


class GameMap(NamedThing):
    def __init__(self, name_='Map Name', description_=' ... ',
                 creation_date_=None, creator_=None,
                 x_size=10, y_size=15,
                 iso_offset_x_=42, iso_offset_y_=29,
                 sprite_list=list):
        super().__init__(name_=name_, description_=description_,
                         creation_date_=creation_date_, creator_=creator_)
        self.size = [x_size, y_size]
        self.iso_offset = [iso_offset_x_, iso_offset_y_]
        self.sprite_list = sprite_list
        self.array_ = [[TileStack() for i in range(x_size)] for j in range(y_size)]


class Item(NamedThing):
    def __init__(self, name_='Item Name', description_=' ... ',
                 creation_date_=None, creator_=None,
                 weight_=0, technology_level_=1, magic_level_=1):
        super().__init__(name_=name_, description_=description_,
                         creation_date_=creation_date_, creator_=creator_)
        self.weight_ = weight_
        self.technology_level_ = technology_level_
        self.magic_level_ = magic_level_


class Armor(Item):
    def __init__(self, name_='Armor Name', description_=' ... ',
                 creation_date_=None, creator_=None,
                 weight_=1, technology_level_=1, magic_level_=1,
                 equip_location_='Head', defence_bonus_=0):
        super().__init__(name_=name_, description_=description_,
                         creation_date_=creation_date_, creator_=creator_,
                         weight_=weight_, technology_level_=technology_level_,
                         magic_level_=magic_level_)
        self.equip_location_ = equip_location_
        self.defence_bonus_ = defence_bonus_


class Weapon(Item):
    def __init__(self, name_='Weapon Name', description_=' ... ',
                 creation_date_=None, creator_=None,
                 weight_=1, technology_level_=1, magic_level_=1,
                 attack_range_=1, attack_bonus_=1,
                 two_handed_=False, concealable_=False):
        super().__init__(name_=name_, description_=description_,
                         creation_date_=creation_date_, creator_=creator_,
                         weight_=weight_, technology_level_=technology_level_,
                         magic_level_=magic_level_)
        self.attack_range_ = attack_range_
        self.attack_bonus_ = attack_bonus_
        self.two_handed_ = two_handed_
        self.concealable_ = concealable_

