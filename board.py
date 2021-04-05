import pygame
from rules import in_check, get_legal_moves
DARK_SQUARE = (120, 60, 40)
LIGHT_SQUARE = (200, 180, 120)
HIGHLIGHT_SQUARE = (240, 240, 120, 180)
CHECK_HIGHLIGHT = (250, 100, 100, 100)
MOVE_INDICATOR = (100, 200, 150, 100)

pygame.font.init()
font = pygame.font.SysFont("Arial", 20, True)

class Pieces:
    def __init__(self):
        self.types = {}
    
    def load_pieces(self):
        piece_types = ['R', 'N', 'B', 'Q', 'K', 'P']
        for ptype in piece_types:
            self.types['w'+ptype] = pygame.image.load('piece_sprites/w'+ptype+'.png')
            self.types['b'+ptype] = pygame.image.load('piece_sprites/b'+ptype+'.png')

class Chessboard:
    def __init__(self, area, pieces):
        self.area = area
        self.board = ['' for i in range(64)]
        self.pieces = pieces
        self.screen_x, self.screen_y = pygame.Surface.get_size(area)
        self.square = pygame.Surface((self.screen_x/8, self.screen_y/8))
        self.color_to_move = ''
        self.highlight_squares = []
        self.dotted_squares = []
        self.en_passant = None
        self.castle_available = ''
        self.incheck_squares = []

    def load_position(self, position='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq'): #'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        board_index = 0
        for fen_index in range(len(position)):
            if position[fen_index].isnumeric():
                for l in range(int(position[fen_index])):
                    self.board[board_index] = ''
                    board_index += 1
            elif position[fen_index] == '/':
                continue
            elif position[fen_index] == ' ':
                self.color_to_move = position[fen_index+1]
                self.castle_available = position[fen_index+3:]
                break
            else:
                if position[fen_index].islower():
                    self.board[board_index] = 'b' + position[fen_index].upper()
                    board_index += 1
                else:
                    self.board[board_index] = 'w' + position[fen_index]
                    board_index += 1
            
              
    def draw_board(self):
        for y in range(8):
            for x in range(8):
                if y % 2:
                    if x % 2:
                        self.square.fill(LIGHT_SQUARE)
                    else:
                        self.square.fill(DARK_SQUARE)
                else:
                    if x % 2:
                        self.square.fill(DARK_SQUARE)
                    else:
                        self.square.fill(LIGHT_SQUARE)

                # showing square index, remove after development
                index = font.render(str(y*8 + x), True, (0, 0, 0))
                self.square.blit(index, (0, 0))

                self.area.blit(self.square, (self.screen_x/8 * x, self.screen_y/8 * y))

                if 8*y+x in self.highlight_squares:
                    transparent_square = pygame.Surface((80,80)).convert_alpha()
                    transparent_square.fill(HIGHLIGHT_SQUARE)
                    self.area.blit(transparent_square, (self.screen_x/8 * x, self.screen_y/8 * y))
                if 8*y+x in self.dotted_squares:
                    transparent_square = pygame.Surface((80,80)).convert_alpha()
                    transparent_square.fill(MOVE_INDICATOR)
                    self.area.blit(transparent_square, (self.screen_x/8 * x, self.screen_y/8 * y))
                if 8*y+x in self.incheck_squares:
                    transparent_square = pygame.Surface((80,80)).convert_alpha()
                    transparent_square.fill(CHECK_HIGHLIGHT)
                    self.area.blit(transparent_square, (self.screen_x/8 * x, self.screen_y/8 * y))
                
        if self.color_to_move == 'w':
            pygame.display.set_caption("Chess - White to Move")
        elif self.color_to_move == 'b':
            pygame.display.set_caption("Chess - Black to Move")

    def draw_pieces(self, dragging_index=None):
        for square_index in range(len(self.board)):
            if self.board[square_index]:
                if square_index == dragging_index:
                    continue
                else:
                    x, y = index_to_coordinates(square_index)
                    self.area.blit(self.pieces.types[self.board[square_index]], (x*self.screen_x/8, y*self.screen_y/8))

    def switch_turns(self):
        
        if self.color_to_move == 'w':
            self.color_to_move = 'b'
        elif self.color_to_move == 'b':
            self.color_to_move = 'w'

        # find checks
        self.incheck_squares = []
        can_move = True
        if in_check(self.board, self.color_to_move, self.castle_available, self.en_passant):
            can_move = False
            for square_index in range(len(self.board)):
                if self.board[square_index] == self.color_to_move + 'K':
                    self.incheck_squares.append(square_index)
        # find checkmates
                if self.board[square_index]:
                    if self.board[square_index][0] == self.color_to_move:
                        moves = get_legal_moves(self.board, square_index, '', self.en_passant)
                        print(moves)
                        if moves:
                            can_move = True
        if can_move == False:
            self.color_to_move = None
            pygame.display.set_caption("Checkmate - Game over")

    def move_piece(self, old_piece_index, new_piece_index):
        self.highlight_squares = [old_piece_index, new_piece_index]
        piece = self.board[old_piece_index]
        self.board[new_piece_index] = piece
        self.board[old_piece_index] = ''
        # PAWN PROMOTION
        for piece_index in range(8):
            if self.board[piece_index] == 'wP':
                self.board[piece_index] = 'wQ'
            if self.board[63 - piece_index] == 'bP':
                self.board[63 - piece_index] = 'bQ'
        # PAWN EN PASSANT
        if piece == 'wP' and new_piece_index == self.en_passant:
            self.board[new_piece_index + 8] = ''
        if piece == 'bP' and new_piece_index == self.en_passant:
            self.board[new_piece_index - 8] = ''
        self.en_passant = None
        if piece == 'bP' and new_piece_index - old_piece_index == 16:
            self.en_passant = new_piece_index - 8
        if piece == 'wP' and new_piece_index - old_piece_index == -16:
            self.en_passant = new_piece_index + 8
        # KING CASTLE
        if piece[1] == 'K' and new_piece_index - old_piece_index == 2:
            self.board[new_piece_index-1] = piece[0] + 'R'
            self.board[new_piece_index+1] = ''
        if piece[1] == 'K' and new_piece_index - old_piece_index == -2:
            self.board[new_piece_index+1] = piece[0] + 'R'
            self.board[new_piece_index-2] = ''
        if piece == 'wK':
            self.castle_available = self.castle_available.replace('K', '')
            self.castle_available = self.castle_available.replace('Q', '')
        if piece == 'bK':
            self.castle_available = self.castle_available.replace('k', '')
            self.castle_available = self.castle_available.replace('q', '')
        if piece[1] == 'R':
            if old_piece_index == 0:
                self.castle_available = self.castle_available.replace('q', '')
            if old_piece_index == 7:
                self.castle_available = self.castle_available.replace('k', '')
            if old_piece_index == 56:
                self.castle_available = self.castle_available.replace('Q', '')
            if old_piece_index == 63:
                self.castle_available = self.castle_available.replace('K', '')
        else:
            if new_piece_index == 0:
                self.castle_available = self.castle_available.replace('q', '')
            if new_piece_index == 7:
                self.castle_available = self.castle_available.replace('k', '')
            if new_piece_index == 56:
                self.castle_available = self.castle_available.replace('Q', '')
            if new_piece_index == 63:
                self.castle_available = self.castle_available.replace('K', '')
                


def index_to_coordinates(index):
    y = index // 8 
    x = index % 8 
    return (x, y)

def coordinates_to_index(x, y):
    index = y * 8 + x
    return index
