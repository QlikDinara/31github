import numpy as np


class Board():
    def __init__(self):
      self.cells=np.array([['1', '2','3'],
                        ['4', '5', '6'],
                        ['7', '8', '9']])
    def display_board(self):
       print(self.cells) 

    def make_move(self, cell, player):
      jj = np.where(self.cells == str(cell))
      x_coor=jj[0]
      y_coor=jj[1]
      if (self.cells[x_coor,y_coor] != 'X' or self.cells[x_coor,y_coor] != 'O'):
        self.cells[x_coor,y_coor]=player
      else: 
        print("This cell was already picked or out of the range, please choose another one")
        