import pygame as pg
from pygame.locals import *

from Const import *
from Board import *
from ScoreManager import *

class Core(object):
    def __init__(self):
        pg.mixer.pre_init(44100, -16, 2, 1024)
        pg.init()

        pg.display.set_caption('AI Connect 4')
        pg.display.set_mode((WINDOW_W, WINDOW_H))

        self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))
        self.bg = pg.Surface((WINDOW_W, WINDOW_H))
        self.clock = pg.time.Clock()

        self.bg.fill((255, 255, 255))

        self.run = True
        self.current_player = PLAYER

        self.init_objects()

    def init_objects(self):
        self.board = Board((WINDOW_W//2, WINDOW_H//2))
        self.scoreM = ScoreManager(2)

    def start(self):
        while self.run:
            self.input()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def switch_player(self):
        self.current_player = -self.current_player - 1
    
    def input(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False

            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.run = False

            elif e.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                print(f"Current mouse position : {pos}.")
                # call Token
                (index, col), onboard = self.board.on_board(pos)
                if onboard:
                    print(f"The token is on the board at index {index} and column {col}")
                    pos = self.board.get_cell_pos_from_mouse(pos, col)
                    if abs(self.current_player) == PLAYER:
                        token = Token(BLUE, pos[0], pos[1])
                    else:
                        token = Token(RED, pos[0], pos[1])
                    #token.place_token(self)

                    self.board.add_token(token)

                    #places the token in the pygame window board
                    x, y = token.place_token(self)
                    print(f"current token x({x}), y({y})")

                    row = self.decode_row(y)
                    print(f"matrix row, col : {row},{index}")

                    #place the token in the python board matrix
                    self.board.place_token(row, index, token.color)

                    #check if the token has created a connect 4
                    if not self.board.check_connect_4(token.color):
                        self.switch_player()
                        print("Current player:", self.decode_player(self.current_player), x, y)
                        for i in range(ROWS):
                            print(self.board.board[i])
                    else:
                        print(f"{self.decode_player(self.current_player)} wins!")

    def decode_player(self, player):
        if abs(player) == 4:
            return "Player"
        else:
            return "Computer"

    def decode_row(self, y):
        row = -1
        if y == 187:
            row = 0
        elif y == 257:
            row = 1
        elif y == 327:
            row = 2
        elif y == 397:
            row = 3
        elif y == 467:
            row = 4
        else:
            row = 5
        return row

    def reset():
        pass

    def update(self):
        pass

    def render(self):
        self.screen.blit(self.bg, (0, 0))

        self.board.render(self)

        pg.display.update()