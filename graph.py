# Anne Edwards, Miguel Mancera, Parker Nguyen
# CPSC 386-03

import pygame as pg
from pathlib import Path
from pygame.sprite import Sprite, Group
import file_functions as f

right = {1:2, 2:3, 4:5, 5:6, 7:8, 8:9, 9:10, 10:11, 11:12, 12:13, 13:14, 15:16, 17:18, 19:20, 21:22, 23:24, 24:25, 
         25:26, 26:27, 28:29, 29:30, 32:33, 33:34, 35:36, 36:37, 38:39, 39:40, 40:41, 42:43, 43:44, 44:45, 46:47, 
         48:49, 49:50, 50:51, 51:52, 52:53, 54:55, 56:57, 57:58, 59:60, 61:62, 63:64, 64:65, 66:67, 67:68, 68:69}

left = {2:1, 3:2, 5:4, 6:5, 8:7, 9:8, 10:9, 11:10, 12:11, 13:12, 14:13, 16:15, 18:17, 20:19, 22:21, 24:23, 25:24, 
        26:25, 27:26, 29:28, 30:29, 33:32, 34:33, 36:35, 37:36, 39:38, 40:39, 41:40, 43:42, 44:43, 45:44, 47:46,
        49:48, 50:49, 51:50, 52:51, 53:52, 55:54, 57:56, 58:57, 60:59, 62:61, 64:63, 65:64, 67:66, 68:67, 69:68}

up = {7:1, 8:2, 10:3, 11:4, 13:5, 14:6, 15:7, 16:8, 17:9, 20:12, 21:13, 22:14, 24:18, 26:19, 29:16, 30:23, 31:25, 
      32:27, 33:21, 35:30, 37:32, 39:29, 40:35, 43:37, 44:33, 46:38, 48:39, 50:41, 51:42, 53:44, 55:45, 57:47,
      58:48, 59:49, 62:52, 63:53, 64:54, 66:56, 67:60, 68:61, 69:65}

down = {1:7, 2:8, 3:10, 4:11, 5:13, 6:14, 7:15, 8:16, 9:17, 12:20, 13:21, 14:22, 16:29, 18:24, 19:26, 21:33, 23:30,
        25:31, 27:32, 29:39, 30:35, 32:37, 33:44, 35:40, 37:43, 38:46, 39:48, 41:50, 42:51, 44:53, 45:55, 47:57, 48:58,
        49:59, 52:62, 53:63, 54:64, 56:66, 60:67, 61:68, 65:69}

graph = {1:[2, 7], 2:[1, 3, 8], 3:[2, 10], 4:[5, 11], 5:[4, 6, 13], 6:[5, 14], 7:[1, 8, 15], 8:[2, 7, 9, 16],
         9:[8, 10, 17], 10:[3, 9, 11], 11:[4, 10, 12], 12:[11, 13, 20], 13:[5, 12, 14, 21], 14:[6, 13, 22],
         15:[7, 16], 16:[8, 15, 29], 17:[9, 18], 18:[17, 24], 19:[20, 26], 20:[12, 19], 21:[13, 22, 33], 22:[14, 21],
         23:[24, 30], 24:[18, 23, 25, 27], 25:[24, 26, 31], 26:[19, 25, 27], 27:[26, 32], 28:[29], 29:[16, 28, 30, 39],
         30:[23, 29, 35], 31:[25], 32:[27, 33, 37], 33:[21, 32, 34, 44], 34:[33], 35:[30, 36, 40], 36:[35, 37],
         37:[32, 36, 43], 38:[39, 46], 39:[29, 38, 40, 48], 40:[35, 39, 41], 41:[40, 50], 42:[43, 51], 43:[37, 42, 44],
         44:[33, 43, 45, 53], 45:[44, 55], 46:[38, 47], 47:[46, 57], 48:[39, 49, 58], 49:[48, 50, 52, 59], 
         50:[41, 49, 51], 51:[42, 50, 52], 52:[51, 53, 62], 53:[44, 52, 63], 54:[55, 64], 55:[45, 54], 56:[57, 66], 
         57:[47, 56, 58], 58:[48, 57], 59:[49, 60], 60:[59, 67], 61:[62, 68], 62:[52, 61], 63:[53, 64], 64:[54, 63, 65],
         65:[64, 69], 66:[56, 67], 67:[60, 66, 68], 68:[61, 67, 69], 69:[65, 68]}

GREEN = (0, 255, 0)

class Node(Sprite):
    def __init__(self, game, x, y, number):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.number = number
        self.rect = pg.Rect(0, 0, self.settings.node_width, self.settings.node_height)
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self):
        pg.draw.rect(self.screen, GREEN, self.rect)


class Graph:
    def __init__(self, game, file):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.width = self.settings.node_width
        self.height = self.settings.node_height
        self.file = file
        self.rows = []
        self.nodes = Group()
        self.top = 20
        self.y = self.top
        self.left = 8
        self.graph = graph
        self.right_movements = right
        self.left_movements = left
        self.up_movements = up
        self.down_movements = down

        f.read_file(list=self.rows, file=self.file)
        self.place_graph()

    def set_side(self):
        self.x = self.left

    def place_graph(self):
        number = 1
        i = 0
        while i < len(self.rows):
            row = self.rows[i]
            self.set_side() # get the initial x position
            iterator = 0
            while iterator < len(row):
                char = row[iterator]
                if char == 'v':
                    node = Node(game=self.game, x=self.x, y=self.y, number=number)
                    self.nodes.add(node)
                    number += 1
                self.x += self.width
                iterator += 1
            self.y += self.height
            i += 1

    def search_nodes(self, num):
        for node in self.nodes.sprites():
            if node.number == num:
                return node

    def draw(self):
        for node in self.nodes.sprites():
            node.draw()

            dir_list = graph[node.number]
            i = 0
            while i < len(dir_list):
                node_num = dir_list[i]
                for temp_node in self.nodes.sprites():
                    if temp_node.number == node_num:
                        pg.draw.line(self.screen, GREEN, (node.rect.centerx, node.rect.centery), 
                                     (temp_node.rect.centerx, temp_node.rect.centery), 4)
                        break
                i += 1
