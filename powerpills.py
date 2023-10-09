import pygame
from pygame.sprite import Sprite


class Powerpills(Sprite):
    def __init__(self, screen, size = 'small'):
        super(Powerpills, self).__init__()
        self.screen = screen
        self.size = size
        if(self.size == 'big'):
            self.height = 15
            self.width = 15
        else:
            self.height = 7
            self.width = 7
        img = pygame.image.load('images/point.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.image = img

    def blitpowerpills(self):
        self.screen.blit(self.image, self.rect)

