PIECE_VALUE = {'K': 100000, 'Q': 900, 'R': 500, 'B': 330, 'N': 320, 'P': 100}

def evaluate_piece(position):
    white_pieces = []
    black_pieces = []
    for square in position:
        if square:
            if square[0] == 'w':
                white_pieces.append(square[1])
            if square[0] == 'b':
                black_pieces.append(square[1])
    white_piece_value = 0
    black_piece_value = 0

    for piece in white_pieces:
        white_piece_value += PIECE_VALUE[piece]
    for piece in black_pieces:
        black_piece_value += PIECE_VALUE[piece]
    return (white_piece_value - black_piece_value) * 0.01

WHITE_POSITION_VALUE = {'K':   [-30,-40,-40,-50,-50,-40,-40,-30,
                                -30,-40,-40,-50,-50,-40,-40,-30,
                                -30,-40,-40,-50,-50,-40,-40,-30,
                                -30,-40,-40,-50,-50,-40,-40,-30,
                                -20,-30,-30,-40,-40,-30,-30,-20,
                                -10,-20,-20,-20,-20,-20,-20,-10,
                                20, 20,  0,  0,  0,  0, 20, 20,
                                20, 30, 10,  0,  0, 10, 30, 20],
                        'Q':   [-20,-10,-10, -5, -5,-10,-10,-20,
                                -10,  0,  0,  0,  0,  0,  0,-10,
                                -10,  0,  5,  5,  5,  5,  0,-10,
                                -5,  0,  5,  5,  5,  5,  0, -5,
                                0,  0,  5,  5,  5,  5,  0, -5,
                                -10,  5,  5,  5,  5,  5,  0,-10,
                                -10,  0,  5,  0,  0,  0,  0,-10,
                                -20,-10,-10, -5, -5,-10,-10,-20],
                        'R':   [0,  0,  0,  0,  0,  0,  0,  0,
                                5, 10, 10, 10, 10, 10, 10,  5,
                                -5,  0,  0,  0,  0,  0,  0, -5,
                                -5,  0,  0,  0,  0,  0,  0, -5,
                                -5,  0,  0,  0,  0,  0,  0, -5,
                                -5,  0,  0,  0,  0,  0,  0, -5,
                                -5,  0,  0,  0,  0,  0,  0, -5,
                                0,  0,  0,  5,  5,  0,  0,  0],
                        'B':   [-20,-10,-10,-10,-10,-10,-10,-20,
                                -10,  0,  0,  0,  0,  0,  0,-10,
                                -10,  0,  5, 10, 10,  5,  0,-10,
                                -10,  5,  5, 10, 10,  5,  5,-10,
                                -10,  0, 10, 10, 10, 10,  0,-10,
                                -10, 10, 10, 10, 10, 10, 10,-10,
                                -10,  5,  0,  0,  0,  0,  5,-10,
                                -20,-10,-10,-10,-10,-10,-10,-20],
                        'N':   [-50,-40,-30,-30,-30,-30,-40,-50,
                                -40,-20,  0,  0,  0,  0,-20,-40,
                                -30,  0, 10, 15, 15, 10,  0,-30,
                                -30,  5, 15, 20, 20, 15,  5,-30,
                                -30,  0, 15, 20, 20, 15,  0,-30,
                                -30,  5, 10, 15, 15, 10,  5,-30,
                                -40,-20,  0,  5,  5,  0,-20,-40,
                                -50,-40,-30,-30,-30,-30,-40,-50],
                        'P':   [0,  0,  0,  0,  0,  0,  0,  0,
                                50, 50, 50, 50, 50, 50, 50, 50,
                                10, 10, 20, 30, 30, 20, 10, 10,
                                5,  5, 10, 25, 25, 10,  5,  5,
                                0,  0,  0, 20, 20,  0,  0,  0,
                                5, -5,-10,  0,  0,-10, -5,  5,
                                5, 10, 10,-20,-20, 10, 10,  5,
                                0,  0,  0,  0,  0,  0,  0,  0],
                        }

BLACK_POSITION_VALUE = {}
for piece in WHITE_POSITION_VALUE:
    BLACK_POSITION_VALUE[piece] = WHITE_POSITION_VALUE[piece].copy()
for piece in BLACK_POSITION_VALUE:
    BLACK_POSITION_VALUE[piece].reverse()

def evaluate_position(position):
    white_piece_value = 0
    black_piece_value = 0
    for square_index in range(len(position)):
        if position[square_index]:
            piece_color = position[square_index][0]
            piece_type = position[square_index][1]
            if piece_color == 'w':
                white_piece_value += WHITE_POSITION_VALUE[piece_type][square_index]
            if piece_color == 'b':
                black_piece_value += BLACK_POSITION_VALUE[piece_type][square_index]
    return (white_piece_value - black_piece_value) * 0.01
    

def evaluate(position):
    return evaluate_piece(position) + evaluate_position(position) 

#print(evaluate_position(['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']))


