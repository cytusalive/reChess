
def get_raw_moves(board_state, piece_index, castle='', en_passant=None):
    raw_moves = []
    current_position = board_state.copy()
    piece_color = current_position[piece_index][0]
    piece_type = current_position[piece_index][1]
    # ROOK MOVES
    if piece_type == 'R':
        row = piece_index // 8
        for squares_LEFT in range(1, 8):
            squares_LEFT = -squares_LEFT
            if piece_index + squares_LEFT >= row*8:
                if current_position[piece_index + squares_LEFT] == '':
                    raw_moves.append(piece_index + squares_LEFT)
                    continue
                elif current_position[piece_index + squares_LEFT][0] != piece_color:
                    raw_moves.append(piece_index + squares_LEFT)
                    break
                elif current_position[piece_index + squares_LEFT][0] == piece_color:
                    break
        for squares_RIGHT in range(1, 8):
            if piece_index + squares_RIGHT < (row+1)*8:
                if current_position[piece_index + squares_RIGHT] == '':
                    raw_moves.append(piece_index + squares_RIGHT)
                    continue
                elif current_position[piece_index + squares_RIGHT][0] != piece_color:
                    raw_moves.append(piece_index + squares_RIGHT)
                    break
                elif current_position[piece_index + squares_RIGHT][0] == piece_color:
                    break
        for squares_UP in range(1, 8):
            squares_UP = -squares_UP*8
            if piece_index + squares_UP >= 0:
                if current_position[piece_index + squares_UP] == '':
                    raw_moves.append(piece_index + squares_UP)
                    continue
                elif current_position[piece_index + squares_UP][0] != piece_color:
                    raw_moves.append(piece_index + squares_UP)
                    break
                elif current_position[piece_index + squares_UP][0] == piece_color:
                    break
        for squares_DOWN in range(1, 8):
            squares_DOWN = squares_DOWN*8
            if piece_index + squares_DOWN <= 63:
                if current_position[piece_index + squares_DOWN] == '':
                    raw_moves.append(piece_index + squares_DOWN)
                    continue
                elif current_position[piece_index + squares_DOWN][0] != piece_color:
                    raw_moves.append(piece_index + squares_DOWN)
                    break
                elif current_position[piece_index + squares_DOWN][0] == piece_color:
                    break
    # BISHOP MOVES
    if piece_type == 'B':
        for squares_UPLEFT in range(1, 8):
            squares_UPLEFT = -squares_UPLEFT*8 - squares_UPLEFT
            new_index = piece_index + squares_UPLEFT
            if new_index % 8 == 7:
                break
            if new_index >= 0:
                if current_position[new_index] == '':
                    if new_index % 8 == 0:
                        raw_moves.append(new_index)
                        break
                    else:
                        raw_moves.append(new_index)
                        continue
                elif current_position[new_index][0] != piece_color:
                    raw_moves.append(new_index)
                    break
                elif current_position[new_index][0] == piece_color:
                    break
        for squares_UPRIGHT in range(1, 8):
            squares_UPRIGHT = -squares_UPRIGHT*8 + squares_UPRIGHT
            new_index = piece_index + squares_UPRIGHT
            if new_index % 8 == 0:
                break
            if new_index >= 0:
                if current_position[new_index] == '':
                    if new_index % 8 == 7:
                        raw_moves.append(new_index)
                        break
                    else:
                        raw_moves.append(new_index)
                        continue
                elif current_position[new_index][0] != piece_color:
                    raw_moves.append(new_index)
                    break
                elif current_position[new_index][0] == piece_color:
                    break
        for squares_DOWNLEFT in range(1, 8):
            squares_DOWNLEFT = squares_DOWNLEFT*8 - squares_DOWNLEFT
            new_index = piece_index + squares_DOWNLEFT
            if new_index % 8 == 7:
                break
            if new_index < 64:
                if current_position[new_index] == '':
                    if new_index % 8 == 0:
                        raw_moves.append(new_index)
                        break
                    else:
                        raw_moves.append(new_index)
                        continue
                elif current_position[new_index][0] != piece_color:
                    raw_moves.append(new_index)
                    break
                elif current_position[new_index][0] == piece_color:
                    break
        for squares_DOWNRIGHT in range(1, 8):
            squares_DOWNRIGHT = squares_DOWNRIGHT*8 + squares_DOWNRIGHT
            new_index = piece_index + squares_DOWNRIGHT
            if new_index % 8 == 0:
                break
            if new_index < 64:
                if current_position[new_index] == '':
                    if new_index % 8 == 7:
                        raw_moves.append(new_index)
                        break
                    else:
                        raw_moves.append(new_index)
                        continue
                elif current_position[new_index][0] != piece_color:
                    raw_moves.append(new_index)
                    break
                elif current_position[new_index][0] == piece_color:
                    break
    # QUEEN MOVES, by copypasting rook and bishop moves
    if piece_type == 'Q':
        row = piece_index // 8
        for squares_LEFT in range(1, 8):
            squares_LEFT = -squares_LEFT
            if piece_index + squares_LEFT >= row*8:
                if current_position[piece_index + squares_LEFT] == '':
                    raw_moves.append(piece_index + squares_LEFT)
                    continue
                elif current_position[piece_index + squares_LEFT][0] != piece_color:
                    raw_moves.append(piece_index + squares_LEFT)
                    break
                elif current_position[piece_index + squares_LEFT][0] == piece_color:
                    break
        for squares_RIGHT in range(1, 8):
            if piece_index + squares_RIGHT < (row+1)*8:
                if current_position[piece_index + squares_RIGHT] == '':
                    raw_moves.append(piece_index + squares_RIGHT)
                    continue
                elif current_position[piece_index + squares_RIGHT][0] != piece_color:
                    raw_moves.append(piece_index + squares_RIGHT)
                    break
                elif current_position[piece_index + squares_RIGHT][0] == piece_color:
                    break
        for squares_UP in range(1, 8):
            squares_UP = -squares_UP*8
            if piece_index + squares_UP >= 0:
                if current_position[piece_index + squares_UP] == '':
                    raw_moves.append(piece_index + squares_UP)
                    continue
                elif current_position[piece_index + squares_UP][0] != piece_color:
                    raw_moves.append(piece_index + squares_UP)
                    break
                elif current_position[piece_index + squares_UP][0] == piece_color:
                    break
        for squares_DOWN in range(1, 8):
            squares_DOWN = squares_DOWN*8
            if piece_index + squares_DOWN <= 63:
                if current_position[piece_index + squares_DOWN] == '':
                    raw_moves.append(piece_index + squares_DOWN)
                    continue
                elif current_position[piece_index + squares_DOWN][0] != piece_color:
                    raw_moves.append(piece_index + squares_DOWN)
                    break
                elif current_position[piece_index + squares_DOWN][0] == piece_color:
                    break
    
        for squares_UPLEFT in range(1, 8):
            squares_UPLEFT = -squares_UPLEFT*8 - squares_UPLEFT
            new_index = piece_index + squares_UPLEFT
            if new_index % 8 == 7:
                break
            if new_index >= 0:
                if current_position[new_index] == '':
                    if new_index % 8 == 0:
                        raw_moves.append(new_index)
                        break
                    else:
                        raw_moves.append(new_index)
                        continue
                elif current_position[new_index][0] != piece_color:
                    raw_moves.append(new_index)
                    break
                elif current_position[new_index][0] == piece_color:
                    break
        for squares_UPRIGHT in range(1, 8):
            squares_UPRIGHT = -squares_UPRIGHT*8 + squares_UPRIGHT
            new_index = piece_index + squares_UPRIGHT
            if new_index % 8 == 0:
                break
            if new_index >= 0:
                if current_position[new_index] == '':
                    if new_index % 8 == 7:
                        raw_moves.append(new_index)
                        break
                    else:
                        raw_moves.append(new_index)
                        continue
                elif current_position[new_index][0] != piece_color:
                    raw_moves.append(new_index)
                    break
                elif current_position[new_index][0] == piece_color:
                    break
        for squares_DOWNLEFT in range(1, 8):
            squares_DOWNLEFT = squares_DOWNLEFT*8 - squares_DOWNLEFT
            new_index = piece_index + squares_DOWNLEFT
            if new_index % 8 == 7:
                break
            if new_index < 64:
                if current_position[new_index] == '':
                    if new_index % 8 == 0:
                        raw_moves.append(new_index)
                        break
                    else:
                        raw_moves.append(new_index)
                        continue
                elif current_position[new_index][0] != piece_color:
                    raw_moves.append(new_index)
                    break
                elif current_position[new_index][0] == piece_color:
                    break
        for squares_DOWNRIGHT in range(1, 8):
            squares_DOWNRIGHT = squares_DOWNRIGHT*8 + squares_DOWNRIGHT
            new_index = piece_index + squares_DOWNRIGHT
            if new_index % 8 == 0:
                break
            if new_index < 64:
                if current_position[new_index] == '':
                    if new_index % 8 == 7:
                        raw_moves.append(new_index)
                        break
                    else:
                        raw_moves.append(new_index)
                        continue
                elif current_position[new_index][0] != piece_color:
                    raw_moves.append(new_index)
                    break
                elif current_position[new_index][0] == piece_color:
                    break
    # KING MOVES
    if piece_type == 'K':
        try_moves = []
        if piece_index % 8 == 7:
            for direction in [-9, -8, -1, 7, 8]:
                try_moves.append(piece_index + direction)
        elif piece_index % 8 == 0:
            for direction in [-8, -7, 1, 8, 9]:
                try_moves.append(piece_index + direction)
        else:
            for direction in [-9, -8, -7, -1, 1, 7, 8, 9]:
                try_moves.append(piece_index + direction)
        for move_index in try_moves:
            if move_index < 64 and move_index >= 0:
                if current_position[move_index] == '':
                    raw_moves.append(move_index)
                elif current_position[move_index][0] == piece_color:
                    continue
                elif current_position[move_index][0] != piece_color:
                    raw_moves.append(move_index)
        if piece_color == 'w':
            if 'K' in castle:
                if current_position[61] == '' and current_position[62] == '':
                    raw_moves.append(62)
            if 'Q' in castle:
                if current_position[59] == '' and current_position[58] == '' and current_position[57] == '':
                    raw_moves.append(58)
        if piece_color == 'b':
            if 'k' in castle:
                if current_position[5] == '' and current_position[6] == '':
                    raw_moves.append(6)
            if 'q' in castle:
                if current_position[3] == '' and current_position[2] == '' and current_position[1] == '':
                    raw_moves.append(2) 

    # PAWN MOVES
    if piece_type == 'P':
        if piece_color == 'w':
            if piece_index - 8 >= 0:
                if current_position[piece_index - 8] == '':
                    raw_moves.append(piece_index - 8)
                    if piece_index >= 6*8 and piece_index < 7*8:
                        if current_position[piece_index - 16] == '':
                            raw_moves.append(piece_index - 16)
                if piece_index % 8 != 7:
                    if current_position[piece_index - 7]:
                        if current_position[piece_index - 7][0] == 'b':
                            raw_moves.append(piece_index - 7)
                    elif piece_index - 7 == en_passant:
                        raw_moves.append(piece_index - 7)
                if piece_index % 8 != 0:
                    if current_position[piece_index - 9]:
                        if current_position[piece_index - 9][0] == 'b':
                            raw_moves.append(piece_index - 9)
                    elif piece_index - 9 == en_passant:
                        raw_moves.append(piece_index - 9)
        if piece_color == 'b':
            if piece_index + 8 < 64:
                if current_position[piece_index + 8] == '':
                    raw_moves.append(piece_index + 8)
                    if piece_index >= 1*8 and piece_index < 2*8:
                        if current_position[piece_index + 16] == '':
                            raw_moves.append(piece_index + 16)
                if piece_index % 8 != 0:
                    if current_position[piece_index + 7]:
                        if current_position[piece_index + 7][0] == 'w':
                            raw_moves.append(piece_index + 7)
                    elif piece_index + 7 == en_passant:
                        raw_moves.append(piece_index + 7)
                if piece_index % 8 != 7:
                    if current_position[piece_index + 9]:
                        if current_position[piece_index + 9][0] == 'w':
                            raw_moves.append(piece_index + 9)
                    elif piece_index + 9 == en_passant:
                        raw_moves.append(en_passant)
    # KNIGHT MOVES
    if piece_type == 'N':
        moves = [-17, -15, -10, -6, 6, 10, 15, 17]
        for move in moves:
            new_index = piece_index + move
            if new_index >= 0 and new_index < 64 and abs(new_index % 8 - piece_index % 8) < 3:
                if current_position[new_index] == '':
                    raw_moves.append(new_index)
                elif current_position[new_index][0] != piece_color:
                    raw_moves.append(new_index)
                elif current_position[new_index][0] == piece_color:
                    continue 
    return raw_moves

def get_legal_moves(board_state, piece_index, castle='', en_passant=None):
    raw_moves = get_raw_moves(board_state, piece_index, castle, en_passant)
    legal_moves = []
    for move in raw_moves:
        test_position = board_state.copy()
        test_position[move] = test_position[piece_index]
        test_position[piece_index] = ''
        if not in_check(test_position, board_state[piece_index][0], '', en_passant):
            legal_moves.append(move)

    return legal_moves

def in_check(position, turn_to_move, castle='', en_passant=None):
    for square_index in range(len(position)):
        if position[square_index]:
            if position[square_index][0] != turn_to_move:
                moves = get_raw_moves(position, square_index, castle, en_passant)
           
                for move in moves:
                    if position[move] == turn_to_move + 'K':

                        return True
    return False
