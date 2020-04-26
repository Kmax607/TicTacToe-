from colors import red, blue, green, yellow
import random

board = [blue("1"), blue("2"), blue("3"), blue("4"), blue("5"), blue("6"), blue("7"), blue("8"), blue("9")]

def print_board():
 global x_wins
 global o_wins
 global x_name
 global o_name
 if x_num_wins > 4 and o_name == "COM":
   print(board[0] + yellow("|") + board[1] + yellow("|") + board[2])
   print(board[3] + yellow("|") + board[4] + yellow("|") + board[5])
   print(board[6] + yellow("|") + board[7] + yellow("|") + board[8])
   print()
 elif o_num_wins > 4 and x_name == "COM":
   print(board[0] + yellow("|") + board[1] + yellow("|") + board[2])
   print(board[3] + yellow("|") + board[4] + yellow("|") + board[5])
   print(board[6] + yellow("|") + board[7] + yellow("|") + board[8])
   print()
 else:
   print(board[0] + "|" + board[1] + "|" + board[2])
   print(board[3] + "|" + board[4] + "|" + board[5])
   print(board[6] + "|" + board[7] + "|" + board[8])
   print()

def change_to_X(pos):
  board[pos] = red("X")

def change_to_O(pos):
  board[pos] = green("O")

x_won = False
o_won = False
turns = 0
x_name = "X"
o_name = "O"
play_again = False
x_num_wins = 0
o_num_wins = 0
x_turn = True

#Determines if X won
def x_wins():
  global x_won
  global turns
  global x_name
  global x_num_wins
  if board[0] == board[1] == board[2] == red("X"):
    print_board()
    print(red(x_name + " wins!"))
    new_x_won = True
    x_won = new_x_won
    turns += 7
    x_num_wins += 1
    return x_num_wins
    return x_won
  if board[3] == board[4] == board[5] == red("X"):
    print_board()
    print(red(x_name + " wins!"))
    new_x_won = True
    x_won = new_x_won
    turns += 7
    x_num_wins += 1
    return x_num_wins
    return x_won
  if board[6] == board[7] == board[8] == red("X"):
    print_board()
    print(red(x_name + " wins!"))
    new_x_won = True
    x_won = new_x_won
    turns += 7
    x_num_wins += 1
    return x_num_wins
    return x_won
  if board[0] == board[3] == board[6] == red("X"):
    print_board()
    print(red(x_name + " wins!"))
    new_x_won = True
    x_won = new_x_won
    turns += 7
    x_num_wins += 1
    return x_num_wins
    return x_won
  if board[1] == board[4] == board[7] == red("X"):
    print_board()
    print(red(x_name + " wins!"))
    new_x_won = True
    x_won = new_x_won
    turns += 7
    x_num_wins += 1
    return x_num_wins
    return x_won
  if board[2] == board[5] == board[8] == red("X"):
    print_board()
    print(red(x_name + " wins!"))
    new_x_won = True
    x_won = new_x_won
    turns += 7
    x_num_wins += 1
    return x_num_wins
    return x_won
  if board[0] == red("X") and board[4] == red("X") and board[8] == red("X"):
    print_board()
    print(red(x_name + " wins!"))
    new_x_won = True
    x_won = new_x_won
    turns += 7
    x_num_wins += 1
    return x_num_wins
    return x_won
  if board[2] == board[4] == board[6] == red("X"):
    print_board()
    print(red(x_name + " wins!"))
    new_x_won = True
    x_won = new_x_won
    turns += 7
    x_num_wins += 1
    return x_num_wins
    return x_won





