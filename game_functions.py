import pygame
# from pygame.sprite import Group
import sys
# from blocks import Blocks
# from shield import Shield
# from powerpills import PowerPills
# from portal import Portal
# from intersection import Intersections
# from settings import Settings
# from gameStats import GameStats
# from random import randint

# def check_events(pacman, powerpills, gamesettings, orange, blue):
def check_events(game):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game)
            # check_keydown_events(event, pacman, orange, blue)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, game)
            # check_keyup_events(event, pacman)

# def check_keydown_events(event, pacman, portals):
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

# def check_keyup_events(event, pacman):
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
                # new = Blocks(screen)
                # new.rect.x, new.rect.y = 13 * i, 13 * j
                # blocks.add(new)
                x, y = 13 * i, 13 * j
                blocks.create_block(x=x, y=y)
            elif chars == 'd':
                # thepowerpill = Powerpills(screen)
                # thepowerpill.rect.x, thepowerpill.rect.y = 13 * i, 13 * j
                # powerpills.add(thepowerpill)
                x, y = 13 * i, 13 * j
                powerpills.create_powerpill(x=x, y=y)
            elif chars == 'b':
                # thepowerpill = Powerpills(screen, 'big')
                # thepowerpill.rect.x, thepowerpill.rect.y = 13 * i, 13 * j
                # powerpills.add(thepowerpill)
                x, y = 13 * i, 13 * j
                powerpills.create_powerpill(x=x, y=y, size='big')
            elif chars == 'i':
                # intersection = Intersections(screen, intersection_num)
                intersection_num+=1
                # intersection.rect.x, intersection.rect.y = 13 * i, 13 * j
                x, y, = 13 * i, 13 * j
                intersections.create_intersection(x=x, y=y, number=intersection_num)
                # intersections.add(intersection)
            elif chars == 'o':
                # theshield = Shield(screen)
                # theshield.rect.x, theshield.rect.y = 13 * i, 13 * j
                # shield.add(theshield)
                x, y = 13 * i, 13 * j
                shield.create_shield(x=x, y=y)
            i += 1
        i = 0
        j += 1


# Only for pac-man
# # Check direction pacman is going to compare and see if he can't go a direction anymore if he hit a block
# def check_direction(npc, block):
#     left = False
#     right = False
#     up = False
#     down = False
#     if npc.rect.centerx <= block.rect.centerx:
#         right = True
#     else:
#         left = True
#     if npc.rect.y + npc.rect.height / 2 <= block.rect.y + block.rect.height / 2:
#         up = True
#     else:
#         down = True

#     if left:
#         npc.rect.x += 1
#     elif right:
#         npc.rect.x -= 1
#     if up:
#         npc.rect.y -= 1
#     elif down:
#         npc.rect.y += 1

# #Ghost AI.
# def ghost_intersection_behavior(ghost, pacman, intersection):

#     # special code for intersection 24
#     if(ghost.DEAD and intersection.number == 24):
#         ghost.moving_left = False
#         ghost.moving_right = False
#         ghost.moving_up = False
#         ghost.moving_down = True
#     elif(not ghost.DEAD and intersection.number == 24 and not ghost.last_intersection == intersection.number):
#         ghost.moving_left = False
#         ghost.moving_right = False
#         ghost.moving_up = False
#         ghost.moving_down = False
#         if ((pacman.rect.x <= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.left):
#             ghost.moving_left = True
#         elif ((pacman.rect.x >= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.right):
#             ghost.moving_right = True
#         else: # failsafe because ghosts keep getting stuck in the shield
#             ghost.moving_left = True
#         ghost.last_intersection = intersection.number

#     # intersection 30 is the one in the box
#     elif(intersection.number == 30):
#         ghost.moving_left = False
#         ghost.moving_right = False
#         ghost.moving_up = True
#         ghost.moving_down = False

#         ghost.DEAD = False
#         ghost.afraid = False

