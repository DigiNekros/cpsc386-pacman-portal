# Anne Edwards, Miguel Mancera, Parker Nguyen
# CPSC 386-03

import pygame as pg
from pathlib import Path

@staticmethod
def read_file(list=[], file=''):
    f = Path(file)
    contents = f.read_text()
    
    i = 0
    # break up into rows
    while i < len(contents):
        string = ''
        char = contents[i]
        while char != '\n' and i < len(contents):
            string += char
            i += 1
            if i < len(contents):
                char = contents[i]
        
        if string != '':
            list.append(string)
        i += 1