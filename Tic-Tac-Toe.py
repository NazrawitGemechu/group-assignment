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
    pass


# Handle a turn for an arbitrary player
def handle_turn(player):
    pass


# Check if the game is over
def check_if_game_over():
    pass


# Check to see if somebody has won
def check_for_winner():
   pass


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
