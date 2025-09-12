from helper import draw_board, check_turn, check_win
import os

spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    if prev_turn == turn:
        print("Invalid spot selected. Pick another.")
    prev_turn = turn

    print("Player " + str(turn % 2 + 1) + "'s turn: Pick your spot or press q to quit.")
    # get player choice
    choice = input()
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots: 
        if not spots[int(choice)] in {'X', 'O'}: 
            turn += 1
            spots[int(choice)] = check_turn(turn)
    if check_win(spots): playing, complete = False, True
    if turn > 8: playing = False

# print result
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

# if there is a winner, 
if complete: 
    if check_turn(turn) == 'X': print("Player 1 wins!")
    else: print("Player 2 wins!")
else: 
    # if there is a tie, no winner
    print("No winner.")