#Determines if O won
def o_wins():
  global o_won
  global turns
  global o_num_wins
  if board[0] == board[1] == board[2] == green("O"):
    print_board()
    print(green(o_name + " wins!"))
    new_o_won = True
    o_won = new_o_won
    turns += 7
    o_num_wins += 1
    return o_num_wins
    return o_won
  if board[3] == board[4] == board[5] == green("O"):
    print_board()
    print(green(o_name + " wins!"))
    new_o_won = True
    o_won = new_o_won
    turns += 7
    o_num_wins += 1
    return o_num_wins
    return o_won
  if board[6] == board[7] == board[8] == green("O"):
    print_board()
    print(green(o_name + " wins!"))
    new_o_won = True
    o_won = new_o_won
    turns += 7
    o_num_wins += 1
    return o_num_wins
    return o_won
  if board[0] == board[3] == board[6] == green("O"):
    print_board()
    print(green(o_name + " wins!"))
    new_o_won = True
    o_won = new_o_won
    turns += 7
    o_num_wins += 1
    return o_num_wins
    return o_won
  if board[1] == board[4] == board[7] == green("O"):
    print_board()
    print(green(o_name + " wins!"))
    new_o_won = True
    o_won = new_o_won
    turns += 7
    o_num_wins += 1
    return o_num_wins
    return o_won
  if board[2] == board[5] == board[8] == green("O"):
    print_board()
    print(green(o_name + " wins!"))
    new_o_won = True
    o_won = new_o_won
    turns += 7
    o_num_wins += 1
    return o_num_wins
    return o_won
  if board[0] == board[4] == board[8] == green("O"):
    print_board()
    print(green(o_name + " wins!"))
    new_o_won = True
    o_won = new_o_won
    turns += 7
    o_num_wins += 1
    return o_num_wins
    return o_won
  if board[2] == board[4] == board[6] == green("O"):
    print_board()
    print(green(o_name + " wins!"))
    new_o_won = True
    o_won = new_o_won
    turns += 7
    o_num_wins += 1
    return o_num_wins
    return o_won






#after a game ends, program goes through this function to determine whether or not to play again and display scoreboard
def new_game():
  global play_again
  global x_won
  global o_won
  global x_name
  global o_name
  global x_num_wins
  global o_num_wins
  if x_won == True or o_won == True or turns >= 9:
    if x_num_wins == o_num_wins:
      print("It's all tied up!")
    elif x_num_wins == o_num_wins + 1:
      print(red(x_name) + " is in the lead!")
    elif o_num_wins == x_num_wins + 1:
      print(green(o_name) + " is in the lead!")
    elif x_num_wins == o_num_wins + 2:
      print(red(x_name) + " is pulling away!")
    elif o_num_wins == x_num_wins + 2:
      print(green(o_name) + " is pulling away!")
    elif x_num_wins > o_num_wins + 2:
      print(red(x_name) + " has a commanding lead!")
    else:
      print(green(o_name) + " has a commanding lead!")
    print(red(x_name + ": " + str(x_num_wins)))
    print(green(o_name + ": " + str(o_num_wins)))
    new_play_again = input("Play again? ")
    if new_play_again == ("Yes") or new_play_again == ("yes") or new_play_again == ("Y") or new_play_again == ("y"):
      new_new_play_again = True
    while new_play_again not in ["Yes", "yes", "Y", "y"]:
     print("Enter 'Yes' or 'Y' to play again")
     new_play_again = input("Play again? ")
     if new_play_again == ("Yes") or new_play_again == ("yes") or new_play_again == ("Y") or new_play_again == ("y"):
      new_new_play_again = True
    play_again = new_new_play_again
    return play_again



#Checks wins, honestly kind of useless
def check_wins():
  x_wins()
  o_wins()






