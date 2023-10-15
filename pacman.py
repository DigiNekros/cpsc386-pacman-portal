# Anne Edwards, Miguel Mancera, Parker Nguyen
import pygame
from pygame import mixer
import SpriteSheet


class Pacman():
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.gamesettings
        self.game = game
        self.blocks = game.blocks.blocks
        self.shields = game.shield.shields
        self.powerpills = game.powerpills.powerpills
        self.ghosts = game.ghosts.ghosts
        self.fruit = game.fruit
        self.portals = game.portals
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

    def returnPacman(self):
        return self
    
    def update_movement(self):
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
            self.last_direction = 'down'


    # Updates pacman direction and sprite depending on direction
    def update(self):
        self.update_movement()
        self.check_collision()
        self.blitpacman()

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

    # Check direction pacman is going to compare and see if he can't go a direction anymore if he hit a block
    def check_direction(self, block):
        left = False
        right = False
        up = False
        down = False
        if self.rect.centerx <= block.rect.centerx:
            right = True
        else:
            left = True
        if self.rect.y + self.rect.height / 2 <= block.rect.y + block.rect.height / 2:
            up = True
        else:
            down = True

        if left:
            self.rect.x += 1
        elif right:
            self.rect.x -= 1
        if up:
            self.rect.y -= 1
        elif down:
            self.rect.y += 1

    def check_shield_direction(self, shield):
        left = False
        right = False
        up = False
        down = False
        
        if self.rect.centerx <= shield.rect.centerx:
            right = True
        else:
            left = True
        if self.rect.y + self.rect.height / 2 <= shield.rect.y + shield.rect.height / 2:
            up = True
        else:
            down = True

        if left:
            self.rect.x += 1
        elif right:
            self.rect.x -= 1
        if up:
            self.rect.y -= 1
        elif down:
            self.rect.y += 1
            
    # Pacman and ghosts collision handling
    def check_collision(self): # blocks, powerpills, shield, ghosts, intersections, showgamestats, gamesettings, fruit, orange, blue):
        for block in self.blocks:
            if pygame.sprite.collide_rect(self, block):
                self.check_direction(block)

        for shield in self.shields:
            if pygame.sprite.collide_rect(self, shield):
                self.check_shield_direction(shield)
        
        if pygame.sprite.spritecollide(self, self.powerpills, False):
            for powerpill in self.powerpills:
                if (pygame.sprite.collide_rect(self, powerpill)):
                    for ghost in self.ghosts:
                        if(ghost.color == 'red'):
                            ghost.speed += .001  # speed up Blinky's (red ghost) speed for every pellet eaten
                    self.powerpills.remove(powerpill)
                    if(powerpill.size == 'big'):
                        for ghost in self.ghosts:
                            ghost.afraid = True
                            ghost.frames = 0 # reset the afraid timer
                        self.game.showgamestats.score += 50
                    else:
                        self.game.showgamestats.score += 10
                        self.playPelletEatSound()
                    
        if pygame.sprite.collide_rect(self, self.fruit):
            if(not self.fruit.destroyed):
                self.game.showgamestats.score += self.fruit.value
                self.fruit.destroyed = True
                self.playFruitEatenSound()
                
        if (pygame.sprite.spritecollide(self, self.ghosts, False)):
            for ghost in self.ghosts:
                if (pygame.sprite.collide_rect(self, ghost)):
                    if(ghost.afraid and not ghost.DEAD):
                        ghost.DEAD = True
                        pts = 0
                        for ghost in self.ghosts:
                            if(ghost.DEAD):
                                pts += 1
                                ghost.value = 100 * 2**pts
                        self.game.showgamestats.score += 100 * 2**pts
                        ghost.playDeathSound()
                        pygame.time.wait(500)
                    elif(not ghost.afraid and not ghost.DEAD):
                        self.DEAD = True
                        self.game.gamesettings.game_active = False
                        self.game.showgamestats.num_lives -= 1
                        self.playDeathSound()
                        break
                    
        # portal teleport
        if(pygame.sprite.collide_rect(self, self.portals.orange)):
            blue = self.portals.blue
            if(blue.portal_placed):
                self.portals.close_portal(color='orange') # close the orange portal
                if(blue.output == 'left'):
                    self.rect.x, self.rect.y = blue.rect.x - 40, blue.rect.y
                elif (blue.output == 'right'):
                    self.rect.x, self.rect.y = blue.rect.x + 40, blue.rect.y
                elif (blue.output == 'up'):
                    self.rect.x, self.rect.y = blue.rect.x, blue.rect.y - 40
                elif (blue.output == 'down'):
                    self.rect.x, self.rect.y = blue.rect.x, blue.rect.y + 40
                pygame.time.wait(1000) # wait so can notice change
                self.portals.close_portal(color='blue')

        if(pygame.sprite.collide_rect(self, self.portals.blue)):
            orange = self.portals.orange
            if(orange.portal_placed):
                self.portals.close_portal(color='blue') # close the blue portal
                if (orange.output == 'left'):
                    self.rect.x, self.rect.y = orange.rect.x - 40, orange.rect.y
                elif (orange.output == 'right'):
                    self.rect.x, self.rect.y = orange.rect.x + 40, orange.rect.y
                elif (orange.output == 'up'):
                    self.rect.x, self.rect.y = orange.rect.x, orange.rect.y - 40
                elif (orange.output == 'down'):
                    self.rect.x, self.rect.y = orange.rect.x, orange.rect.y + 40
                pygame.time.wait(1000) # wait so can notice change
                self.portals.close_portal(color='orange')