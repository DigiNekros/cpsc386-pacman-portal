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

        # Grouping blocks and pellets and ghosts
        # self.blocks = Group()
        self.blocks = Maze(screen=self.screen)
        self.powerpills = PowerPills(screen=self.screen)
        # self.powerpills = Group()
        # self.shield = Group()
        self.shield = Shields(screen=self.screen)
        self.portals = Portals(screen=self.screen)
        # self.portals = Group()
        self.ghosts = Group()
        self.intersections = Group()
        self.fruit = Fruit(self.screen)

        self.thepacman = Pacman(self.screen, self.gamesettings)

        # Making the ghosts
        redghost = Ghosts(self.screen, "red")
        cyanghost = Ghosts(self.screen, "cyan")
        orangeghost = Ghosts(self.screen, "orange")
        pinkghost = Ghosts(self.screen, "pink")
        
        self.ghosts.add(redghost)
        self.ghosts.add(cyanghost)
        self.ghosts.add(orangeghost)
        self.ghosts.add(pinkghost)
        
        # Making the two portals
        self.orange = Portal(self.screen, "orange")
        self.blue = Portal(self.screen, "blue")
        
        self.portals.add_portal(self.orange)
        self.portals.add_portal(self.blue)
        
        # self.startScreen.makeScreen(self.screen, self.gamesettings)
        self.fruit.fruitReset()
        gf.readFile(self.screen, self.blocks, self.shield, self.powerpills, self.intersections)
        
        self.frames = 0 # for the victory fanfare and death animation
        
        # play intro chime
        self.playIntro = True
        
    def __str__(self):
        return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'
    
    def check_start(self):
        if not self.gamesettings.game_active:
            self.startScreen.makeScreen(self.screen, self.gamesettings)

    def check_win(self):
        if (len(self.powerpills) == 0):
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
        for ghost in self.ghosts:
            ghost.resetPosition()
            ghost.speed += 1
    
    def next_level(self):
        self.reset()
        self.showgamestats.level += 1
        self.fruit.fruitReset()
        gf.readFile(self.screen, self.blocks, self.shield, self.powerpills, self.intersections)
        self.frames = 0
        pygame.time.wait(1000)

    def game_over(self):
        #reset game and save score
        self.screen.fill(BLACK)
        pygame.time.wait(2000)
        self.gamesettings.game_active = False
        self.thepacman.resetPosition()
        for ghost in self.ghosts:
                ghost.resetPosition()
                ghost.speed = 1
        self.showgamestats.num_lives = 3
        self.showgamestats.save_hs_to_file()
        self.showgamestats.score = 0
        self.showgamestats.level = 1
        self.fruit.fruitReset()
        self.playIntro = True # reset the chime
        gf.readFile(self.screen, self.blocks, self.shield, self.powerpills, self.intersections)
        self.startScreen.makeScreen(self.screen, self.gamesettings)

    def check_game_over(self):
        if(self.showgamestats.num_lives < 0):
            self.game_over()

    def play(self):
        # self.screen.fill(BLACK)
        while True:
            gf.check_events(self.thepacman, self.powerpills, self.gamesettings, self.orange, self.blue)
            self.check_start()
            if(self.gamesettings.game_active):
                pygame.time.Clock().tick(120) #120 fps lock
                self.screen.fill(BLACK)
                self.showgamestats.blitstats()
                # gf.check_events(self.thepacman, self.powerpills, self.gamesettings, self.orange, self.blue)
                # gf.check_collision(self.thepacman, self.blocks, self.powerpills, self.shield, self.ghosts, 
                #                    self.intersections, self.showgamestats, self.gamesettings, self.fruit, 
                #                    self.orange, self.blue)
                self.blocks.draw()
                self.shield.draw()
                self.powerpills.draw()
                self.portals.draw()
                for ghost in self.ghosts:
                    ghost.blitghosts()
                    ghost.update()
                    if(ghost.DEAD):
                        ghost.playRetreatSound()
                    elif(ghost.afraid):
                        ghost.playAfraidSound()# if ghosts are afraid, loop their sound
                for intersection in self.intersections:
                    intersection.blit()
                self.fruit.blitfruit()
                self.thepacman.blitpacman()
                self.thepacman.update()
                self.check_win()
                self.check_if_play_intro_sound()
                
            elif(self.gamesettings.victory_fanfare):
                if(self.frames <= 120):
                    for block in self.blocks:
                        block.color = ((255,255,255))
                        block.blitblocks()
                elif(self.frames <= 240):
                    for block in self.blocks:
                        block.color = ((0,0,255))
                        block.blitblocks()
                elif (self.frames <= 360):
                    for block in self.blocks:
                        block.color = ((255, 255, 255))
                        block.blitblocks()
                elif (self.frames <= 480):
                    for block in self.blocks:
                        block.color = ((0, 0, 255))
                        block.blitblocks()
                else:
                    self.next_level()
                self.frames += 1
            elif(self.thepacman.DEAD):
                self.thepacman.deathAnimation(self.frames)
                self.frames += 1
                if(self.frames > 600):
                    self.gamesettings.game_active = True
                    self.thepacman.DEAD = False
                    self.thepacman.resetPosition()
                    for ghost in self.ghosts:
                        ghost.resetPosition()
                    self.frames = 0
                    pygame.time.wait(1000)
            
            self.check_game_over()
            pygame.display.flip()


