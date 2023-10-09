import pygame
from pygame import mixer
import SpriteSheet

class Pacman():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.height = 35
        self.width = 35
        ss = SpriteSheet.spritesheet('images/PacmanSpriteSheet.png')
        self.image = [ss.image_at((0,0,32,32)),
                      ss.image_at((448,0,32,32)),
                      ss.image_at((224,0,32,32))]
        self.left_image = [ss.image_at((0, 0, 32, 32)),
                      ss.image_at((448, 0, 32, 32)),
                      ss.image_at((224, 0, 32, 32))]
        self.right_image = [pygame.transform.rotate(ss.image_at((0,0,32,32)), 180),
                      pygame.transform.rotate(ss.image_at((448,0,32,32)), 180),
                      pygame.transform.rotate(ss.image_at((224,0,32,32)), 180)]
        self.up_image = [pygame.transform.rotate(ss.image_at((0, 0, 32, 32)), 270),
                      pygame.transform.rotate(ss.image_at((448, 0, 32, 32)), 270),
                      pygame.transform.rotate(ss.image_at((224, 0, 32, 32)), 270)]
        self.down_image = [pygame.transform.rotate(ss.image_at((0, 0, 32, 32)), 90),
                      pygame.transform.rotate(ss.image_at((448, 0, 32, 32)), 90),
                      pygame.transform.rotate(ss.image_at((224, 0, 32, 32)), 90)]
        self.death_image = [pygame.transform.rotate(ss.image_at((576, 0, 34, 34)), 270),
                            pygame.transform.rotate(ss.image_at((610, 0, 34, 34)), 270),
                            pygame.transform.rotate(ss.image_at((644, 0, 34, 34)), 270),
                            pygame.transform.rotate(ss.image_at((678, 0, 34, 34)), 270),
                            pygame.transform.rotate(ss.image_at((712, 0, 34, 34)), 270),
                            pygame.transform.rotate(ss.image_at((746, 0, 34, 34)), 270),
                            pygame.transform.rotate(ss.image_at((780, 0, 34, 34)), 270),
                            pygame.transform.rotate(ss.image_at((814, 0, 34, 34)), 270),
                            pygame.transform.rotate(ss.image_at((848, 0, 34, 34)), 270)]
        self.image[0] = pygame.transform.scale(self.image[0], (self.height, self.width))
        self.image[1] = pygame.transform.scale(self.image[1], (self.height, self.width))
        self.image[2] = pygame.transform.scale(self.image[2], (self.height, self.width))
        self.rect = self.image[0].get_rect()
        #self.rect.x, self.rect.y = 310, 515
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height

        self.rect.x, self.rect.y = 300, 485
        self.reset_x, self.reset_y = self.rect.x, self.rect.y
        # For updating pacman and to rotate depending on direction
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.DEAD = False

        # to know what direction to place portal
        self.last_direction = 'left'

    # Updates pacman direction and sprite depending on direction
    def update(self):
        if self.moving_right:
            self.rect.x += self.settings.pacmanspeed
            self.image = self.right_image
            self.last_direction = 'right'
        if self.moving_left:
            self.rect.x -= self.settings.pacmanspeed
            self.image = self.left_image
            self.last_direction = 'left'
        if self.moving_up:
            self.rect.y -= self.settings.pacmanspeed
            self.image = self.up_image
            self.last_direction = 'up'
        if self.moving_down:
            self.rect.y += self.settings.pacmanspeed
            self.image = self.down_image
            l=self.last_direction = 'down'

    def blitpacman(self):
        if pygame.time.get_ticks() % 200 <= 50:
            self.screen.blit(self.image[0], self.rect)
        elif pygame.time.get_ticks() % 200 <= 100:
            self.screen.blit(self.image[1], self.rect)
        elif pygame.time.get_ticks() % 200 <= 150:
            self.screen.blit(self.image[2], self.rect)
        else:
            self.screen.blit(self.image[2], self.rect)

    def resetPosition(self):
        self.rect.x, self.rect.y = self.reset_x, self.reset_y

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def deathAnimation(self, frames):
        if(frames <= 60):
            self.screen.blit(self.death_image[0], self.rect)
        elif (frames <= 120):
            self.screen.blit(self.death_image[1], self.rect)
        elif (frames <= 180):
            self.screen.blit(self.death_image[2], self.rect)
        elif (frames <= 240):
            self.screen.blit(self.death_image[3], self.rect)
        elif (frames <= 300):
            self.screen.blit(self.death_image[4], self.rect)
        elif (frames <= 360):
            self.screen.blit(self.death_image[5], self.rect)
        elif (frames <= 420):
            self.screen.blit(self.death_image[6], self.rect)
        elif (frames <= 480):
            self.screen.blit(self.death_image[7], self.rect)
        elif (frames <= 540):
            self.screen.blit(self.death_image[8], self.rect)

    def playPelletEatSound(self):
        mixer.Channel(0).play(pygame.mixer.Sound('sounds/power_pellet_eaten.wav'))
    def playDeathSound(self):
        mixer.Channel(0).play(pygame.mixer.Sound('sounds/life_lost.wav'))
    def playFruitEatenSound(self):
        mixer.Channel(0).play(pygame.mixer.Sound('sounds/fruit_eaten.wav'))


