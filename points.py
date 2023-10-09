# Anne Edwards, Miguel Mancera, Parker Nguyen
# CPSC 386-03

import pygame as pg
from pygame.sprite import Sprite, Group
from pathlib import Path
import file_functions as f


YELLOW = (155, 155, 0)
ORANGE = (255, 175, 0)

class RegularPoint(Sprite):
    def __init__(self, game, x, y, radius):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.color = YELLOW
        self.radius = radius
        self.rect = pg.Rect(x, y, 2 * radius, 2 * radius) # for collisions
        self.rect.x = x
        self.rect.y = y
        self.x = self.rect.centerx
        self.y = self.rect.centery

    def update(self):
        self.draw()
    
    def draw(self):
        # self.screen.fill((255, 255, 255), self.rect)
        pg.draw.circle(self.screen, self.color, (self.x, self.y), self.radius, 0)

    def update_score(self): pass


class PowerPoint(Sprite):
    def __init__(self, game, x, y, radius):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.color = ORANGE
        self.radius = radius
        self.rect = pg.Rect(x, y, 2 * radius, 2 * radius) # for collisions
        self.rect.x = x
        self.rect.y = y
        self.x = self.rect.centerx
        self.y = self.rect.centery

    def update(self):
        self.draw()
    
    def draw(self):
        pg.draw.circle(self.screen, self.color, (self.x, self.y), self.radius, 0)

    def update_score(self): pass


class Points:
    def __init__(self, game, file):
        self.game = game
        self.settings = game.settings
        self.file = file
        self.rp_radius = game.settings.regular_points_radius
        self.pp_radius = game.settings.power_points_radius
        self.width = game.settings.wall_width
        self.height = game.settings.wall_height
        self.top = 20
        self.y = self.top
        self.left = 8
        self.rows = []

        self.r_points = Group() # for collisions
        self.p_points = Group() # for collisions
        # self.pac_man = Group() # for collisions
        # self.pac_man.add(game.pac_man)

        f.read_file(list=self.rows, file=self.file)
        self.create_points()

    def set_side(self):
        self.x = self.left

    def create_points(self):
        i = 0
        while i < len(self.rows):
            row = self.rows[i]
            self.set_side() # get the initial x position
            iterator = 0
            while iterator < len(row):
                char = row[iterator]
                if char == 'p':
                    point = RegularPoint(game=self.game, x=self.x, y=self.y, radius=self.rp_radius)
                    self.r_points.add(point)
                elif char == 'o':
                    point = PowerPoint(game=self.game, x=self.x, y=self.y, radius=self.pp_radius)
                    self.p_points.add(point)
                self.x += self.width
                iterator += 1
            self.y += self.height
            i += 1

    # def check_collisions(self):
    #     # check for 'regular points' collision
    #     collision = pg.sprite.groupcollide(self.pac_man, 
    #                                        self.r_points, False, 
    #                                        True)
    #     if collision:
    #         for point in collision:
    #             point.update_score()

    #     # check for 'power pill' collision
    #     collision = pg.sprite.groupcollide(self.pac_man,
    #                                        self.p_points, False,
    #                                        True)
    #     if collision:
    #         for point in collision:
    #             point.update_score()


    def draw(self):
        for point in self.r_points.sprites():
            point.draw()

        for point in self.p_points.sprites():
            point.draw()

    def update(self):
        # self.check_collisions()
        self.draw()