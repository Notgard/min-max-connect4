import pygame as pg

from Const import *
from Token import *

class Board(object):
    #position board middle of the screen
    def __init__(self, pos: tuple):
        # 0 = empty space
        # 1 = red token
        # 2 = blue token 
        self.board = [[0 for _ in range(7)] for _ in range(6)] # for checking game winning condition
        self.tokens = [] #list of token objects

        self.image = pg.image.load('img/board.png')
        
        self.size = (self.image.get_width(), self.image.get_height())
        # position needed for the board to be in the middle
        self.pos = (pos[0] - (self.size[0]//2), pos[1] - (self.size[1]//2))

        #self.start_pos = (pos[0] - WINDOW_W//2, pos[1] - WINDOW_H//2)
        self.end_pos = (pos[0] + (self.size[0]//2), pos[1] + (self.size[1]//2))

        #detect placed token by having invisible rectangles for each column
        self.rect = pg.Rect(self.pos, self.size)

        column_size = (self.size[0]//7, self.size[1] + 150)
        column_pos = [self.pos[0], self.pos[1] - 150]
        self.columns = []
        for _ in range(0, 7):
            self.columns.append(pg.Rect(tuple(column_pos), column_size))
            column_pos[0] += column_size[0]


    #make sure the token is on the board or above it (i.e in any column)
    def on_board(self, pos: tuple):
        for index, col in enumerate(self.columns):
            if col.collidepoint(pos):
                return (index, col), True
        return (-1, -1), False

    #places token in list and in board state matrix (tensor)
    def add_token(self, token: Token):
        self.tokens.append(token)

    def place_token(self, row, col, color):
        self.board[row][col] = color

    def get_cell_pos_from_mouse(self, pos: tuple, column: pg.Rect):
        x = column.centerx
        y = pos[1]
        return (x, y)

    # returns the winning color (i.e 1 or 2), else -1
    # can be optimized by checking players last move as chronological list
    def check_connect_4(self, last_move: int) -> int:
        # check row connect 4
        for i in range(ROWS):
            connect = 0
            start = 0
            for j in range(COLS):
                if self.board[i][j] == last_move:
                    start = j
                    break
            while start < len(self.board[0]) and self.board[i][start] == last_move:
                connect += 1
                start += 1
            if connect == 4:
                return True

        matrix = np.array(self.board)

        # check column connect 4
        for i in range(COLS):
            connect = 0
            start = 0
            for j in range(ROWS):
                if matrix[:,i][j] == last_move:
                    start = j
                    break
            while start < ROWS and matrix[:,i][start] == last_move:
                connect += 1
                start += 1
            if connect == 4:
                return True

        diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1]) if len(matrix[::-1,:].diagonal(i)) == 4]
        diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1) if len(matrix.diagonal(i)) == 4)
        for diag in diags:
            if diag.tolist().count(diag[0]) == len(diag) and diag[0] != 0:
                return True
        return False

    def render(self, core):
        core.screen.blit(self.image.convert_alpha(), self.pos)
        for col in self.columns:
            pg.draw.rect(core.screen, (0, 100, 255), col, 3)
        for token in self.tokens:
            token.render(core)
