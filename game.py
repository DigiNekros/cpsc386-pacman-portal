# Anne Edwards, Miguel Mancera, Parker Nguyen
# CPSC 386-03

from settings import Settings
import pygame as pg
import sys
# import game_functions as gf
# from pacman import Pacman
# from startscreen import StartScreen
from pygame.sprite import Group
# from ghosts import Ghosts
# from game_stats import GameStats
# from fruit import Fruit
# from pygame import mixer
# from portal import Portal
from maze import Maze
from events import Events
# from graph import Graph

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        screen_size = (self.settings.screen_width, self.settings.screen_height)
        self.screen = pg.display.set_mode(screen_size)
        self.clock = pg.time.Clock()
        pg.display.set_caption("Pac-Man Portal")

        # Start screen
        # self.game_stats = GameStats(self.screen, self.settings)
        # self.startscreen = StartScreen(self.screen, self.settings, self.game_stats)

        # Grouping blocks, pellets, and ghosts
        self.blocks = Group()
        self.power_pills = Group()
        self.points = Group()
        self.shield = Group()
        self.portals = Group()
        self.ghosts = Group()
        self.intersections = Group()
        # self.fruit = Fruit(self.screen)
        self.maze = Maze(game=self, file='maze.txt')
        # self.maze.create_maze()

        # Making the characters
        # self.the_pac_man = Pacman(game=self)
        # # Making the ghosts
        # red_ghost = Ghosts(self.screen, "red")
        # cyan_ghost = Ghosts(self.screen, "cyan")
        # orange_ghost = Ghosts(self.screen, "orange")
        # pink_ghost = Ghosts(self.screen, "pink")

        # Add ghosts to the group
        # self.ghosts.add(red_ghost)
        # self.ghosts.add(cyan_ghost)
        # self.ghosts.add(orange_ghost)
        # self.ghosts.add(pink_ghost)

        # Making the two portals
        # orange_portal = Portal(self.screen, "orange")
        # blue_portal = Portal(self.screen, "blue")
        # self.portals.add(orange_portal, blue_portal)

    def __str__(self):
        return 'Game(Pac-Man Portal), maze = ' + str(self.maze) + ')'
    
    def play(self):
        while True:
            Events.handle_events(game=self)
            self.screen.fill(self.settings.bg_color)
            # print('Drawing the maze')
            self.maze.draw()
            # print('Flipping')
            pg.display.flip()
            self.clock.tick(120)


def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    main()


#     startScreen.makeScreen(screen, gamesettings)
#     fruit.fruitReset()
#     gf.readFile(screen, blocks, shield, powerpills, intersections)

#     frames = 0 # for the victory fanfare and death animation

#     # play intro chime
#     playIntro = True

#     screen.fill(BLACK)
#     while True:
#         if(gamesettings.game_active):
#             pygame.time.Clock().tick(120) #120 fps lock
#             screen.fill(BLACK)
#             showgamestats.blitstats()
#             gf.check_events(thepacman, powerpills, gamesettings, orange, blue)
#             gf.check_collision(thepacman, blocks, powerpills, shield, ghosts, intersections, showgamestats, gamesettings, fruit, orange, blue)
#             for block in blocks:
#                 block.blitblocks()
#             for theshield in shield:
#                 theshield.blitshield()
#             for pill in powerpills:
#                 pill.blitpowerpills()
#             for portal in portals:
#                 portal.blitportal()
#             for ghost in ghosts:
#                 ghost.blitghosts()
#                 ghost.update()
#                 if(ghost.DEAD):
#                     ghost.playRetreatSound()
#                 elif(ghost.afraid):
#                     ghost.playAfraidSound()# if ghosts are afraid, loop their sound
#             for intersection in intersections:
#                 intersection.blit()
#             fruit.blitfruit()
#             thepacman.blitpacman()
#             thepacman.update()

#             if (len(powerpills) == 0):
#                 gamesettings.game_active = False
#                 gamesettings.victory_fanfare = True
#             if (playIntro and pygame.time.get_ticks() % 200 <= 50):
#                 mixer.Channel(2).play(pygame.mixer.Sound('sounds/pacman_beginning.wav'))
#                 pygame.time.wait(4500)
#                 playIntro = False
#         elif(gamesettings.victory_fanfare):
#             if(frames <= 120):
#                 for block in blocks:
#                     block.color = ((255,255,255))
#                     block.blitblocks()
#             elif(frames <= 240):
#                 for block in blocks:
#                     block.color = ((0,0,255))
#                     block.blitblocks()
#             elif (frames <= 360):
#                 for block in blocks:
#                     block.color = ((255, 255, 255))
#                     block.blitblocks()
#             elif (frames <= 480):
#                 for block in blocks:
#                     block.color = ((0, 0, 255))
#                     block.blitblocks()
#             else:
#                 gamesettings.game_active = True
#                 gamesettings.victory_fanfare = False
#                 thepacman.resetPosition()
#                 for ghost in ghosts:
#                     ghost.resetPosition()
#                     ghost.speed += 1
#                 showgamestats.level += 1
#                 fruit.fruitReset()
#                 gf.readFile(screen, blocks, shield, powerpills, intersections)
#                 frames = 0
#                 pygame.time.wait(1000)
#             frames += 1
#         elif(thepacman.DEAD):
#             thepacman.deathAnimation(frames)
#             frames += 1
#             if(frames > 600):
#                 gamesettings.game_active = True
#                 thepacman.DEAD = False
#                 thepacman.resetPosition()
#                 for ghost in ghosts:
#                     ghost.resetPosition()
#                 frames = 0
#                 pygame.time.wait(1000)

#         if(showgamestats.num_lives < 0):
#             #reset game and save score
#             screen.fill(BLACK)
#             pygame.time.wait(2000)
#             gamesettings.game_active = False
#             thepacman.resetPosition()
#             for ghost in ghosts:
#                 ghost.resetPosition()
#                 ghost.speed = 1
#             showgamestats.num_lives = 3
#             showgamestats.save_hs_to_file()
#             showgamestats.score = 0
#             showgamestats.level = 1
#             fruit.fruitReset()
#             playIntro = True # reset the chime
#             gf.readFile(screen, blocks, shield, powerpills, intersections)
#             startScreen.makeScreen(screen, gamesettings)


#         pygame.display.flip()


# game = Game()
# game.play()
