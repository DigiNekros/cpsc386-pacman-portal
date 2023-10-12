import pygame
from pygame.sprite import Sprite, Group


class Blocks(Sprite):
    def __init__(self, screen, x, y):
        super(Blocks, self).__init__()
        self.screen = screen
        #img = pygame.image.load('images/block.png')
        #img = pygame.transform.scale(img, (15, 15))
        #self.rect = img.get_rect()
        self.rect = pygame.Rect(0,0,15,15)
        self.rect.x = x
        self.rect.y = y
        self.color = ((0, 0, 255))
        #self.image = img

    def blitblocks(self):
        #self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect)

class Maze:
    def __init__(self, screen):
        self.screen = screen
        self.blocks = Group()

    def create_block(self, x, y):
        block = Blocks(screen=self.screen, x=x, y=y)
        self.blocks.add(block)

    def draw(self):
        for block in self.blocks:
            block.blitblocks()