# Anne Edwards, Miguel Mancera, Parker Nguyen
import pygame
import game_functions as gf
from pacman import Pacman
from startscreen import StartScreen
from pygame.sprite import Group
from ghosts import Ghosts
from settings import Settings
from gameStats import GameStats
from fruit import Fruit
from pygame import mixer
from portal import Portal, Portals
from blocks import Maze
from shield import Shields
from powerpills import PowerPills
from intersection import Intersections


BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

class Game:
    def __init__(self):
        pygame.init()
        self.gamesettings = Settings()
        self.screen = pygame.display.set_mode((self.gamesettings.screen_width, self.gamesettings.screen_height))
        pygame.display.set_caption("Pacman Portal")

        # Start screen
        self.showgamestats = GameStats(self.screen, self.gamesettings)
        self.startScreen = StartScreen(self.screen, self.gamesettings, self.showgamestats)
        self.frames = 0 # for the victory fanfare and death animation

        # Grouping blocks and pellets and ghosts
        self.blocks = Maze(screen=self.screen, game=self)
        self.powerpills = PowerPills(screen=self.screen)
        self.shield = Shields(screen=self.screen)
        self.portals = Portals(game=self)
        self.intersections = Intersections(screen=self.screen)
        self.ghosts = Ghosts(game=self)
        self.fruit = Fruit(self.screen)
        gf.readFile(blocks=self.blocks, shield=self.shield, powerpills=self.powerpills, intersections=self.intersections)

        self.thepacman = Pacman(game=self)

        self.ghosts.pacman = self.thepacman.returnPacman()

        # Making the ghosts
        ghostcolor = ["red", "cyan", "orange", "pink"]
        for index in range(len(ghostcolor)):
            self.ghosts.create_ghost(color=ghostcolor[index])

        self.fruit.fruitReset()

        # play intro chime
        self.playIntro = True
        
    def __str__(self):
        return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'
    
    def check_start(self):
        if not self.gamesettings.game_active and not self.gamesettings.victory_fanfare and not self.thepacman.DEAD:
            self.startScreen.makeScreen(self.screen, self)

    def check_win(self):
        if (len(self.powerpills.powerpills) == 0):
                self.gamesettings.game_active = False
                self.gamesettings.victory_fanfare = True

    def check_if_play_intro_sound(self):
        if (self.playIntro and pygame.time.get_ticks() % 200 <= 50):
                mixer.Channel(2).play(pygame.mixer.Sound('sounds/pacman_beginning.wav'))
                pygame.time.wait(4500)
                self.playIntro = False

    def reset(self):
        self.gamesettings.game_active = True
        self.gamesettings.victory_fanfare = False
        self.thepacman.resetPosition()
        self.ghosts.reset()
        self.portals.reset()
        self.ghosts.change_speed() # changes speed to += 1
    
    def next_level(self):
        self.reset()
        self.showgamestats.level += 1
        self.fruit.fruitReset()
        gf.readFile(self.blocks, self.shield, self.powerpills, self.intersections)
        self.frames = 0
        pygame.time.wait(1000)

    def game_over(self):
        #reset game and save score
        self.screen.fill(BLACK)
        pygame.time.wait(2000)
        self.gamesettings.game_active = False
        self.thepacman.resetPosition()
        self.ghosts.reset()
        self.ghosts.change_speed(reset=True) # changes speed to 1
        self.showgamestats.num_lives = 3
        self.showgamestats.save_hs_to_file()
        self.showgamestats.score = 0
        self.showgamestats.level = 1
        self.fruit.fruitReset()
        self.portals.reset()
        self.playIntro = True # reset the chime
        self.blocks.times_drawn = 0
        gf.readFile(self.blocks, self.shield, self.powerpills, self.intersections)
        self.startScreen.makeScreen(self.screen, self)

    def check_game_over(self):
        if(self.showgamestats.num_lives < 0):
            self.game_over()

    def reset_level(self):
        self.thepacman.deathAnimation(self.frames)
        self.frames += 1
        if(self.frames > 600):
            self.gamesettings.game_active = True
            self.thepacman.DEAD = False
            self.thepacman.resetPosition()
            self.ghosts.reset()
            self.portals.reset()
            self.frames = 0
            pygame.time.wait(1000)

    def play(self):
        while True:
            gf.check_events(game=self)
            self.check_start()
            if(self.gamesettings.game_active):
                pygame.time.Clock().tick(120) #120 fps lock
                self.screen.fill(BLACK)
                self.showgamestats.blitstats()
                self.powerpills.draw()
                self.portals.update()
                self.blocks.draw()
                self.shield.draw()
                self.ghosts.update()
                self.intersections.draw()
                self.fruit.blitfruit()
                self.thepacman.update()
                self.check_win()
                self.check_if_play_intro_sound()  
            elif(self.gamesettings.victory_fanfare):
                if(self.frames <= 120):
                    for block in self.blocks.blocks:
                        block.color = ((255,255,255))
                        block.blitblocks()
                elif(self.frames <= 240):
                    for block in self.blocks.blocks:
                        block.color = ((0,0,255))
                        block.blitblocks()
                elif (self.frames <= 360):
                    for block in self.blocks.blocks:
                        block.color = ((255, 255, 255))
                        block.blitblocks()
                elif (self.frames <= 480):
                    for block in self.blocks.blocks:
                        block.color = ((0, 0, 255))
                        block.blitblocks()
                else:
                    self.next_level()
                self.frames += 1
            elif(self.thepacman.DEAD):
                self.reset_level()
            self.check_game_over()
            pygame.display.flip()


def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    main()