#     # x,y = 351, 234 is the location of intersection number 24, the entrance of the box
#     elif(ghost.DEAD):
#         if ((abs(351 - ghost.rect.x) <= abs(234 - ghost.rect.y))
#               and not ghost.last_intersection == intersection.number):
#             ghost.moving_left = False
#             ghost.moving_right = False
#             ghost.moving_up = False
#             ghost.moving_down = False
#             if (intersection.up or intersection.down):
#                 if ((234 <= ghost.rect.y and abs(234 - ghost.rect.y) > 3) and intersection.up):
#                     ghost.moving_up = True
#                 elif ((234 >= ghost.rect.y and abs(234 - ghost.rect.y) > 3) and intersection.down):
#                     ghost.moving_down = True
#                 elif (intersection.left or intersection.right):
#                     if (intersection.left):
#                         ghost.moving_left = True
#                     elif (intersection.right):
#                         ghost.moving_right = True
#             elif (intersection.left or intersection.right):
#                 if ((351 <= ghost.rect.x and abs(351 - ghost.rect.x) > 3) and intersection.left):
#                     ghost.moving_left = True
#                 elif ((351 >= ghost.rect.x and abs(351 - ghost.rect.x) > 3) and intersection.right):
#                     ghost.moving_right = True
#                 elif (intersection.up or intersection.down):
#                     if (intersection.up):
#                         ghost.moving_up = True
#                     elif (intersection.down):
#                         ghost.moving_down = True
#             ghost.last_intersection = intersection.number

#         elif ((abs(351 - ghost.rect.x) >= abs(234 - ghost.rect.y))
#               and not ghost.last_intersection == intersection.number):
#             ghost.moving_left = False
#             ghost.moving_right = False
#             ghost.moving_up = False
#             ghost.moving_down = False
#             if (intersection.left or intersection.right):
#                 if ((351 <= ghost.rect.x and abs(351 - ghost.rect.x) > 3) and intersection.left):
#                     ghost.moving_left = True
#                 elif ((351 >= ghost.rect.x and abs(351 - ghost.rect.x) > 3) and intersection.right):
#                     ghost.moving_right = True
#                 elif (intersection.up or intersection.down):
#                     if (intersection.up):
#                         ghost.moving_up = True
#                     elif (intersection.down):
#                         ghost.moving_down = True
#             elif (intersection.up or intersection.down):
#                 if ((234 <= ghost.rect.y and abs(234 - ghost.rect.y) > 3) and intersection.up):
#                     ghost.moving_up = True
#                 elif ((234 >= ghost.rect.y and abs(234 - ghost.rect.y) > 3) and intersection.down):
#                     ghost.moving_down = True
#                 elif (intersection.left or intersection.right):
#                     if (intersection.left):
#                         ghost.moving_left = True
#                     elif (intersection.right):
#                         ghost.moving_right = True
#             ghost.last_intersection = intersection.number

#     elif(ghost.afraid): #if afraid, run from pacman
#         ghost.moving_left = False
#         ghost.moving_right = False
#         ghost.moving_up = False
#         ghost.moving_down = False
#         if (pacman.rect.x <= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3):
#             ghost.moving_right = True
#         elif (pacman.rect.x >= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3):
#             ghost.moving_left = True
#         if (pacman.rect.y <= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3):
#             ghost.moving_down = True
#         elif(pacman.rect.y >= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3):
#             ghost.moving_up = True

#     elif(randint(1,100) <= 25 and not ghost.last_intersection == intersection.number): # go in a random direction every once in a while
#         ghost.moving_left = False
#         ghost.moving_right = False
#         ghost.moving_up = False
#         ghost.moving_down = False
#         while(True):
#             if (randint(0, 1) == 0 and intersection.left):
#                 ghost.moving_left = True
#                 break
#             elif (randint(0, 1) == 0 and intersection.right):
#                 ghost.moving_right = True
#                 break
#             elif (randint(0, 1) == 0 and intersection.up):
#                 ghost.moving_up = True
#                 break
#             elif (randint(0, 1) == 0 and intersection.down):
#                 ghost.moving_down = True
#                 break
#         ghost.last_intersection = intersection.number