#First game only
def play_game():
 global turns
 global x_won
 global o_won
 global x_name
 global o_name
 global play_again
 global x_turn
 global position
 print("Welcome to Tic Tac Toe! Enter your name or enter COM for a computer player. Beat the computer 5 times to win a prize!")
 print()
 new_x_name = input("Player 1: ")
 x_name = new_x_name
 new_o_name = input("Player 2: ")
 o_name = new_o_name
 while x_won == False and o_won == False and turns < 9:
   while turns < 9:
     print_board()
     if x_turn == True:
       if x_name == "COM":
        ai_logic()
       else:
         position = input("Choose a position: ")
         position = int(position) - 1
       if board[position] == red("X"):
         print("Invalid position")
         x_turn = True
         turns -= 1
         board[position] = red("X")
       if board[position] == green("O"):
        print("Invalid position")
        x_turn = True
        turns -= 1
        board[position] = green("O")
       else:
         x_turn = False
         change_to_X(position)
     elif x_turn == False:
       if o_name == "COM":
         ai_logic()
       else:
         position = input("Choose a position: ")
         position = int(position) - 1
       x_turn = True
       if board[position] == red("X"):
        print("Invalid position")
        x_turn = False
        turns -= 1
        board[position] = red("X")
       elif board[position] == green("O"):
        print("Invalid position")
        x_turn = False
        turns -= 1
        board[position] = green("O")
       else:
        x_turn = True
        change_to_O(position)
     turns += 1
     check_wins()
     if turns >= 9 and x_won == False and o_won == False:
       print("TIE!")
   new_game()
 if play_again == True:
   x_won = False
   o_won = False
   turns = 0
   board[0] = blue("1")
   board[1] = blue("2")
   board[2] = blue("3")
   board[3] = blue("4")
   board[4] = blue("5")
   board[5] = blue("6")
   board[6] = blue("7")
   board[7] = blue("8")
   board[8] = blue("9")
   play_new_game()
 return x_turn








#Logic for computer players
def ai_logic():
  global position
  global board  
  global x_turn
  global turns
  #Horizontal offense
  if board[1] == green("O") and board[2] == green("O") and board[0] == blue("1"):
   com_position = 0
  elif board[0] == green("O") and board[1] == green("O") and board[1] == blue("2"):
   com_position = 1
  elif board[0] == green("O") and board[1] == green("O") and board[2] == blue("3"):
   com_position = 2
  elif board[4] == green("O") and board[5] == green("O") and board[3] == blue("4"):
   com_position = 3
  elif board[3] == green("O") and board[5] == green("O") and board[4] == blue("5"):
   com_position = 4
  elif board[3] == green("O") and board[4] == green("O") and board[5] == blue("6"):
   com_position = 5
  elif board[7] == green("O") and board[8] == green("O") and board[6] == blue("7"):
   com_position = 6
  elif board[6] == green("O") and board[8] == green("O") and board[7] == blue("8"):
   com_position = 7
  elif board[6] == green("O") and board[7] == green("O") and board[8] == blue("9"):
   com_position = 8
  #Diagonal offense 
  elif board[4] == green("O") and board[8] == green("O") and board[0] == blue("1"):
   com_position = 0
  elif board[4] == green("O") and board[0] == green("O") and board[8] == blue("9"):
    com_position = 8
  elif board[0] == green("O") and board[8] == green("O") and board[4] == blue("2"):
   com_position = 4
  elif board[4] == green("O") and board[6] == green("O") and board[2] == blue("3"):
   com_position = 2
  elif board[4] == green("O") and board[2] == green("O") and board[6] == blue("7"):
    com_position = 6
  elif board[2] == green("O") and board[6] == green("O") and board[4] == blue("5"):
    com_position = 4
  #Horizontal defense
  elif board[1] == green("O") and board[2] == green("O") and board[0] == blue("1"):
   com_position = 0
  elif board[0] == red("X") and board[1] == red("X") and board[1] == blue("2"):
   com_position = 1
  elif board[0] == red("X") and board[1] == red("X") and board[2] == blue("3"):
   com_position = 2
  elif board[4] == red("X") and board[5] == red("X") and board[3] == blue("4"):
   com_position = 3
  elif board[3] == red("X") and board[5] == red("X") and board[4] == blue("5"):
   com_position = 4
  elif board[3] == red("X") and board[4] == red("X") and board[5] == blue("6"):
   com_position = 5
  elif board[7] == red("X") and board[8] == red("X") and board[6] == blue("7"):
   com_position = 6
  elif board[6] == red("X") and board[8] == red("X") and board[7] == blue("8"):
   com_position = 7
  elif board[6] == red("X") and board[7] == red("X") and board[8] == blue("9"):
   com_position = 8
  #Vertical defense 
  elif board[3] == red("X") and board[6] == red("X") and board[0] == blue("1"):
   com_position = 0
  elif board[4] == red("X") and board[7] == red("X") and board[1] == blue("2"):
   com_position = 1
  elif board[5] == red("X") and board[8] == red("X") and board[2] == blue("3"):
   com_position = 2
  elif board[6] == red("X") and board[1] == red("X") and board[3] == blue("4"):
   com_position = 3
  elif board[1] == red("X") and board[7] == red("X") and board[4] == blue("5"):
   com_position = 4
  elif board[2] == red("X") and board[8] == red("X") and board[5] == blue("6"):
   com_position = 5
  elif board[0] == red("X") and board[5] == red("X") and board[6] == blue("7"):
   com_position = 6
  elif board[1] == red("X") and board[4] == red("X") and board[7] == blue("8"):
   com_position = 7
  elif board[2] == red("X") and board[5] == red("X") and board[8] == blue("9"):
   com_position = 8
  #Diagonal defense 
  elif board[4] == red("X") and board[8] == red("X") and board[0] == blue("1"):
   com_position = 0
  elif board[4] == red("X") and board[0] == red("X") and board[8] == blue("9"):
    com_position = 8
  elif board[0] == red("X") and board[8] == red("X") and board[4] == blue("2"):
   com_position = 4
  elif board[4] == red("X") and board[6] == red("X") and board[2] == blue("3"):
   com_position = 2
  elif board[4] == red("X") and board[2] == red("X") and board[6] == blue("7"):
    com_position = 6
  elif board[2] == red("X") and board[6] == red("X") and board[4] == blue("5"):
    com_position = 4
  else:
   com_position = random.randint(0, 8)
  position = com_position
  return position
  turns -= 1
  return x_turn
  return turns








