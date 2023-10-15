# Anne Edwards, Miguel Mancera, Parker Nguyen
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from pygame.sysfont import SysFont
from pygame import mixer
import SpriteSheet
from random import randint

# up = [30, 32, 35, 36, 39, 42, 45, 47, 49, 50, 52, 54, 57, 58, 61, 62, 65, 66, 67, 68]
# down = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 16, 18, 19, 21, 25]
# right = [15, 17, 23, 24, 28, 29, 37, 38, 41, 53, 55, 56, 60]
# left = [10, 11, 20, 22, 26, 27, 33, 34, 40, 43, 44, 46, 48, 51, 59, 63, 64]
up = [32, 36, 39, 42, 45, 47, 49, 50, 52, 54, 57, 58, 61, 62, 65, 66, 67, 68]
down = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 16, 18, 19, 21, 25, 29, 30]
right = [15, 17, 23, 24, 28, 35, 37, 38, 41, 53, 55, 56, 60]
left = [10, 11, 20, 22, 26, 27, 33, 34, 40, 43, 44, 46, 48, 51, 59, 63, 64]

class Ghost(Sprite):
    def __init__(self, screen, color):
        super(Ghost, self).__init__()
        self.color = color # ghost type
        self.screen = screen
        self.height = 35
        self.width = 35

        Cyan_SS = SpriteSheet.spritesheet('images/Cyan/CyanSpriteSheet.png')
        Orange_SS = SpriteSheet.spritesheet('images/Orange/OrangeSpriteSheet.png')
        Pink_SS = SpriteSheet.spritesheet('images/Pink/PinkSpriteSheet.png')
        Red_SS = SpriteSheet.spritesheet('images/Red/RedSpriteSheet.png')
        Freight_ss = SpriteSheet.spritesheet('images/PowerPelletSpriteSheet.png')
        Eyes_ss = SpriteSheet.spritesheet('images/EyesSpriteSheet.png')

        self.left_image = []
        self.right_image = []
        self.up_image = []
        self.down_image = []
        self.freight = [Freight_ss.image_at((0,0,32,38)),
                        Freight_ss.image_at((0,38,32,38)),
                        Freight_ss.image_at((0,76,32,38)),
                        Freight_ss.image_at((0,114,32,38))]
        self.eyes = [Eyes_ss.image_at((0,0,23,12)),
                     Eyes_ss.image_at((0,12,23,12)),
                     Eyes_ss.image_at((0,24,23,12)),
                     Eyes_ss.image_at((0,36,23,12))]

        if color == "red":
            self.left_image = [Red_SS.image_at((0,76,32,38)),
                               Red_SS.image_at((0,228, 32,38))]
            self.right_image = [Red_SS.image_at((0, 190, 32, 38)),
                               Red_SS.image_at((0, 266, 32, 38))]
            self.up_image = [Red_SS.image_at((0, 0, 32, 38)),
                               Red_SS.image_at((0, 114, 32, 38))]
            self.down_image = [Red_SS.image_at((0, 38, 32, 38)),
                               Red_SS.image_at((0, 152, 32, 38))]
        elif color == "cyan":
            self.left_image = [Cyan_SS.image_at((0, 76, 32, 38)),
                               Cyan_SS.image_at((0, 228, 32, 38))]
            self.right_image = [Cyan_SS.image_at((0, 190, 32, 38)),
                                Cyan_SS.image_at((0, 266, 32, 38))]
            self.up_image = [Cyan_SS.image_at((0, 0, 32, 38)),
                             Cyan_SS.image_at((0, 114, 32, 38))]
            self.down_image = [Cyan_SS.image_at((0, 38, 32, 38)),
                               Cyan_SS.image_at((0, 152, 32, 38))]
        elif color == "orange":
            self.left_image = [Orange_SS.image_at((0, 76, 32, 38)),
                               Orange_SS.image_at((0, 228, 32, 38))]
            self.right_image = [Orange_SS.image_at((0, 190, 32, 38)),
                                Orange_SS.image_at((0, 266, 32, 38))]
            self.up_image = [Orange_SS.image_at((0, 0, 32, 38)),
                             Orange_SS.image_at((0, 114, 32, 38))]
            self.down_image = [Orange_SS.image_at((0, 38, 32, 38)),
                               Orange_SS.image_at((0, 152, 32, 38))]
        elif color == "pink":
            self.left_image = [Pink_SS.image_at((0, 76, 32, 38)),
                               Pink_SS.image_at((0, 228, 32, 38))]
            self.right_image = [Pink_SS.image_at((0, 190, 32, 38)),
                                Pink_SS.image_at((0, 266, 32, 38))]
            self.up_image = [Pink_SS.image_at((0, 0, 32, 38)),
                             Pink_SS.image_at((0, 114, 32, 38))]
            self.down_image = [Pink_SS.image_at((0, 38, 32, 38)),
                               Pink_SS.image_at((0, 152, 32, 38))]

        self.rect = pygame.transform.scale(self.up_image[0], (self.height, self.width)).get_rect()
        self.rect.x, self.rect.y = 330, 315
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height
        self.image = [None, None] #image placeholder
        self.image = self.up_image #start with ghost looking up

        self.moving_up = True #Start with the ghosts going up
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.last_move = "up/down"
        self.last_intersection = None

        self.speed = 1

        # ghosts are blue
        self.afraid = False

        # ghosts are eyes
        self.DEAD = False

        self.value = 0
        self.font = SysFont(None, 16, italic=True)
        self.score_image = self.font.render(str(self.value), True, (255, 255, 255), (0, 0, 0))

        # how long to show score
        self.frames = 0

    def update(self):
        if self.moving_left == True:
            self.rect.x -= self.speed
            self.image = self.left_image
        elif self.moving_right == True:
            self.rect.x += self.speed
            self.image = self.right_image
        elif self.moving_up == True:
            self.rect.y -= self.speed
            self.image = self.up_image
        elif self.moving_down == True:
            self.rect.y += self.speed
            self.image = self.down_image

    def blitghosts(self):
        if(self.DEAD):
            if(self.moving_left):
                self.screen.blit(self.eyes[2], self.rect)
            elif (self.moving_right):
                self.screen.blit(self.eyes[3], self.rect)
            elif (self.moving_up):
                self.screen.blit(self.eyes[1], self.rect)
            elif (self.moving_down):
                self.screen.blit(self.eyes[0], self.rect)
        elif(self.afraid):
            if(self.frames <= 720):
                if pygame.time.get_ticks() % 200 <= 50:
                    self.screen.blit(self.freight[2], self.rect)
                elif pygame.time.get_ticks() % 200 <= 100:
                    self.screen.blit(self.freight[3], self.rect)
                elif pygame.time.get_ticks() % 200 <= 150:
                    self.screen.blit(self.freight[2], self.rect)
                else:
                    self.screen.blit(self.freight[3], self.rect)
            elif(self.frames <= 960):
                if pygame.time.get_ticks() % 200 <= 50:
                    self.screen.blit(self.freight[0], self.rect)
                elif pygame.time.get_ticks() % 200 <= 100:
                    self.screen.blit(self.freight[1], self.rect)
                elif pygame.time.get_ticks() % 200 <= 150:
                    self.screen.blit(self.freight[2], self.rect)
                else:
                    self.screen.blit(self.freight[3], self.rect)
        else:
            if pygame.time.get_ticks() % 200 <= 50:
                self.screen.blit(self.image[0], self.rect)
            elif pygame.time.get_ticks() % 200 <= 100:
                self.screen.blit(self.image[1], self.rect)
            elif pygame.time.get_ticks() % 200 <= 150:
                self.screen.blit(self.image[0], self.rect)
            else:
                self.screen.blit(self.image[1], self.rect)
        if(self.frames <= 60 and self.DEAD):
            self.screen.blit(self.score_image, self.rect)
            self.frames += 1
        if(self.frames <= 960 and self.afraid):
            self.frames += 1
        elif(self.frames > 960 and self.afraid):
            self.afraid = False
            self.frames = 0

    def resetPosition(self):
        self.moving_up = True  # Start with the ghosts going up
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.rect.x, self.rect.y = 300, 300

        self.afraid = False
        self.DEAD = False

    def playAfraidSound(self):
        mixer.Channel(1).play(pygame.mixer.Sound('sounds/ghosts_ambient.wav'))

    def playDeathSound(self):
        mixer.Channel(1).play(pygame.mixer.Sound('sounds/ghost_eaten.wav'))

    def playRetreatSound(self):
        mixer.Channel(1).play(pygame.mixer.Sound('sounds/ghosts_ambient_scared1.wav'))


