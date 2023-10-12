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
        self.create_orange_portal()
        self.create_blue_portal()

    def create_orange_portal(self):
        self.orange = Portal(self.screen, "orange", -1, -1) # portal offscreen
        self.portals.add(self.orange)

    def create_blue_portal(self):
        self.blue = Portal(self.screen, "blue", -1, -1) # portal offscreen
        self.portals.add(self.blue)

    def draw(self):
        for portal in self.portals:
            portal.blitportal()

    def update(self):
        for portal in self.portals:
            if (portal.rect.x > -1 and portal.rect.y > -1):
                self.draw()

    def close_portal(self, color):
        if color == 'blue':
            self.blue.rect.x = -1
            self.blue.rect.y = -1
        else:
            self.orange.rect.x = -1
            self.orange.rect.y = -1
            
    def place_portal_orange(self, pacman):
        orange = self.orange
        if(pacman.last_direction == 'left'):
            orange.rect.x, orange.rect.y = pacman.rect.x - 14, pacman.rect.y
        elif (pacman.last_direction == 'right'):
            orange.rect.x, orange.rect.y = pacman.rect.x + 34.5, pacman.rect.y
        elif (pacman.last_direction == 'up'):
            orange.rect.x, orange.rect.y = pacman.rect.x, pacman.rect.y - 14
        elif (pacman.last_direction == 'down'):
            orange.rect.x, orange.rect.y = pacman.rect.x, pacman.rect.y + 34.5
        orange.rotate(pacman.last_direction)
        orange.portal_placed = True
        
    def place_portal_blue(self, pacman):
        blue = self.portals.blue
        if (pacman.last_direction == 'left'):
            blue.rect.x, blue.rect.y = pacman.rect.x - 14, pacman.rect.y
        elif (pacman.last_direction == 'right'):
            blue.rect.x, blue.rect.y = pacman.rect.x + 34.5, pacman.rect.y
        elif (pacman.last_direction == 'up'):
            blue.rect.x, blue.rect.y = pacman.rect.x, pacman.rect.y - 14
        elif (pacman.last_direction == 'down'):
            blue.rect.x, blue.rect.y = pacman.rect.x, pacman.rect.y + 34.5
        blue.rotate(pacman.last_direction)
        blue.portal_placed = True