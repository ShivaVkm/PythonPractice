# import os
# import time

# board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
# player = 1

# ########win Flags##########
# Win = 1
# Draw = -1
# Running = 0
# Stop = 1
# ###########################
# Game = Running
# Mark = 'X'

# #This Function Draws Game Board 
# def DrawBoard():
#     print(" %c | %c | %c " % (board[1],board[2],board[3]))
#     print("___|___|___")
#     print(" %c | %c | %c " % (board[4],board[5],board[6]))
#     print("___|___|___")
#     print(" %c | %c | %c " % (board[7],board[8],board[9]))
#     print(" | | ")

# #This Function Checks position is empty or not
# def CheckPosition(x):
#     if(board[x] == ' '):
#         return True
#     else:
#         return False

# #This Function Checks player has won or not
# def CheckWin():
#     global Game
#     #Horizontal winning condition
#     if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
#         Game = Win
#     elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
#         Game = Win
#     elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
#         Game = Win
#     #Vertical Winning Condition
#     elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
#         Game = Win
#     elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
#         Game = Win
#     elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
#         Game=Win
#     #Diagonal Winning Condition
#     elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
#         Game = Win
#     elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
#         Game=Win
#     #Match Tie or Draw Condition
#     elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and
#     board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '): 
#         Game=Draw
#     else:
#         Game=Running

# print("Tic-Tac-Toe Game")
# print("Player 1 [X] --- Player 2 [O]\n")
# print()
# print()
# print("Please Wait...")
# time.sleep(1)
# while(Game == Running):
#     os.system('cls')
#     DrawBoard()
#     if(player % 2 != 0):
#         print("Player 1's chance")
#         Mark = 'X'
#     else:
#         print("Player 2's chance")
#         Mark = 'O'
#     choice = int(input("Enter the position between [1-9] where you want to mark :"))
#     if(CheckPosition(choice)):
#         board[choice] = Mark
#         player+=1
#         CheckWin()

# os.system('cls')
# DrawBoard()
# if(Game==Draw):
#     print("Game Draw")
# elif(Game==Win):
#     player-=1
#     if(player%2!=0):
#         print("Player 1 Won")
#     else:
#         print("Player 2 Won") 









# --------- Global Variables -----------

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
  # Set global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or return None if there was no winner
  else:
    return None


# Check the columns for a win
def check_columns():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Or return None if there was no winner
  else:
    return None


# Check if there is a tie
def check_for_tie():
  # Set global variables
  global game_still_going
  # If board is full
  if "-" not in board:
    game_still_going = False
    return True
  # Else there is no tie
  else:
    return False


# Flip the current player from X to O, or O to X
def flip_player():
  # Global variables we need
  global current_player
  # If the current player was X, make it O
  if current_player == "X":
    current_player = "O"
  # Or if the current player was O, make it X
  elif current_player == "O":
    current_player = "X"


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()