class Ghosts:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.pacman = None
        self.blocks = game.blocks.blocks
        self.intersections = game.intersections.intersections
        self.portals = game.portals
        self.ghosts = Group()

    def create_ghost(self, color):
        ghost = Ghost(screen=self.screen, color=color)
        self.ghosts.add(ghost)

    def update_ghosts(self):
        for ghost in self.ghosts:
            ghost.update()

    def draw(self):
        for ghost in self.ghosts:
            ghost.blitghosts()
            if(ghost.DEAD):
                ghost.playRetreatSound()
            elif(ghost.afraid):
                ghost.playAfraidSound() # if ghosts are afraid, loop their sound

    def update(self):
        self.update_ghosts()
        self.check_collision()
        self.draw()

    def reset(self):
        for ghost in self.ghosts:
            ghost.resetPosition()

    def change_speed(self, reset=False):
        if reset:
            for ghost in self.ghosts:
                ghost.speed = 1
        else:
            for ghost in self.ghosts:
                ghost.speed += 1

    # Check direction ghost is going to compare and see if they can't go a direction anymore if they hit a block
    def check_direction(self, ghost, block):
        left = False
        right = False
        up = False
        down = False
        if ghost.rect.centerx <= block.rect.centerx:
            right = True
        else:
            left = True
        if ghost.rect.y + ghost.rect.height / 2 <= block.rect.y + block.rect.height / 2:
            up = True
        else:
            down = True

        if left:
            ghost.rect.x += 1
        elif right:
            ghost.rect.x -= 1
        if up:
            ghost.rect.y -= 1
        elif down:
            ghost.rect.y += 1

    def stuck(self, ghost):
        collision = False
        for block in self.blocks:
                if pygame.sprite.collide_rect(ghost, block):
                    collision = True
                    self.check_direction(ghost, block)
                    break

        return collision


    def go_home(self, ghost, intersection):
        if intersection.number in up:
            ghost.moving_left = False
            ghost.moving_right = False
            ghost.moving_down = False
            ghost.moving_up = True
        if intersection.number in down:
            ghost.moving_left = False
            ghost.moving_right = False
            ghost.moving_down = True
            ghost.moving_up = False
        if intersection.number in left:
            ghost.moving_left = True
            ghost.moving_right = False
            ghost.moving_down = False
            ghost.moving_up = False
        if intersection.number in right:
            ghost.moving_left = False
            ghost.moving_right = True
            ghost.moving_down = False
            ghost.moving_up = False

    # Ghosts collision handling
    def check_collision(self):
        for block in self.blocks:
            for singleghost in self.ghosts:
                if (pygame.sprite.collide_rect(singleghost, block)):
                    self.check_direction(singleghost, block)

        for intersection in self.intersections:
            for singleghost in self.ghosts:
                if(pygame.sprite.collide_rect(singleghost, intersection)):
                    self.ghost_intersection_behavior(singleghost, self.pacman, intersection)

        if(self.game.showgamestats.level > 4): # if player beyond level 4, ghosts can enter and exit portals too
            for ghost in self.ghosts:
                orange = self.portals.orange
                blue = self.portals.blue

                if (pygame.sprite.collide_rect(ghost, orange)):
                    if (blue.portal_placed):
                        self.portals.close_portal(color='orange') # close the orange portal
                        if (blue.output == 'left'):
                            ghost.rect.x, ghost.rect.y = blue.rect.x - 40, blue.rect.y
                        elif (blue.output == 'right'):
                            ghost.rect.x, ghost.rect.y = blue.rect.x + 40, blue.rect.y
                        elif (blue.output == 'up'):
                            ghost.rect.x, ghost.rect.y = blue.rect.x, blue.rect.y - 40
                        elif (blue.output == 'down'):
                            ghost.rect.x, ghost.rect.y = blue.rect.x, blue.rect.y + 40
                        pygame.time.wait(1000) # wait so can notice the change
                        self.portals.close_portal(color='blue') # close the blue portal
                
                if (pygame.sprite.collide_rect(ghost, blue)):
                    if (orange.portal_placed):
                        self.portals.close_portal(color='blue') # close the blue portal
                        if (orange.output == 'left'):
                            ghost.rect.x, ghost.rect.y = orange.rect.x - 40, orange.rect.y
                        elif (orange.output == 'right'):
                            ghost.rect.x, ghost.rect.y = orange.rect.x + 40, orange.rect.y
                        elif (orange.output == 'up'):
                            ghost.rect.x, ghost.rect.y = orange.rect.x, orange.rect.y - 40
                        elif (orange.output == 'down'):
                            ghost.rect.x, ghost.rect.y = orange.rect.x, orange.rect.y + 40
                        pygame.time.wait(1000) # wait so can notice the change
                        self.portals.close_portal(color='orange') # close the orange portal

    #Ghost AI.
    def ghost_intersection_behavior(self, ghost, pacman, intersection):
        # special code for intersection 25
        if(ghost.DEAD and intersection.number == 25):
            ghost.moving_left = False
            ghost.moving_right = False
            ghost.moving_up = False
            ghost.moving_down = True
        elif(not ghost.DEAD and intersection.number == 25 and not ghost.last_intersection == intersection.number):
            ghost.moving_left = False
            ghost.moving_right = False
            ghost.moving_up = False
            ghost.moving_down = False
            if ((pacman.rect.x <= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.left):
                ghost.moving_left = True
            elif ((pacman.rect.x >= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.right):
                ghost.moving_right = True
            else: # failsafe because ghosts keep getting stuck in the shield
                ghost.moving_left = True
            ghost.last_intersection = intersection.number

        if(not ghost.DEAD and intersection.number == 23 or ghost.last_intersection == 23 and intersection.left):
            ghost.moving_left = False
            ghost.moving_right = False
            ghost.moving_up = False
            if (pacman.rect.y <= ghost.rect.y):
                ghost.moving_down = True
            else:
                ghost.moving_left = True

        # intersection 30 is the one in the box
        elif(intersection.number == 31):
            ghost.moving_left = False
            ghost.moving_right = False
            ghost.moving_up = True
            ghost.moving_down = False

            ghost.DEAD = False
            ghost.afraid = False

        # x,y = 351, 234 is the location of intersection number 25, the entrance of the box
        elif(ghost.DEAD):
            self.go_home(ghost, intersection)
            ghost.last_intersection = intersection.number

        elif(ghost.afraid): #if afraid, run from pacman
            ghost.moving_left = False
            ghost.moving_right = False
            ghost.moving_up = False
            ghost.moving_down = False
            if (pacman.rect.x <= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3):
                ghost.moving_right = True
            elif (pacman.rect.x >= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3):
                ghost.moving_left = True
            if (pacman.rect.y <= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3):
                ghost.moving_down = True
            elif(pacman.rect.y >= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3):
                ghost.moving_up = True

        elif(randint(1,100) <= 25 and not ghost.last_intersection == intersection.number): # go in a random direction every once in a while
            ghost.moving_left = False
            ghost.moving_right = False
            ghost.moving_up = False
            ghost.moving_down = False
            while(True):
                if (randint(0, 1) == 0 and intersection.left):
                    ghost.moving_left = True
                    break
                elif (randint(0, 1) == 0 and intersection.right):
                    ghost.moving_right = True
                    break
                elif (randint(0, 1) == 0 and intersection.up):
                    ghost.moving_up = True
                    break
                elif (randint(0, 1) == 0 and intersection.down):
                    ghost.moving_down = True
                    break
            ghost.last_intersection = intersection.number

        elif((abs(pacman.rect.x - ghost.rect.x) <= abs(pacman.rect.y - ghost.rect.y)) 
             and not ghost.last_intersection == intersection.number):
            ghost.moving_left = False
            ghost.moving_right = False
            ghost.moving_up = False
            ghost.moving_down = False
            if(intersection.up or intersection.down):
                if ((pacman.rect.y <= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3) and intersection.up):
                    ghost.moving_up = True
                elif ((pacman.rect.y >= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3) and intersection.down):
                    ghost.moving_down = True
                elif(intersection.left or intersection.right):
                    if (intersection.left):
                        ghost.moving_left = True
                    elif (intersection.right):
                        ghost.moving_right = True
            elif(intersection.left or intersection.right):
                if ((pacman.rect.x <= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.left):
                    ghost.moving_left = True
                elif ((pacman.rect.x >= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.right):
                    ghost.moving_right = True
                elif (intersection.up or intersection.down):
                    if (intersection.up):
                        ghost.moving_up = True
                    elif (intersection.down):
                        ghost.moving_down = True
            ghost.last_intersection = intersection.number

        elif ((abs(pacman.rect.x - ghost.rect.x) >= abs(pacman.rect.y - ghost.rect.y))
              and not ghost.last_intersection == intersection.number):
            ghost.moving_left = False
            ghost.moving_right = False
            ghost.moving_up = False
            ghost.moving_down = False
            if (intersection.left or intersection.right):
                if ((pacman.rect.x <= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.left):
                    ghost.moving_left = True
                elif ((pacman.rect.x >= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.right):
                    ghost.moving_right = True
                elif (intersection.up or intersection.down):
                    if (intersection.up):
                        ghost.moving_up = True
                    elif (intersection.down):
                        ghost.moving_down = True
            elif (intersection.up or intersection.down):
                if ((pacman.rect.y <= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3) and intersection.up):
                    ghost.moving_up = True
                elif ((pacman.rect.y >= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3) and intersection.down):
                    ghost.moving_down = True
                elif (intersection.left or intersection.right):
                    if (intersection.left):
                        ghost.moving_left = True
                    elif (intersection.right):
                        ghost.moving_right = True
            ghost.last_intersection = intersection.number