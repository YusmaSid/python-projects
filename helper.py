def draw_board(spots):
    board = (f'|{spots[1]}|{spots[2]}|{spots[3]}| \
             \n|{spots[4]}|{spots[5]}|{spots[6]}| \
             \n|{spots[7]}|{spots[8]}|{spots[9]}|')
    print(board)

def check_turn(turn):
    if turn % 2 == 0: return 'O'
    elif turn % 2 == 1: return 'X'

def check_win(spots):
    # horizontal
    if (spots[1] == spots[2] == spots[3] \
        or spots[4] == spots[5] == spots[6] \
        or spots [7] == spots[8] == spots[9]):
        return True
    # vertical
    elif (spots[1] == spots[4] == spots[7] \
        or spots[2] == spots[5] == spots[8] \
        or spots[3] == spots[6] == spots[9]):
        return True
    # diagonal
    elif (spots[1] == spots[5] == spots[9] \
        or spots[3] == spots[5] == spots[7]):
        return True
    else: return False