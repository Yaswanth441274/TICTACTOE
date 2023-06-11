#code written by Kavitha

import random,sys,time
n=[j for j in range(1,10)]
board=[" "for i in range(9)]
print("TIC-TAC-TOE")
def print_board():
  row1="|{}|{}|{}|".format(board[0],board[1],board[2])
  row2="|{}|{}|{}|".format(board[3],board[4],board[5])
  row3="|{}|{}|{}|".format(board[6],board[7],board[8])
  print(row1)
  print(row2)
  print(row3)
def player_move(icon):
  if icon=='X':
    number=1
  elif icon=="O":
    number=2
  print("your turn player {}".format(number))
  choice1=int(input("enter your move(1-9):").strip())
  if choice1>0 and choice1<=9:
    if board[choice1-1]==" ":
      board[choice1-1]=icon
    else:
      print()
      print("The space was taken")
      print()
      player_move(icon) 
  else:
    print("invalid move....please enter again")
    player_move(icon)
def player_movec(icon):
  n1=random.choice(n)
  print("computer turn  :")
  time.sleep(0.5)
  print(n1)
  time.sleep(1)
  if board[n1-1]==" ":
    board[n1-1]=icon 
  else:
    print("this space was taken....")
    print()
    player_movec(icon)
def is_victory(icon):
  if(board[0]==icon and board[1]==icon and board[2]==icon)or\
    (board[3]==icon and board[4]==icon and board[5]==icon)or\
    (board[6]==icon and board[7]==icon and board[8]==icon)or\
    (board[0]==icon and board[3]==icon and board[6]==icon)or\
    (board[1]==icon and board[4]==icon and board[7]==icon)or\
    (board[2]==icon and board[5]==icon and board[8]==icon)or\
    (board[0]==icon and board[4]==icon and board[8]==icon)or\
    (board[2]==icon and board[4]==icon and board[6]==icon):
    return True
  else:
    return False
def isdraw():
  if " " not in board:
    return True
  else:
    return False
while True:
  ch=int(input("which mode you want to play\n 1.computer vs player\n 2.player vs player\n choice: "))
  if ch==1:
    while True:
     print_board()
     player_move("X")
     print_board()
     if is_victory("X"):
      print("player X wins......congratulations")
      sys.exit()
     elif isdraw():
      print("is draw")
      sys.exit()
     print_board()
     player_movec("O")
     print_board()
     if is_victory("O"):
      print("player O wins......congratulations")
      sys.exit()
     elif isdraw():
      print("is draw")
      sys.exit()
  elif ch==2:
    while True:
     print_board()
     player_move("X")
     print_board()
     if is_victory("X"):
      print("player X wins......congratulations")
      sys.exit()
     elif isdraw():
      print("is draw")
      sys.exit()
     print_board()
     player_movec("O")
     print_board()
     if is_victory("O"):
      print("player O wins......congratulations")
      sys.exit()
     elif isdraw():
      print("is draw")
      sys.exit()
  else:
    print("enter again")
