import pygame
from pygame.sprite import Sprite
from pygame.sysfont import SysFont
from pygame import mixer
import SpriteSheet
import random

class Fruit(Sprite):
    def __init__(self, screen):
        super(Fruit, self).__init__()
        self.screen = screen
        ss = SpriteSheet.spritesheet('images/Fruits.png')
        self.fruits = [ss.image_at((0,0,32,32)),
                       ss.image_at((32,0,32,32)),
                       ss.image_at((64,0,32,32)),
                       ss.image_at((96,0,32,32)),
                       ss.image_at((128,0,32,32))]
        self.values = [100, 300, 500, 700, 1000]
        index = random.randint(0,4)
        img, self.value = self.fruits[index], self.values[index]
        img = pygame.transform.scale(img, (25, 25))
        self.rect = img.get_rect()
        self.image = img
        self.rect.x, self.rect.y = 1000,1000 # hide fruit offscreen
        self.font = SysFont(None, 32, italic=True)
        self.score_image = self.font.render(str(self.value), True, (255, 255, 255), (0,0,0))

        self.randomint = 101
        self.fruitspawned = False
        self.destroyed = False

        # how long to show score
        self.frames = 0

    def blitfruit(self):
        if(not self.destroyed):
            if(pygame.time.get_ticks() % 1000 <= 1 and not self.fruitspawned):
                self.randomint = random.randint(1,100)
            if(self.randomint <= 20): # 20% chance of fruit spawn
                self.rect.x, self.rect.y = 312, 364
                self.screen.blit(self.image, self.rect)
                self.fruitspawned = True
        elif(self.frames <= 60 and self.destroyed):
            self.screen.blit(self.score_image, self.rect)
            self.frames += 1
        if(self.frames > 60):
            self.frames = 0
            self.rect.x, self.rect.y = 1000, 1000  # hide fruit offscreen

    def fruitReset(self):
        self.destroyed = False  # make getting the fruit possible again for the next stage
        self.fruitspawned = False
        self.randomint = 101