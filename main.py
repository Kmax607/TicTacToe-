from colors import red, blue, green
import random

board = [blue("1"), blue("2"), blue("3"), blue("4"), blue("5"), blue("6"), blue("7"), blue("8"), blue("9")]

def print_board():
  print(board[0] + "|" + board[1] + "|" + board[2])
  print(board[3] + "|" + board[4] + "|" + board[5])
  print(board[6] + "|" + board[7] + "|" + board[8])

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
    else:
      print("Enter 'Yes' or 'Y' to play again")
    play_again = new_new_play_again
    return play_again

def check_wins():
  x_wins()
  o_wins()

x_turn = True


def play_game():
 global turns
 global x_won
 global o_won
 global x_name
 global o_name
 global play_again
 global x_turn
 print("Welcome to TicTacToe! Enter your name or enter COM for a computer player")
 print()
 new_x_name = input("Player 1: ")
 x_name = new_x_name
 new_o_name = input("Player 2: ")
 o_name = new_o_name
 while x_won == False and o_won == False:
   while turns < 9:
     print_board()
     if x_turn == True:
       if x_name == "COM":
         com_position = random.randint(0, 8)
         position = com_position
       else:
         position = input("Choose a position: ")
         position = int(position) - 1
       if board[position] == "X":
         print("Invalid position")
         x_turn = True
         turns -= 1
       if board[position] == "O":
        print("Invalid position")
        x_turn = True
        turns -= 1
       else:
         x_turn = False
         change_to_X(position)
     elif x_turn == False:
       if o_name == "COM":
         com_position = random.randint(0, 8)
         position = com_position - 1
       else:
         position = input("Choose a position: ")
         position = int(position) - 1
       x_turn = True
       if board[position] == red("X"):
        print("Invalid position")
        x_turn = False
        turns -= 1
       elif board[position] == green("O"):
        print("Invalid position")
        x_turn = False
        turns -= 1
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

def play_new_game():
  global turns
  global x_won
  global o_won
  global x_name
  global o_name
  global play_again
  global x_turn
  while x_won == False and o_won == False:
    while turns < 9:
      print_board()
      if x_turn == True:
        if x_name == "COM":
          com_position = random.randint(0, 8)
          position = com_position
        else:
          position = input("Choose a position: ")
          position = int(position) - 1
        if board[position] == "X":
          print("Invalid position")
          x_turn = True
          turns -= 1
        if board[position] == "O":
         print("Invalid position")
         x_turn = True
         turns -= 1
        else:
          x_turn = False
          change_to_X(position)
      elif x_turn == False:
        if o_name == "COM":
          com_position = random.randint(0, 8)
          position = com_position - 1
        else:
          position = input("Choose a position: ")
          position = int(position) - 1
        x_turn = True
        if board[position] == red("X"):
         print("Invalid position")
         x_turn = False
         turns -= 1
        elif board[position] == green("O"):
         print("Invalid position")
         x_turn = False
         turns -= 1
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

play_game()