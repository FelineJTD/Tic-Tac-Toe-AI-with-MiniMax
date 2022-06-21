from sys import base_prefix
from board import Board

if __name__ == '__main__':
  print('Welcome to Tic-Tac-Toe!')

  board = Board()

  # Choose symbol
  symbol = input('Choose symbol (X or O): ')
  while symbol != 'X' and symbol != 'O':
    symbol = input('Invalid input. Choose symbol (X or O): ')
  board.set_symbol(symbol)

  # print board
  board.print()
  
  # Gameplay
  while (not (board.is_full())):
    # get user input
    move = input('Enter your move (1-9): ')
    while(not (board.make_move(int(move), "user"))): # invalid move
      move = input('Invalid move. Enter your move (1-9): ')
    # print board
    board.print()
    # check if user won
    if (board.check_win("user")):
      print('You win!')
      exit(0)
    # check if board is full
    if (board.is_full()):
      print('Draw!')
      exit(0)

    # AI move
    move = board.get_best_move("AI")
    board.make_move(move, "AI")
    # print board
    print("AI's move: " + str(move))
    board.print()
    # check if AI won
    if (board.check_win("AI")):
      board.print()
      print('AI wins!')
      exit(0)