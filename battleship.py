# Welcome to Battleship!
# In this project you will build a simplified, one-player version of the classic board game Battleship! 
# In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid. The player will have 10 guesses to try to sink the ship.
# To build this game we will use our knowledge of lists, conditionals and functions in Python.

# Make the board:
# Good! Now we'll use a built-in Python function to generate our board, which we'll make into a 5 x 5 grid of all "O"s, for "ocean."
# Ex. print(["O"] * 5) --> will print out ['O', 'O', 'O', 'O', 'O'], which is the basis for a row of our board.
# We'll do this five times to make five rows. (Since we have to do this five times, it sounds like a loop might be in order.)
# Create a 5 x 5 grid initialized to all 'O's and store it in board.

# import randin(low, high) from random module to create random number (for ship placement)
from random import randint 

# Set board to blank
board = []

# create the board by creating a list of five 'O's, five time
for x in range(0, 5):
    board.append(["O"] * 5)

#format the print layout to appear like a board
def print_board(board_in):
  for row in board:
    # " ".join will remove the quotes around the Os
    print( " ".join(row))
    
# using the randint function, create a random row and random column for the ship
def random_row(board_in):
  return randint(0, len(board_in) - 1)

def random_col(board_in):
  return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# printing for debug purposes
# print ship_row
# print ship_col

# For loop that gives a player 4 guesses
for turn in range(4):
    # Code to allow someone to guess where the ship is
    # Python 2 uses raw_input
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col: "))

    # Check if guesses match ship location. If not, change that O to an X
    if guess_row == ship_row and guess_col == ship_col:
      print("Congratulations! You sank my battleship!")  
      # Break command will end the for loop
      break  
    else:
    # check to make sure guess is on the 5x5 board. Note* ' \ ' at the end just continues the command onto the next line
        if guess_row not in range(5) or \
            guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        #check to see if this spot has been guessed already
        elif (board[guess_row][guess_col] == 'X'):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print("Game Over")
    # print_board(board)

