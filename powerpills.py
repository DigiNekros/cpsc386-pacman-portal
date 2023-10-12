import pygame
from pygame.sprite import Sprite, Group


class Powerpill(Sprite):
    def __init__(self, screen, x, y, size='small'):
        super(Powerpill, self).__init__()
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
        self.rect.x = x
        self.rect.y = y
        self.image = img

    def blitpowerpills(self):
        self.screen.blit(self.image, self.rect)


class PowerPills:
    def __init__(self, screen):
        self.screen = screen
        self.powerpills = Group()

    def create_powerpill(self, x, y, size='small'):
        powerpill = Powerpill(screen=self.screen, x=x, y=y, size=size)
        self.powerpills.add(powerpill)

    def draw(self):
        for powerpill in self.powerpills:
            powerpill.blitpowerpills()

