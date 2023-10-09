import pygame
from pygame.sprite import Sprite


class Blocks(Sprite):
    def __init__(self, screen):
        super(Blocks, self).__init__()
        self.screen = screen
        #img = pygame.image.load('images/block.png')
        #img = pygame.transform.scale(img, (15, 15))
        #self.rect = img.get_rect()
        self.rect = pygame.Rect(0,0,15,15)
        self.color = ((0, 0, 255))
        #self.image = img

    def blitblocks(self):
        #self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect)