# Anne Edwards, Miguel Mancera, Parker Nguyen
# CPSC 386-03

import pygame as pg
from pygame.sprite import Sprite, Group
from pathlib import Path


MEDIUM_BLUE = (0, 0, 205)

class WallPieces(Sprite):
    def __init__(self, game, x, y, width, height):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.color = MEDIUM_BLUE
        self.rect = pg.Rect(x, y, width, height)

    def update(self):
        self.draw()

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)

class Wall:
    def __init__(self, game, row, x, y):
        self.game = game
        self.screen = game.screen
        self.row = row
        self.settings = game.settings
        self.width = game.settings.wall_width
        self.height = game.settings.wall_height
        self.x, self.y = x, y
        self.pieces = Group()
        self.create_wall()

    def create_wall(self):
        iterator = 0
        while iterator < len(self.row):
            piece = WallPieces(game=self.game, x=self.x, y=self.y, width=self.width, height=self.height)
            self.pieces.add(piece)
            self.x += self.width
            iterator += 1

    def draw(self):
        for piece in self.pieces.sprites():
            piece.update()


class Maze:
    def __init__(self, game, file):
        self.game = game
        self.settings = game.settings
        self.file = file
        self.width = game.settings.wall_width
        self.height = game.settings.wall_height
        self.top = 20
        self.y = self.top
        self.left = None
        self.rows = []
        self.maze_walls = []
        self.get_maze(file=self.file)
        self.create_maze()

    # for troubleshooting
    def print_maze(self):
        i = 0
        while i < len(self.rows):
            print(f'{self.rows[i]}')
            i += 1

    def get_maze(self, file):
        f = Path(file)
        contents = f.read_text()
        
        i = 0
        # break up into rows
        while i < len(contents):
            string = ''
            char = contents[i]
            while char != '\n' and i < len(contents):
                string += char
                i += 1
                if i < len(contents):
                    char = contents[i]
            if string != '':
                self.rows.append(string)
            i += 1

    def set_side(self):
        self.left = 20
        self.x = 20

    def create_maze(self):
        i = 0
        while i < len(self.rows):
            row = self.rows[i]
            self.set_side() # get the initial x position
            iterator = 0
            while iterator < len(row):
                char = row[iterator]
                barrier = []
                init_x = self.x
                while char == 'X' and iterator < len(row):
                    barrier.append(char)
                    iterator += 1
                    self.x += self.width
                    if iterator < len(row):
                        char = row[iterator]
                
                if len(barrier) > 0:
                    wall = Wall(game=self.game, x=init_x, y=self.y, row=barrier)
                    self.maze_walls.append(wall)
                
                self.x += self.width
                iterator += 1
            self.y += self.height
            i += 1

    def draw(self):
        for i in range(len(self.maze_walls)):
            self.maze_walls[i].draw()