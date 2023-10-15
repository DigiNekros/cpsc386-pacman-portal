# Anne Edwards, Miguel Mancera, Parker Nguyen
import pygame
import pygame.font
import SpriteSheet
import json
from pygame.sprite import Group
from fruit import Fruit

WHITE = (255, 255, 255)


class GameStats():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.height = 50
        self.width = 50
        ss = SpriteSheet.spritesheet('images/PacmanSpriteSheet.png')
        img = ss.image_at((0,0,32,32))
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.rect.x, self.rect.y = 310, 515
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height
        self.pacmanimage = img
        self.rect = self.pacmanimage.get_rect()
        self.pacpos = ((self.settings.screen_width / 2) + 250, (self.settings.screen_height / 8) - 25)
        self.pacpos2 = ((self.settings.screen_width / 2) + 300, (self.settings.screen_height / 8) - 25)
        self.pacpos3 = ((self.settings.screen_width / 2) + 350, (self.settings.screen_height / 8) - 25)

        # Lives display text
        self.text_color = (30, 30, 30)
        font = pygame.font.Font(None, 72)
        self.font = pygame.font.SysFont(None, 48)
        self.Livestext = font.render("LIVES ", 2, WHITE)
        self.Livespos = self.Livestext.get_rect()
        self.Livespos = ((self.settings.screen_width / 2) + 250, (self.settings.screen_height / 8) - 75)

        # Score display text
        self.text_color = (30, 30, 30)
        font = pygame.font.Font(None, 72)
        self.font = pygame.font.SysFont(None, 48)
        self.scores = font.render("SCORE ", 2, WHITE)
        self.scorespos = self.scores.get_rect()
        self.scorespos = ((self.settings.screen_width / 2) + 225, (self.settings.screen_height / 8) + 100)

        # Score number display text
        self.score = 0 # score holder
        self.text_color = (30, 30, 30)
        font = pygame.font.Font(None, 72)
        self.font = pygame.font.SysFont(None, 48)
        self.number = font.render(str(self.score), 2, WHITE)
        self.numberpos = self.number.get_rect()
        self.numberpos = ((self.settings.screen_width / 2) + 250, (self.settings.screen_height / 8) + 150)

        # Number of lives
        self.num_lives = 3

        # The current level
        self.level = 1

        """Read the saved high score from the json file on disk (if it exists)"""
        try:
            with open('high_scores.json', 'r') as file:
                self.high_scores_all = json.load(file)  # Cast to int to verify type
                self.high_scores_all.sort(reverse=True)
        except (FileNotFoundError, ValueError, EOFError, json.JSONDecodeError, AttributeError, IndexError) as e:
            print(e)
            self.high_scores_all = [0, 0, 0]  # Some issue with the file, going to default

    def prep_level(self):
        self.fruits = Group()
        for fruit_num in range(self.level):
            fruit = Fruit(self.screen, type=0)
            fruit.rect.x, fruit.rect.y = self.scorespos
            fruit.rect.x += 70
            if fruit_num == 0:
                fruit.rect.y += 140
            else:
                fruit.rect.y = fruit.rect.y + 140 + fruit_num * fruit.rect.height
            self.fruits.add(fruit)

    def blitstats(self):
        self.screen.blit(self.Livestext, self.Livespos)
        if(self.num_lives == 3):
            self.screen.blit(self.pacmanimage, self.pacpos)
            self.screen.blit(self.pacmanimage, self.pacpos2)
            self.screen.blit(self.pacmanimage, self.pacpos3)
        elif(self.num_lives == 2):
            self.screen.blit(self.pacmanimage, self.pacpos2)
            self.screen.blit(self.pacmanimage, self.pacpos3)
        elif(self.num_lives == 1):
            self.screen.blit(self.pacmanimage, self.pacpos3)
        self.screen.blit(self.scores, self.scorespos)
        self.screen.blit(self.number, self.numberpos)

        self.prep_level()

        for fruit in self.fruits:
            self.screen.blit(fruit.image, fruit.rect)

        font = pygame.font.Font(None, 72)
        self.number = font.render(str(self.score), 2, WHITE)

    def save_hs_to_file(self):
        """Save the high score to a json file on disk"""
        for i in range(len(self.high_scores_all)):
            if self.score >= self.high_scores_all[i]:
                if(not i == 2): # avoid index out of bounds
                    self.high_scores_all[i + 1] = self.high_scores_all[i]
                    self.high_scores_all[i] = self.score
                else:
                    self.high_scores_all[i] = self.score
                break
        with open('high_scores.json', 'w') as file:
            json.dump(self.high_scores_all, file)