#     elif((abs(pacman.rect.x - ghost.rect.x) <= abs(pacman.rect.y - ghost.rect.y))
#         and not ghost.last_intersection == intersection.number):
#         ghost.moving_left = False
#         ghost.moving_right = False
#         ghost.moving_up = False
#         ghost.moving_down = False
#         if(intersection.up or intersection.down):
#             if ((pacman.rect.y <= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3) and intersection.up):
#                 ghost.moving_up = True
#             elif ((pacman.rect.y >= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3) and intersection.down):
#                 ghost.moving_down = True
#             elif(intersection.left or intersection.right):
#                 if (intersection.left):
#                     ghost.moving_left = True
#                 elif (intersection.right):
#                     ghost.moving_right = True
#         elif(intersection.left or intersection.right):
#             if ((pacman.rect.x <= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.left):
#                 ghost.moving_left = True
#             elif ((pacman.rect.x >= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.right):
#                 ghost.moving_right = True
#             elif (intersection.up or intersection.down):
#                 if (intersection.up):
#                     ghost.moving_up = True
#                 elif (intersection.down):
#                     ghost.moving_down = True
#         ghost.last_intersection = intersection.number

#     elif ((abs(pacman.rect.x - ghost.rect.x) >= abs(pacman.rect.y - ghost.rect.y))
#         and not ghost.last_intersection == intersection.number):
#         ghost.moving_left = False
#         ghost.moving_right = False
#         ghost.moving_up = False
#         ghost.moving_down = False
#         if (intersection.left or intersection.right):
#             if ((pacman.rect.x <= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.left):
#                 ghost.moving_left = True
#             elif ((pacman.rect.x >= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.right):
#                 ghost.moving_right = True
#             elif (intersection.up or intersection.down):
#                 if (intersection.up):
#                     ghost.moving_up = True
#                 elif (intersection.down):
#                     ghost.moving_down = True
#         elif (intersection.up or intersection.down):
#             if ((pacman.rect.y <= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3) and intersection.up):
#                 ghost.moving_up = True
#             elif ((pacman.rect.y >= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3) and intersection.down):
#                 ghost.moving_down = True
#             elif (intersection.left or intersection.right):
#                 if (intersection.left):
#                     ghost.moving_left = True
#                 elif (intersection.right):
#                     ghost.moving_right = True
#         ghost.last_intersection = intersection.number

# only for pac-man
# Check the direction pacman is going for the collision with the shield
# def check_shield_direction(pacman, shield):
#     left = False
#     right = False
#     up = False
#     down = False

#     if pacman.rect.centerx <= shield.rect.centerx:
#         right = True
#     else:
#         left = True
#     if pacman.rect.y + pacman.rect.height / 2 <= shield.rect.y + shield.rect.height / 2:
#         up = True
#     else:
#         down = True

#     if left:
#         pacman.rect.x += 1
#     elif right:
#         pacman.rect.x -= 1
#     if up:
#         pacman.rect.y -= 1
#     elif down:
#         pacman.rect.y += 1

