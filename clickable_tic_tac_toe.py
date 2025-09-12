# Make your Tic-Tac-Toe game clickable. Building off the beginner project, 
# now make a version of Tic-Tac-Toe that has an actual UI  you’ll use by clicking on open squares. 
# Challenge: can you write a simple “AI” opponent for a human player to play against?
import tkinter as tk
from helper import draw_board, check_turn, check_win

def empty_spots(spots):
    return [i for i, v in spots.items() if v not in ('X', 'O')]

# computer moves
def find_computer_win(spots, computer_symbol, player_symbol):
    # win move
    for spot in empty_spots(spots):
        temp_board = spots.copy()
        temp_board[spot] = computer_symbol
        
        if check_win(temp_board):
            return spot

    # block move
    for spot in empty_spots(spots):
        temp_board = spots.copy()
        temp_board[spot] = player_symbol
        
        if check_win(temp_board):
            return spot
        
    return None

def get_computer_move():
    computer_symbol = 'O'
    player_symbol = 'X'

    # block or win
    move = find_computer_win(spots, computer_symbol, player_symbol)
    if move is not None:
        return move
    
    # center piece
    if spots[5] not in ('X', 'O'):
        return 5
    
    # corners
    for corner in [1, 3, 7, 9]:
        if spots[corner] not in ('X', 'O'):
            return corner

    # sides 
    for side in [2, 4, 6, 8]:
        if spots[side] not in ('X', 'O'):
            return side
        
    return None

root = tk.Tk()
root.title("Tic-Tac-Toe")

spots = {i: str(i) for i in range(1, 10)}
buttons = {}
turn = 0
complete = False

label = tk.Label(root, text="Player X's turn", font=('Helvetica', 12))
label.grid(row=3, column=0, columnspan=3,)

def disable_all():
    for btn in buttons.values():
        btn.config(state="disabled")

def handle_click(pos):
    global turn, complete
    if complete:
        return
    if spots[pos] not in {'X', 'O'}:
        turn += 1
        spots[pos] = check_turn(turn)
        buttons[pos].config(text=spots[pos], state='disabled')
    
        if check_win(spots):
            # label.config(text=f"Player {1 if check_turn(turn) == 'X' else 2} wins!")
            # complete = True
            # disable_all()
            show_win(1 if check_turn(turn) == 'X' else 2)
            complete = True
        elif turn > 8:
            show_win(0)
            # label.config(text="No Winner")
            complete = True
        else:
            label.config(text=f"Player {spots[pos]}'s turn")

            # computer choice
            if spots[pos] == 'X' and not complete:
                computer_move = get_computer_move()
                if computer_move is not None:
                    root.after(500, handle_click(computer_move))
# win screen
def show_win(winner):
    for btn in buttons.values():
        btn.destroy()
    label.destroy()
    
    if winner == 0:
        s = "It's a tie!"
    else: 
        s = f"Player {check_turn(turn)} wins!"
    # create a new, centered label
    win_label = tk.Label(root, text = s, font=('Helvetica', 24))
    win_label.place(relx = 0.5, rely = 0.5, anchor='center')

# create a 3x3 grid for game
for i in range (1, 10):
    btn = tk.Button(root, text="", width = 20, height = 8, command = lambda i = i: handle_click(i))
    btn.grid(row = (i-1) // 3, column = (i-1) % 3)
    buttons[i] = btn

root.mainloop()