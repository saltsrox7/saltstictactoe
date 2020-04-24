# ----Global Variables-----
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

winner = None

player = "X"

tie = False

move = True


# Function to display the board
def display_board():
    print(board[0] + " " + "|" + " " + board[1] + " " + "|" + " " + board[2])
    print(board[3] + " " + "|" + " " + board[4] + " " + "|" + " " + board[5])
    print(board[6] + " " + "|" + " " + board[7] + " " + "|" + " " + board[8])


# Plays Turns
def play_tic_tac_toe():
    global winner
    global tie
    while winner == None and tie == False:
        display_board()
        place_player()
        check_row_win()
        check_column_win()
        check_diagonal_win()
        check_tie()
        change_turn()

#Changes which player's turn it is
def change_turn():
    global player
    global move
    if move == True:
         if player == "X":
        player = "0"
         elif player == "0":
        player = "X"

#Handles placing X or 0 on the board, along with some error handling
def place_player():
    global player
    global move
    print(f'''It's {player}'s turn.''')
    player_input = input('Choose a place 1-9 ')
    if player_input in ["1", "2", "3", "4", "5", "6", "7", "8", "9",] and board[int(player_input) - 1] == "-":
        move = True
    else:
        move = False
    if move:
        player_spot = int(player_input) - 1
        board[player_spot] = player
    else:
        print('That input is not valid, go again.')
    return
#checks for wins in rows
def check_row_win():
    global winner
    global player

    if board[0] == board[1] == board[2] != "-":
        winner = True
    elif board[3] == board[4] == board[5] != "-":
        winner = True
    elif board[6] == board[7] == board[8] != "-":
        winner = True

    if winner == True:
        display_board()
        print(player + ' won, game over.')

    return

#checks for wins in columns
def check_column_win():
    global winner
    global player
    if board[0] == board[3] == board[6] != "-":
        winner = True
    elif board[1] == board[4] == board[7] != "-":
        winner = True
    elif board[2] == board[5] == board[8] != "-":
        winner = True
    if winner == True:
        display_board()
        print(player + ' won, game over.')

    return

#checks for wins in diagonals
def check_diagonal_win():
    global winner
    global player
    if board[0] == board[4] == board[8] != "-":
        winner = True
    elif board[2] == board[4] == board[6] != "-":
        winner = True
    if winner == True:
        display_board()
        print(player + ' won, game over.')

    return

#checks for ties
def check_tie():
    global tie
    if "-" in board:
        tie = False
    elif "-" not in board:
        tie = True
    if tie == True:
        display_board()
        print('You tied; game over.')


    return


play_tic_tac_toe()
