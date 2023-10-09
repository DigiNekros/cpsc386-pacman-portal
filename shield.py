# Anne Edwards, Miguel Mancera, Parker Nguyen
# CPSC 386-03

import pygame as pg
from pygame.sprite import Sprite, Group
from pathlib import Path
import file_functions as f


WHITE = (255, 255, 255)

class ShieldPiece(Sprite):
    def __init__(self, game, x, y, width, height):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.color = WHITE
        self.rect = pg.Rect(x, y, width, height)

    def update(self):
        self.draw()

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)

class Shield:
    def __init__(self, game, file):
        self.game = game
        self.settings = game.settings
        self.file = file
        self.width = game.settings.wall_width
        self.height = game.settings.wall_width
        self.top = 20
        self.y = self.top
        self.left = 8
        self.rows = []
        self.shield_pieces = Group()
        f.read_file(list=self.rows, file=self.file)
        self.create_shield()
        self.adjust()

    def set_side(self):
        self.x = self.left

    def create_shield(self):
        i = 0
        while i < len(self.rows):
            row = self.rows[i]
            self.set_side() # get the initial x position
            iterator = 0
            while iterator < len(row):
                char = row[iterator]
                if char == 's':
                    shield = ShieldPiece(game=self.game, x=self.x, y=self.y, width=self.width, height=self.height)
                    self.shield_pieces.add(shield)
                self.x += self.width
                iterator += 1
            self.y += self.height
            i += 1

    def adjust(self):
        for piece in self.shield_pieces.sprites():
            piece.rect.y += 40

    def draw(self):
        for piece in self.shield_pieces.sprites():
            piece.draw()

    def update(self):
        # self.check_collisions()
        self.draw()