#Plays all games excluding the first one
def play_new_game():
  global turns
  global x_won
  global o_won
  global x_name
  global o_name
  global play_again
  global x_turn
  global position
  while x_won == False and o_won == False and turns < 9:
    while turns < 9:
      print_board()
      if x_turn == True:
        if x_name == "COM":
          ai_logic()
        else:
          position = input("Choose a position: ")
          position = int(position) - 1
        if board[position] == red("X"):
          print("Invalid position")
          x_turn = True
          turns -= 1
          board[position] = red("X")
        if board[position] == green("O"):
          print("Invalid position")
          x_turn = True
          turns -= 1
          board[position] = green("O")
        else:
          x_turn = False
          change_to_X(position)
      elif x_turn == False:
        if o_name == "COM":
          ai_logic()
        else:
          position = input("Choose a position: ")
          position = int(position) - 1
        x_turn = True
        if board[position] == red("X"):
          print("Invalid position")
          x_turn = False
          turns -= 1
          board[position] = red("X")
        elif board[position] == green("O"):
          print("Invalid position")
          x_turn = False
          turns -= 1
          board[position] = green("O")
        else:
          x_turn = True
          change_to_O(position)
      turns += 1
      check_wins()
      if turns >= 9 and x_won == False and o_won == False:
        print("TIE!")
    new_game()
  if play_again == True:
    x_won = False
    o_won = False
    turns = 0
    board[0] = blue("1")
    board[1] = blue("2")
    board[2] = blue("3")
    board[3] = blue("4")
    board[4] = blue("5")
    board[5] = blue("6")
    board[6] = blue("7")
    board[7] = blue("8")
    board[8] = blue("9")
    play_new_game()
  return x_turn

play_game()