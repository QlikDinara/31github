import numpy as np
a = np.array([['1', '2','3'],
              ['4', '5', '6'],
              ['7', '8', '9']])



def chooseXO(XO,counter):
    print ("Pick a number from 1 to 9 and make your move")
    #o=input()
    jj = np.where(a == XO)
    x_coor=jj[0]
    y_coor=jj[1]
    if((int(o)>=1) or (int(o)<=9) and a.size>0):
      if (len(x_coor) == 0 and len(y_coor)==0):
        print("This cell was already picked or out of the range, please choose another one")
        chooseXO(XO)
      elif ((a[x_coor,y_coor]!='X') or (a[x_coor,y_coor]!='O')):
        if counter%2==1:
            a[x_coor,y_coor]='X'
        else:
            a[x_coor,y_coor]='O'
      print(a)
    
def chooseO():
  print ("O: Pick a number from 1 to 9 and make your move")
  o=input()
  jj = np.where(a == o)
  x_coor=jj[0]
  y_coor=jj[1]
  if((int(o)>=1) or (int(o)<=9) and a.size>0):
    if (len(x_coor) == 0 and len(y_coor)==0):
      print("This cell was already picked or out of the range, please choose another one")
      chooseO()
    elif ((a[x_coor,y_coor]!='X') or (a[x_coor,y_coor]!='O')):
      a[x_coor,y_coor]='O'
    print("board ",a)

def determine_winner(game_board):
  winner=None
  j=0
  for i in range(3):
        if a[i][j] == a[i][j+1] == a[i][j+2] and a[i][j] in ('X', 'O'):
         # print('Winner is row',a[i][j])
          winner=a[i][j]
  l=0
  for k in range(3):
    if a[l][k] == a[l+1][k] == a[l+2][k] and a[l][k] in ('X', 'O'):
      #print('Winner is column',a[l][k])
      winner=a[l][k]
  r=0
  c=0
  if a[r][c] == a[r+1][c+1] == a[r+2][c+2] and a[r][c] in ('X', 'O'):
      #print('Winner is diagonal',a[r][c])
      winner=a[r][c]
  x=0
  y=2
  if a[x][y] == a[x+1][y-1] == a[x+2][y-2] and a[x][y] in ('X', 'O'):
    #print('Winner is counter diagonal',a[x][y])
    winner=a[x][y]
  return winner

counter=1
while not determine_winner(a):
    print(a)
    o=input()
    chooseXO(o, counter)
    print("Winner is ",determine_winner(a))
    counter=counter+1
    """chooseO()
    determine_winner(a)"""

     
