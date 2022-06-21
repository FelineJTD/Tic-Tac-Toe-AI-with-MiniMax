from curses.ascii import isdigit

from sympy import symbols


class Board:
  # A class that represents a board Tic-Tac-Toe

  def __init__(self, blocks=[[str(j*3+i+1) for i in range(3)] for j in range(3)], symbols={"user": "X", "AI": "O"}):
    self.blocks = blocks
    self.symbols = symbols

  def set_symbol(self, symbol):
    # set the symbol for the user
    self.symbols["user"] = "\033[91m\033[1m" + symbol + "\033[0m\033[0m"
    self.symbols["AI"] = "\033[92m\033[1m" + ("X" if symbol == "O" else "O") + "\033[0m\033[0m"

  def copy(self):
    temp = []
    for i in range(3):
      temp.append(self.blocks[i][:])
    return Board(temp, self.symbols)

  def print(self):
    # print board
    for i in range(3):
      print(' ' + ' | '.join(self.blocks[i]))
      if i != 2:
        print('---+---+---')
    print()

  def is_full(self):
    # check if the board is full
    for i in range(3):
      for j in range(3):
        if (self.blocks[i][j]).isdigit():
          return False
    return True

  def make_move(self, i, player):
    # make a move on the board
    if (not (self.blocks[(i-1)//3][(i-1)%3]).isdigit()): # block already filled
      return False
    self.blocks[(i-1)//3][(i-1)%3] = self.symbols[player]
    return True

  def check_win(self, player):
    # check if the player has won
    for i in range(3):
      if (self.blocks[i][0] == self.symbols[player] and self.blocks[i][1] == self.symbols[player] and self.blocks[i][2] == self.symbols[player]):
        return True
      if (self.blocks[0][i] == self.symbols[player] and self.blocks[1][i] == self.symbols[player] and self.blocks[2][i] == self.symbols[player]):
        return True
    if (self.blocks[0][0] == self.symbols[player] and self.blocks[1][1] == self.symbols[player] and self.blocks[2][2] == self.symbols[player]):
      return True
    if (self.blocks[0][2] == self.symbols[player] and self.blocks[1][1] == self.symbols[player] and self.blocks[2][0] == self.symbols[player]):
      return True
    return False

  def minimax(self, board, player):
    # find the best move for the player
    if (board.check_win("AI")):
      return -1
    if (board.check_win("user")):
      return 1
    if (board.is_full()):
      return 0
    if (player == "AI"):
      best = -2
      for i in range(3):
        for j in range(3):
          if (board.blocks[i][j]).isdigit():
            new_board = board.copy()
            new_board.make_move(i*3+j+1, "user")
            score = new_board.minimax(new_board, "user")
            if (score > best):
              best = score
      return best
    else:
      best = 2
      for i in range(3):
        for j in range(3):
          if (board.blocks[i][j]).isdigit():
            new_board = board.copy()
            new_board.make_move(i*3+j+1, "AI")
            score = new_board.minimax(new_board, "AI")
            if (score < best):
              best = score
      return best

  def get_best_move(self):
    # find the best move for the player
    best = 2
    for i in range(3):
      for j in range(3):
        if (self.blocks[i][j]).isdigit():
          new_board = self.copy()
          new_board.make_move(i*3+j+1, "AI")
          score = new_board.minimax(new_board, "AI")
          if (score < best):
            best = score
            move = i*3+j+1
    return move