import pygame

class Settings():
    def __init__(self):
        # screen settings
        self.screen_width = 700
        self.screen_height = 750
        self.bg_color = (0,0,0)

        # adjustable speed factor for player
        self.pacman_speed_factor = 0.4

        self.wall_height = self.screen_height // 51
        self.wall_width = self.screen_width // 55

        self.regular_points_radius = self.wall_width // 3
        self.power_points_radius = int(self.regular_points_radius * 2)

        self.node_height = self.wall_height
        self.node_width = self.wall_width