def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    main()


# def Game():
    # pygame.init()

    # gamesettings = Settings()
    # screen = pygame.display.set_mode((gamesettings.screen_width, gamesettings.screen_height))
    # pygame.display.set_caption("Pacman Portal")

    # # Start screen
    # showgamestats = GameStats(screen, gamesettings)
    # startScreen = StartScreen(screen, gamesettings, showgamestats)

    # # Grouping blocks and pellets and ghosts
    # blocks = Group()
    # powerpills = Group()
    # shield = Group()
    # portals = Group()
    # ghosts = Group()
    # intersections = Group()
    # fruit = Fruit(screen)

    # thepacman = Pacman(screen, gamesettings)

    # # Making the ghosts
    # redghost = Ghosts(screen, "red")
    # cyanghost = Ghosts(screen, "cyan")
    # orangeghost = Ghosts(screen, "orange")
    # pinkghost = Ghosts(screen, "pink")

    # ghosts.add(redghost)
    # ghosts.add(cyanghost)
    # ghosts.add(orangeghost)
    # ghosts.add(pinkghost)

    # # Making the two portals
    # orange = Portal(screen, "orange")
    # blue = Portal(screen, "blue")

    # portals.add(orange)
    # portals.add(blue)

    # startScreen.makeScreen(screen, gamesettings)
    # fruit.fruitReset()
    # gf.readFile(screen, blocks, shield, powerpills, intersections)

    # frames = 0 # for the victory fanfare and death animation

    # # play intro chime
    # playIntro = True

    # screen.fill(BLACK)
    # while True:
    #     if(gamesettings.game_active):
    #         pygame.time.Clock().tick(120) #120 fps lock
    #         screen.fill(BLACK)
    #         showgamestats.blitstats()
    #         gf.check_events(thepacman, powerpills, gamesettings, orange, blue)
    #         gf.check_collision(thepacman, blocks, powerpills, shield, ghosts, intersections, showgamestats, gamesettings, fruit, orange, blue)
    #         for block in blocks:
    #             block.blitblocks()
    #         for theshield in shield:
    #             theshield.blitshield()
    #         for pill in powerpills:
    #             pill.blitpowerpills()
    #         for portal in portals:
    #             portal.blitportal()
    #         for ghost in ghosts:
    #             ghost.blitghosts()
    #             ghost.update()
    #             if(ghost.DEAD):
    #                 ghost.playRetreatSound()
    #             elif(ghost.afraid):
    #                 ghost.playAfraidSound()# if ghosts are afraid, loop their sound
    #         for intersection in intersections:
    #             intersection.blit()
    #         fruit.blitfruit()
    #         thepacman.blitpacman()
    #         thepacman.update()

    #         if (len(powerpills) == 0):
    #             gamesettings.game_active = False
    #             gamesettings.victory_fanfare = True
    #         if (playIntro and pygame.time.get_ticks() % 200 <= 50):
    #             mixer.Channel(2).play(pygame.mixer.Sound('sounds/pacman_beginning.wav'))
    #             pygame.time.wait(4500)
    #             playIntro = False
    #     elif(gamesettings.victory_fanfare):
    #         if(frames <= 120):
    #             for block in blocks:
    #                 block.color = ((255,255,255))
    #                 block.blitblocks()
    #         elif(frames <= 240):
    #             for block in blocks:
    #                 block.color = ((0,0,255))
    #                 block.blitblocks()
    #         elif (frames <= 360):
    #             for block in blocks:
    #                 block.color = ((255, 255, 255))
    #                 block.blitblocks()
    #         elif (frames <= 480):
    #             for block in blocks:
    #                 block.color = ((0, 0, 255))
    #                 block.blitblocks()
    #         else:
    #             gamesettings.game_active = True
    #             gamesettings.victory_fanfare = False
    #             thepacman.resetPosition()
    #             for ghost in ghosts:
    #                 ghost.resetPosition()
    #                 ghost.speed += 1
    #             showgamestats.level += 1
    #             fruit.fruitReset()
    #             gf.readFile(screen, blocks, shield, powerpills, intersections)
    #             frames = 0
    #             pygame.time.wait(1000)
    #         frames += 1
    #     elif(thepacman.DEAD):
    #         thepacman.deathAnimation(frames)
    #         frames += 1
    #         if(frames > 600):
    #             gamesettings.game_active = True
    #             thepacman.DEAD = False
    #             thepacman.resetPosition()
    #             for ghost in ghosts:
    #                 ghost.resetPosition()
    #             frames = 0
    #             pygame.time.wait(1000)

    #     if(showgamestats.num_lives < 0):
    #         #reset game and save score
    #         screen.fill(BLACK)
    #         pygame.time.wait(2000)
    #         gamesettings.game_active = False
    #         thepacman.resetPosition()
    #         for ghost in ghosts:
    #             ghost.resetPosition()
    #             ghost.speed = 1
    #         showgamestats.num_lives = 3
    #         showgamestats.save_hs_to_file()
    #         showgamestats.score = 0
    #         showgamestats.level = 1
    #         fruit.fruitReset()
    #         playIntro = True # reset the chime
    #         gf.readFile(screen, blocks, shield, powerpills, intersections)
    #         startScreen.makeScreen(screen, gamesettings)


    #     pygame.display.flip()


# game = Game()
# game.play()

