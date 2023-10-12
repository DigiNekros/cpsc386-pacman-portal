import pygame
from pygame.sprite import Sprite, Group
from SpriteSheet import spritesheet


class Portal(Sprite):
    def __init__(self, screen, type, x, y):
        super(Portal, self).__init__()
        self.screen = screen
        self.type = type
        ss = spritesheet('images/portals.png')

        self.orange_left = pygame.transform.scale(ss.image_at((0,0,35,96)), (15,41))
        self.blue_left = pygame.transform.scale(ss.image_at((0,96,35,96)), (15,41))

        self.orange_right = pygame.transform.rotate(self.orange_left, 180)
        self.orange_up = pygame.transform.rotate(self.orange_left, 270)
        self.orange_down = pygame.transform.rotate(self.orange_left, 90)

        self.blue_right = pygame.transform.rotate(self.blue_left, 180)
        self.blue_up = pygame.transform.rotate(self.blue_left, 270)
        self.blue_down = pygame.transform.rotate(self.blue_left, 90)

        if(type == 'orange'):
            img = self.orange_left
        elif(type == 'blue'):
            img = self.blue_left

        img = pygame.transform.scale(img, (15, 15))
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = img

        # direction pacman would be coming out
        self.output = 'left'

        # to make sure portal is placed somewhere
        self.portal_placed = False

    def blitportal(self):
        self.screen.blit(self.image, self.rect)

    def rotate(self, direction):
        if(self.type == 'orange'):
            if(direction == 'left'):
                self.image = self.orange_left
                self.output = 'right'
            elif (direction == 'right'):
                self.image = self.orange_right
                self.output = 'left'
            elif (direction == 'up'):
                self.image = self.orange_up
                self.output = 'down'
            elif (direction == 'down'):
                self.image = self.orange_down
                self.output = 'up'
        elif (self.type == 'blue'):
            if (direction == 'left'):
                self.image = self.blue_left
                self.output = 'right'
            elif (direction == 'right'):
                self.image = self.blue_right
                self.output = 'left'
            elif (direction == 'up'):
                self.image = self.blue_up
                self.output = 'down'
            elif (direction == 'down'):
                self.image = self.blue_down
                self.output = 'up'


class Portals:
    def __init__(self, screen):
        self.screen = screen
        self.portals = Group()

    def add_portal(self, portal):
        self.portals.add(portal)

    def draw(self):
        for portal in self.portals:
            portal.blitportal()
