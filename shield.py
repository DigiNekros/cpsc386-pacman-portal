import pygame
from pygame.sprite import Sprite



class Shield(Sprite):
    def __init__(self, screen):
        super(Shield, self).__init__()
        self.screen = screen
        self.height = 13
        self.width = 13
        img = pygame.image.load('images/shield.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.image = img

    def blitshield(self):
        self.screen.blit(self.image, self.rect)

