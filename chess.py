import pygame
import sys
from board import Pieces, Chessboard, index_to_coordinates, coordinates_to_index
from rules import get_legal_moves, get_raw_moves, in_check

pygame.init()
pygame.display.set_caption("Chess")

screenx = 640
screeny = 640
screen = pygame.display.set_mode((screenx, screeny))
BGCOLOR = (250, 250, 250)

clock = pygame.time.Clock()

pieces = Pieces()
pieces.load_pieces()
chessgame = Chessboard(screen, pieces)
chessgame.load_position()

dragging = False
old_piece_index = None

while True:
    screen.fill(BGCOLOR)
    chessgame.draw_board()
    chessgame.draw_pieces(old_piece_index)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if dragging == False:
                mousex, mousey = pygame.mouse.get_pos()
                old_square_index = coordinates_to_index(mousex//80, mousey//80)
                if chessgame.board[old_square_index]:
                    if chessgame.board[old_square_index][0] == chessgame.color_to_move:
                        if chessgame.incheck_squares:
                            legal_moves = get_legal_moves(chessgame.board, old_square_index, '', chessgame.en_passant)
                        else:
                            legal_moves = get_legal_moves(chessgame.board, old_square_index, chessgame.castle_available, chessgame.en_passant)
                        chessgame.dotted_squares = legal_moves
                        dragging_piece = chessgame.board[old_square_index]
                        old_piece_index = old_square_index
                        dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            chessgame.dotted_squares = []
            if dragging == True:
                mousex, mousey = pygame.mouse.get_pos()
                new_square_index = coordinates_to_index(mousex//80, mousey//80)

                if new_square_index in legal_moves:
    
                    chessgame.move_piece(old_square_index, new_square_index)
                    dragging = False
                    chessgame.switch_turns()

                else:
                    chessgame.board[old_square_index] = dragging_piece
                    dragging = False
            old_piece_index = None
    
    chessgame.incheck_squares = []

    if in_check(chessgame.board, chessgame.color_to_move, chessgame.castle_available, chessgame.en_passant):

        for square_index in range(len(chessgame.board)):
            if chessgame.board[square_index] == chessgame.color_to_move + 'K':
                chessgame.incheck_squares.append(square_index)



    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        if dragging == True:
            mousex, mousey = pygame.mouse.get_pos()
            screen.blit(pieces.types[dragging_piece], (mousex-40, mousey-40))


    pygame.display.update()
    msElapsed = clock.tick(30)