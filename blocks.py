# Anne Edwards, Miguel Mancera, Parker Nguyen
import pygame
from pygame.sprite import Sprite, Group
from button import Button


class Blocks(Sprite):
    def __init__(self, screen, x, y):
        super(Blocks, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,15,15)
        self.rect.x = x
        self.rect.y = y
        self.color = ((0, 0, 255))

    def blitblocks(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Maze:
    def __init__(self, screen, game):
        self.screen = screen
        self.blocks = Group()
        self.game = game
        self.frames = game.frames
        self.ready_button = Button(self.screen, "Ready!")
        self.times_drawn = 0

    def create_block(self, x, y):
        block = Blocks(screen=self.screen, x=x, y=y)
        self.blocks.add(block)

    def draw(self):
        self.times_drawn += 1
        for block in self.blocks:
            block.blitblocks()
        if self.times_drawn <= 10:
            self.ready_button.draw_button()