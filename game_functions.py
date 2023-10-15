# Anne Edwards, Miguel Mancera, Parker Nguyen
import pygame
import sys


def check_events(game):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, game)

def check_keydown_events(event, game):
    pacman = game.thepacman
    portals = game.portals
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        pacman.moving_up = True
    elif event.key == pygame.K_DOWN:
        pacman.moving_down = True
    elif event.key == pygame.K_RIGHT:
        pacman.moving_right = True
    elif event.key == pygame.K_LEFT:
        pacman.moving_left = True
    elif event.key == pygame.K_SPACE:
        pass
    elif event.key == pygame.K_o:
        portals.place_portal_orange(pacman)
    elif event.key == pygame.K_b:
        portals.place_portal_blue(pacman)

def check_keyup_events(event, game):
    pacman = game.thepacman
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        pacman.moving_right = False
    elif event.key == pygame.K_LEFT:
        pacman.moving_left = False
    elif event.key == pygame.K_UP:
        pacman.moving_up = False
    elif event.key == pygame.K_DOWN:
        pacman.moving_down = False

def readFile(blocks, shield, powerpills, intersections):
    file = open("images/otherpacmanportalmaze.txt", "r")
    contents = file.read()
    line = ''
    all_lines = []
    for chars in contents:
        if chars != '\n':
            line += chars
        else:
            all_lines.append(line)
            line = ''
    i = 0
    j = 0
    intersection_num = 0
    for rows in all_lines:
        for chars in rows:
            if chars == 'X':
                x, y = 13 * i, 13 * j
                blocks.create_block(x=x, y=y)
            elif chars == 'd':
                x, y = 13 * i, 13 * j
                powerpills.create_powerpill(x=x, y=y)
            elif chars == 'b':
                x, y = 13 * i, 13 * j
                powerpills.create_powerpill(x=x, y=y, size='big')
            elif chars == 'i':
                intersection_num+=1
                x, y, = 13 * i, 13 * j
                intersections.create_intersection(x=x, y=y, number=intersection_num)
            elif chars == 'o':
                x, y = 13 * i, 13 * j
                shield.create_shield(x=x, y=y)
            i += 1
        i = 0
        j += 1