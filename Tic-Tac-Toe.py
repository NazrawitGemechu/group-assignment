# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
current_player = "X"


# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():

    # Show the initial game board
    display_board()

    # Loop until the game stops (winner or tie)
    while game_still_going:

        # Handle a turn
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # Since the game is over, print the winner or tie
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# Display the game board to the screen
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):
    # Get position from player
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Get correct index in our board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the board
    board[position] = player

    # Show the game board
    display_board()


# Check if the game is over
def check_if_game_over():
    check_for_winner()
    check_for_tie()


# Check to see if somebody has won
def check_for_winner():
   # Set global variables
    global winner
    # Check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check the rows for a win
def check_rows():
   pass

# Check the columns for a win
def check_columns():
    pass


# Check the diagonals for a win
def check_diagonals():
    pass


# Check if there is a tie
def check_for_tie():
    pass


# Flip the current player from X to O, or O to X
def flip_player():
   pass


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()