# # Pacman and ghosts collision handling
# def check_collision(pacman, blocks, powerpills, shield, ghosts, intersections, showgamestats, gamesettings, fruit, orange, blue):
#     for block in blocks:
#         if pygame.sprite.collide_rect(pacman, block):
#             check_direction(pacman, block)
#         for ghost in ghosts:
#             if (pygame.sprite.collide_rect(ghost, block)):
#                 check_direction(ghost, block)
#     for theshield in shield:
#         if pygame.sprite.collide_rect(pacman, theshield):
#             check_shield_direction(pacman, theshield)
#     if pygame.sprite.spritecollide(pacman, powerpills, False):
#         for powerpill in powerpills:
#             if (pygame.sprite.collide_rect(pacman, powerpill)):
#                 for ghost in ghosts:
#                     if(ghost.color == 'red'):
#                         ghost.speed += .001  # speed up Blinky's (red ghost) speed for every pellet eaten
#                 powerpills.remove(powerpill)
#                 if(powerpill.size == 'big'):
#                     for ghost in ghosts:
#                         ghost.afraid = True
#                         ghost.frames = 0 # reset the afraid timer
#                     showgamestats.score += 50
#                 else:
#                     showgamestats.score += 10
#                     pacman.playPelletEatSound()
#     if pygame.sprite.collide_rect(pacman, fruit):
#         if(not fruit.destroyed):
#             showgamestats.score += fruit.value
#             fruit.destroyed = True
#             pacman.playFruitEatenSound()
#     if (pygame.sprite.spritecollide(pacman, ghosts, False)):
#         for ghost in ghosts:
#             if (pygame.sprite.collide_rect(pacman, ghost)):
#                 if(ghost.afraid and not ghost.DEAD):
#                     ghost.DEAD = True
#                     pts = 0
#                     for ghost in ghosts:
#                         if(ghost.DEAD):
#                             pts += 1
#                             ghost.value = 100 * 2**pts
#                     showgamestats.score += 100 * 2**pts
#                     ghost.playDeathSound()
#                     pygame.time.wait(500)
#                 elif(not ghost.afraid and not ghost.DEAD):
#                     pacman.DEAD = True
#                     gamesettings.game_active = False
#                     showgamestats.num_lives -= 1
#                     pacman.playDeathSound()
#                     break

#     for intersection in intersections:
#         for ghost in ghosts:
#             if(pygame.sprite.collide_rect(ghost, intersection)):
#                 ghost_intersection_behavior(ghost, pacman, intersection)

#     # portal teleport
#     if(pygame.sprite.collide_rect(pacman, orange)):
#         if(blue.portal_placed):
#             if(blue.output == 'left'):
#                 pacman.rect.x, pacman.rect.y = blue.rect.x - 40, blue.rect.y
#             elif (blue.output == 'right'):
#                 pacman.rect.x, pacman.rect.y = blue.rect.x + 40, blue.rect.y
#             elif (blue.output == 'up'):
#                 pacman.rect.x, pacman.rect.y = blue.rect.x, blue.rect.y - 40
#             elif (blue.output == 'down'):
#                 pacman.rect.x, pacman.rect.y = blue.rect.x, blue.rect.y + 40
#     if(pygame.sprite.collide_rect(pacman, blue)):
#         if(orange.portal_placed):
#             if (orange.output == 'left'):
#                 pacman.rect.x, pacman.rect.y = orange.rect.x - 40, orange.rect.y
#             elif (orange.output == 'right'):
#                 pacman.rect.x, pacman.rect.y = orange.rect.x + 40, orange.rect.y
#             elif (orange.output == 'up'):
#                 pacman.rect.x, pacman.rect.y = orange.rect.x, orange.rect.y - 40
#             elif (orange.output == 'down'):
#                 pacman.rect.x, pacman.rect.y = orange.rect.x, orange.rect.y + 40

#     if(showgamestats.level > 4): # if player beyond level 4, ghosts can enter and exit portals too
#         for ghost in ghosts:
#             if (pygame.sprite.collide_rect(ghost, orange)):
#                 if (blue.portal_placed):
#                     if (blue.output == 'left'):
#                         ghost.rect.x, ghost.rect.y = blue.rect.x - 40, blue.rect.y
#                     elif (blue.output == 'right'):
#                         ghost.rect.x, ghost.rect.y = blue.rect.x + 40, blue.rect.y
#                     elif (blue.output == 'up'):
#                         ghost.rect.x, ghost.rect.y = blue.rect.x, blue.rect.y - 40
#                     elif (blue.output == 'down'):
#                         ghost.rect.x, ghost.rect.y = blue.rect.x, blue.rect.y + 40
#             if (pygame.sprite.collide_rect(ghost, blue)):
#                 if (orange.portal_placed):
#                     if (orange.output == 'left'):
#                         ghost.rect.x, ghost.rect.y = orange.rect.x - 40, orange.rect.y
#                     elif (orange.output == 'right'):
#                         ghost.rect.x, ghost.rect.y = orange.rect.x + 40, orange.rect.y
#                     elif (orange.output == 'up'):
#                         ghost.rect.x, ghost.rect.y = orange.rect.x, orange.rect.y - 40
#                     elif (orange.output == 'down'):
#                         ghost.rect.x, ghost.rect.y = orange.rect.x, orange.rect.y + 40

