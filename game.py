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
from portal import Portal


BLACK = (0, 0, 0)
WHITE = (250, 250, 250)


def __str__(self):
    return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'


def Game():
    pygame.init()

    gamesettings = Settings()
    screen = pygame.display.set_mode((gamesettings.screen_width, gamesettings.screen_height))
    pygame.display.set_caption("Pacman Portal")

    # Start screen
    showgamestats = GameStats(screen, gamesettings)
    startScreen = StartScreen(screen, gamesettings, showgamestats)

    # Grouping blocks and pellets and ghosts
    blocks = Group()
    powerpills = Group()
    shield = Group()
    portals = Group()
    ghosts = Group()
    intersections = Group()
    fruit = Fruit(screen)

    thepacman = Pacman(screen, gamesettings)

    # Making the ghosts
    redghost = Ghosts(screen, "red")
    cyanghost = Ghosts(screen, "cyan")
    orangeghost = Ghosts(screen, "orange")
    pinkghost = Ghosts(screen, "pink")

    ghosts.add(redghost)
    ghosts.add(cyanghost)
    ghosts.add(orangeghost)
    ghosts.add(pinkghost)

    # Making the two portals
    orange = Portal(screen, "orange")
    blue = Portal(screen, "blue")

    portals.add(orange)
    portals.add(blue)

    startScreen.makeScreen(screen, gamesettings)
    fruit.fruitReset()
    gf.readFile(screen, blocks, shield, powerpills, intersections)

    frames = 0 # for the victory fanfare and death animation

    # play intro chime
    playIntro = True

    screen.fill(BLACK)
    while True:
        if(gamesettings.game_active):
            pygame.time.Clock().tick(120) #120 fps lock
            screen.fill(BLACK)
            showgamestats.blitstats()
            gf.check_events(thepacman, powerpills, gamesettings, orange, blue)
            gf.check_collision(thepacman, blocks, powerpills, shield, ghosts, intersections, showgamestats, gamesettings, fruit, orange, blue)
            for block in blocks:
                block.blitblocks()
            for theshield in shield:
                theshield.blitshield()
            for pill in powerpills:
                pill.blitpowerpills()
            for portal in portals:
                portal.blitportal()
            for ghost in ghosts:
                ghost.blitghosts()
                ghost.update()
                if(ghost.DEAD):
                    ghost.playRetreatSound()
                elif(ghost.afraid):
                    ghost.playAfraidSound()# if ghosts are afraid, loop their sound
            for intersection in intersections:
                intersection.blit()
            fruit.blitfruit()
            thepacman.blitpacman()
            thepacman.update()

            if (len(powerpills) == 0):
                gamesettings.game_active = False
                gamesettings.victory_fanfare = True
            if (playIntro and pygame.time.get_ticks() % 200 <= 50):
                mixer.Channel(2).play(pygame.mixer.Sound('sounds/pacman_beginning.wav'))
                pygame.time.wait(4500)
                playIntro = False
        elif(gamesettings.victory_fanfare):
            if(frames <= 120):
                for block in blocks:
                    block.color = ((255,255,255))
                    block.blitblocks()
            elif(frames <= 240):
                for block in blocks:
                    block.color = ((0,0,255))
                    block.blitblocks()
            elif (frames <= 360):
                for block in blocks:
                    block.color = ((255, 255, 255))
                    block.blitblocks()
            elif (frames <= 480):
                for block in blocks:
                    block.color = ((0, 0, 255))
                    block.blitblocks()
            else:
                gamesettings.game_active = True
                gamesettings.victory_fanfare = False
                thepacman.resetPosition()
                for ghost in ghosts:
                    ghost.resetPosition()
                    ghost.speed += 1
                showgamestats.level += 1
                fruit.fruitReset()
                gf.readFile(screen, blocks, shield, powerpills, intersections)
                frames = 0
                pygame.time.wait(1000)
            frames += 1
        elif(thepacman.DEAD):
            thepacman.deathAnimation(frames)
            frames += 1
            if(frames > 600):
                gamesettings.game_active = True
                thepacman.DEAD = False
                thepacman.resetPosition()
                for ghost in ghosts:
                    ghost.resetPosition()
                frames = 0
                pygame.time.wait(1000)

        if(showgamestats.num_lives < 0):
            #reset game and save score
            screen.fill(BLACK)
            pygame.time.wait(2000)
            gamesettings.game_active = False
            thepacman.resetPosition()
            for ghost in ghosts:
                ghost.resetPosition()
                ghost.speed = 1
            showgamestats.num_lives = 3
            showgamestats.save_hs_to_file()
            showgamestats.score = 0
            showgamestats.level = 1
            fruit.fruitReset()
            playIntro = True # reset the chime
            gf.readFile(screen, blocks, shield, powerpills, intersections)
            startScreen.makeScreen(screen, gamesettings)


        pygame.display.flip()


game = Game()
game.play()

