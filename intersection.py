import pygame
from pygame.sprite import Sprite, Group


class Intersection(Sprite):
    def __init__(self, screen, number, x, y):
        super(Intersection, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 1, 1)
        self.rect.x = x
        self.rect.y = y
        self.color = ((0, 0, 0))
        self.number = number

        self.up = False
        self.down = False
        self.left = False
        self.right = False

        ups = [6,7,9,10,12,13,14,15,16,19,20,21,23,25,28,29,30,31,32,34,35,37,38,41,42,44,46,48,49,51,53,55,56,57,60,61,62,64,65,66,67]
        downs = [0,1,2,3,4,5,6,7,8,11,12,13,15,17,18,20,22,24,26,28,29,31,32,34,35,36,37,39,40,42,43,45,46,47,50,51,52,54,58,59,63]
        lefts = [1,2,4,5,7,8,9,10,11,12,13,15,17,19,21,23,24,25,26,28,29,32,33,35,37,38,39,41,42,43,45,47,48,49,50,51,53,55,56,58,60,62,63,65,66,67]
        rights = [0,1,3,4,6,7,8,9,10,11,12,14,16,18,20,22,23,24,25,27,28,31,32,34,36,37,38,40,41,42,44,46,47,48,49,50,52,54,55,57,59,61,62,64,65,66]

        for up in ups:
            if(self.number == up):
                self.up = True
        for down in downs:
            if(self.number == down):
                self.down = True
        for right in rights:
            if(self.number == right):
                self.right = True
        for left in lefts:
            if(self.number == left):
                self.left = True

    def blit(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Intersections:
    def __init__(self, screen):
        self.screen = screen
        self.intersections = Group()

    def create_intersection(self, x, y, number):
        intersection = Intersection(screen=self.screen, x=x, y=y, number=number)
        self.intersections.add(intersection)

    def draw(self):
        for intersect in self.intersections:
            intersect.blit()