# put in portal
# def place_portal_orange(pacman, orange):
#     if(pacman.last_direction == 'left'):
#         orange.rect.x, orange.rect.y = pacman.rect.x - 14, pacman.rect.y
#     elif (pacman.last_direction == 'right'):
#         orange.rect.x, orange.rect.y = pacman.rect.x + 34.5, pacman.rect.y
#     elif (pacman.last_direction == 'up'):
#         orange.rect.x, orange.rect.y = pacman.rect.x, pacman.rect.y - 14
#     elif (pacman.last_direction == 'down'):
#         orange.rect.x, orange.rect.y = pacman.rect.x, pacman.rect.y + 34.5
#     orange.rotate(pacman.last_direction)
#     orange.portal_placed = True

# # put in portal
# def place_portal_blue(pacman, blue):
#     if (pacman.last_direction == 'left'):
#         blue.rect.x, blue.rect.y = pacman.rect.x - 14, pacman.rect.y
#     elif (pacman.last_direction == 'right'):
#         blue.rect.x, blue.rect.y = pacman.rect.x + 34.5, pacman.rect.y
#     elif (pacman.last_direction == 'up'):
#         blue.rect.x, blue.rect.y = pacman.rect.x, pacman.rect.y - 14
#     elif (pacman.last_direction == 'down'):
#         blue.rect.x, blue.rect.y = pacman.rect.x, pacman.rect.y + 34.5
#     blue.rotate(pacman.last_direction)
#     blue.portal_placed = True

# Read in text file of maze and then fill in X's with a block
# def readFile(screen, blocks, shield, powerpills, intersections):
#     file = open("images/otherpacmanportalmaze.txt", "r")
#     contents = file.read()
#     line = ''
#     all_lines = []
#     for chars in contents:
#         if chars != '\n':
#             line += chars
#         else:
#             all_lines.append(line)
#             line = ''
#     i = 0
#     j = 0
#     intersection_num = 0
#     for rows in all_lines:
#         for chars in rows:
#             if chars == 'X':
#                 # new = Blocks(screen)
#                 # new.rect.x, new.rect.y = 13 * i, 13 * j
#                 # blocks.add(new)
#                 x, y = 13 * i, 13 * j
#                 blocks.create_block(x=x, y=y)
#             elif chars == 'd':
#                 # thepowerpill = Powerpills(screen)
#                 # thepowerpill.rect.x, thepowerpill.rect.y = 13 * i, 13 * j
#                 # powerpills.add(thepowerpill)
#                 x, y = 13 * i, 13 * j
#                 powerpills.create_powerpill(x=x, y=y)
#             elif chars == 'b':
#                 # thepowerpill = Powerpills(screen, 'big')
#                 # thepowerpill.rect.x, thepowerpill.rect.y = 13 * i, 13 * j
#                 # powerpills.add(thepowerpill)
#                 x, y = 13 * i, 13 * j
#                 powerpills.create_powerpill(x=x, y=y, size='big')
#             elif chars == 'i':
#                 # intersection = Intersections(screen, intersection_num)
#                 intersection_num+=1
#                 # intersection.rect.x, intersection.rect.y = 13 * i, 13 * j
#                 x, y, = 13 * i, 13 * j
#                 intersections.create_intersection(x=x, y=y, number=intersection_num)
#                 # intersections.add(intersection)
#             elif chars == 'o':
#                 # theshield = Shield(screen)
#                 # theshield.rect.x, theshield.rect.y = 13 * i, 13 * j
#                 # shield.add(theshield)
#                 x, y = 13 * i, 13 * j
#                 shield.create_shield(x=x, y=y)
#             i += 1
#         i = 0
#         j += 1

