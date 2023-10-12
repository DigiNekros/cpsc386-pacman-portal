import pygame
from pygame.sprite import Sprite, Group



class Shield(Sprite):
    def __init__(self, screen, x, y):
        super(Shield, self).__init__()
        self.screen = screen
        self.height = 13
        self.width = 13
        img = pygame.image.load('images/shield.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = img

    def blitshield(self):
        self.screen.blit(self.image, self.rect)

class Shields:
    def __init__(self, screen):
        self.screen = screen
        self.shields = Group()

    def create_shield(self, x, y):
        shield = Shield(screen=self.screen, x=x, y=y)
        self.shields.add(shield)

    def draw(self):
        for shield in self.shields:
            shield.blitshield()

