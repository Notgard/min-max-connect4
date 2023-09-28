import pygame as pg
import numpy as np

from Const import *

class Token(object):
    def __init__(self, color: int, x: int, y: int):
        self.x = x
        self.y = y

        assert color in [RED, BLUE]
        self.color = color

        if self.color == BLUE:
            self.image = pg.image.load('img/player1.png')
        else:
            self.image = pg.image.load('img/player2.png')

        # 0 W
        # 1 H
        self.size = (self.image.get_width(), self.image.get_height())

        self.rect = pg.Rect(x - (self.size[0]//2), y - (self.size[1]//2), self.size[0], self.size[1]+14)

        self.speed_y = 0

    def __eq__(self, other):
        return (self.x == other.x)and (self.y == other.y)

    def place_token(self, core):
        falling = True
        offset = 5 # space between tokens in image board
        while falling:
            if (self.y + (self.size[1]//2)) + offset >= core.board.end_pos[1]:
                print("reached bottom", self.y, self.size[1], core.board.end_pos)
                falling = False
                break
            else:
                for token in core.board.tokens:
                    if token != self and token.rect.colliderect(self.rect):
                        print("collision between tokens")
                        print(token.rect, self.rect)
                        falling = False
                        break
            #erase current image
            core.screen.fill((0, 0, 0, 0))
            core.render()
            # update position
            self.y += 1
            self.rect.centery = self.y
            #move token rect hitbox
            self.render(core)
            pg.display.update()
        return (self.x, self.y)

    def render(self, core):
        #pg.draw.rect(core.screen, (0, 100, 255), self.rect, 3) #show token hitbox outline for debugging
        core.screen.blit(self.image.convert_alpha(), (self.x - (self.size[0]//2), self.y - (self.size[1]//2)))

