import sys
import pygame
import pygame.font
import SpriteSheet
from pacman import Pacman
from ghosts import Ghosts

from pygame.sprite import Group
from settings import Settings
from button import Button

# Globals for ease
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class StartScreen():
    def __init__(self, screen, settings, showgamestats):
        self.screen = screen
        self.settings = settings
        self.showgamestats = showgamestats
        self.screen_rect = screen.get_rect()

        Cyan_SS = SpriteSheet.spritesheet('images/Cyan/CyanSpriteSheet.png')
        Orange_SS = SpriteSheet.spritesheet('images/Orange/OrangeSpriteSheet.png')
        Pink_SS = SpriteSheet.spritesheet('images/Pink/PinkSpriteSheet.png')
        Red_SS = SpriteSheet.spritesheet('images/Red/RedSpriteSheet.png')
        ss = SpriteSheet.spritesheet('images/PacmanSpriteSheet.png')

        # Load in ghost images
        self.image = Cyan_SS.image_at((0,190,32,38))
        self.image2 = Orange_SS.image_at((0,190,32,38))
        self.image3 = Pink_SS.image_at((0,190,32,38))
        self.image4 = Red_SS.image_at((0,190,32,38))

        # Load in Pacman image
        self.height = 125
        self.width = 125
        img = ss.image_at((0,0,32,32))
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.rect.x, self.rect.y = 310, 515
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height
        self.pacmanimage = img
        self.rect = self.pacmanimage.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        screen.fill(BLACK)

    def makeScreen(self, screen, gamesettings):

        # create second set of characters for the title screen
        titlepacman = Pacman(screen, gamesettings)
        titlepacman.rect.x, titlepacman.rect.y = 0, 280

        titleredghost = Ghosts(screen, "red")
        titleredghost.rect.x = -70
        titlecyanghost = Ghosts(screen, "cyan")
        titlecyanghost.rect.x = -105
        titleorangeghost = Ghosts(screen, "orange")
        titleorangeghost.rect.x = -140
        titlepinkghost = Ghosts(screen, "pink")
        titlepinkghost.rect.x = -175
        titlecyanghost.speed, titleorangeghost.speed, titlepinkghost.speed, titleredghost.speed = 2, 2, 2, 2

        # pygame.init()
        # pygame.display.set_caption("PACMAN")

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill(BLACK)

        # Display P in front of the PACMAN pic
        font = pygame.font.Font(None, 144)
        text1 = font.render("PA", 2, WHITE)
        textpos1 = text1.get_rect()
        textpos1 = ((self.settings.screen_width / 2) - 300, (self.settings.screen_height / 8) - 75)
        font = pygame.font.Font(None, 144)

        # Display "MAN" after the PACMAN pic
        text2 = font.render("MAN", 2, WHITE)
        textpos2 = text2.get_rect()
        textpos2 = ((self.settings.screen_width / 2), (self.settings.screen_height / 8) - 75)

       # PACMAN position
        pacman_pos = ((self.settings.screen_width / 2) - 150, (self.settings.screen_height / 8) - 55)

        # Ghosts position and text
        # Cyan Ghost
        font = pygame.font.Font(None, 44)
        text3 = font.render(" INKY", 2, (0, 255, 255))
        textpos3 = ((self.settings.screen_width / 2) - 250, (self.settings.screen_height / 4) + 20)
        background.blit(self.image,(180,220))

        # Orange Ghost
        text4 = font.render(" CLYDE", 2, (255, 165, 0))
        textpos4 = ((self.settings.screen_width / 2) - 150, (self.settings.screen_height / 4) + 20)
        background.blit(self.image2, (290, 220))

        # Pink Ghost
        text5 = font.render(" PINKY", 2, (255, 20, 147))
        textpos5 = ((self.settings.screen_width / 2) - 25, (self.settings.screen_height / 4) + 20)
        background.blit(self.image3, (410, 220))

        # Red Ghost
        text6 = font.render(" BLINKY", 2, (250, 0, 0))
        textpos6 = ((self.settings.screen_width / 2) + 100, (self.settings.screen_height / 4) + 20)
        background.blit(self.image4, (550, 220))

        # Draw onto screen
        background.blit(text1, textpos1)
        background.blit(self.pacmanimage, pacman_pos)
        background.blit(text2, textpos2)
        background.blit(text3, textpos3)
        background.blit(text4, textpos4)
        background.blit(text5, textpos5)
        background.blit(text6, textpos6)

        # Blit everything to screen
        screen.blit(self.image, (self.settings.screen_width / 2, self.settings.screen_height / 3))
        screen.blit(background, (200, 200))

        #Play button
        play_button = Button(screen, "Play")

        # High Scores button
        hs_button = Button(screen, "High Scores")
        show_hs_menu = False

        # animation
        titlepacman.moving_right = True
        titlecyanghost.moving_right = True
        titleorangeghost.moving_right = True
        titlepinkghost.moving_right = True
        titleredghost.moving_right = True

        pygame.display.flip()

        while True:
            pygame.time.Clock().tick(120)  # 120 fps lock
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    show_hs_menu = False
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    play_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
                    hs_clicked = hs_button.rect.collidepoint(mouse_x, mouse_y)
                    if(play_clicked):
                        self.settings.game_active = True
                        return
                    elif (hs_clicked):
                        show_hs_menu = True
            if(show_hs_menu):
                screen.fill(BLACK)
                pygame.font.init()
                myfont = pygame.font.SysFont(None, 40)
                score1 = myfont.render('1. ' + str(self.showgamestats.high_scores_all[0]), False, (255, 255, 255))
                score2 = myfont.render('2. ' + str(self.showgamestats.high_scores_all[1]), False, (255, 255, 255))
                score3 = myfont.render('3. ' + str(self.showgamestats.high_scores_all[2]), False, (255, 255, 255))
                notify = myfont.render('Click anywhere on the screen to go back', False, (255, 255, 255))
                screen.blit(score1, (150, 58))
                screen.blit(score2, (150, 188))
                screen.blit(score3, (150, 318))
                screen.blit(notify, (50, 400))
            else:
                if(titlepinkghost.rect.x > 850):
                    # move left
                    titlepacman.moving_right, titlepacman.moving_left = False, True
                    titlecyanghost.moving_right, titlecyanghost.moving_left, titlecyanghost.afraid = False, True, True
                    titleorangeghost.moving_right, titleorangeghost.moving_left, titleorangeghost.afraid = False, True, True
                    titlepinkghost.moving_right, titlepinkghost.moving_left, titlepinkghost.afraid = False, True, True
                    titleredghost.moving_right, titleredghost.moving_left, titleredghost.afraid = False, True, True
                elif(titlepacman.rect.x < -50):
                    # move right
                    titlepacman.moving_right, titlepacman.moving_left = True, False
                    titlecyanghost.moving_right, titlecyanghost.moving_left, titlecyanghost.afraid = True, False, False
                    titleorangeghost.moving_right, titleorangeghost.moving_left, titleorangeghost.afraid = True, False, False
                    titlepinkghost.moving_right, titlepinkghost.moving_left, titlepinkghost.afraid = True, False, False
                    titleredghost.moving_right, titleredghost.moving_left, titleredghost.afraid = True, False, False

                screen.blit(background, (0, 0))
                play_button.draw_button()
                hs_button.draw_button()

                titlepacman.blitpacman()
                titlepacman.update()
                titlecyanghost.blitghosts()
                titleorangeghost.blitghosts()
                titleredghost.blitghosts()
                titlepinkghost.blitghosts()
                titlecyanghost.update()
                titleorangeghost.update()
                titleredghost.update()
                titlepinkghost.update()


            pygame.display.flip()