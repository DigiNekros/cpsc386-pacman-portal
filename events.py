# Anne Edwards, Miguel Mancera, Parker Nguyen
# CPSC 386-03

import pygame as pg
import sys


class Events:
    @staticmethod
    def handle_events(game):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                Events.check_keydown_events(game, event)

    @staticmethod
    def check_keydown_events(game, event):
        key = event.key
        if key == pg.K_q:
            pg.quit()
            sys.exit()