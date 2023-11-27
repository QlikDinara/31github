import numpy as np
a = np.array([['1', '2','3'],
              ['4', '5', '6'],
              ['7', '8', '9']])
print(a)

def chooseX():
  print ("X: Pick a number from 1 to 9 and make your move")
  x=input()
  ii = np.where(a == x)
  xcoor=ii[0]
  ycoor=ii[1]
  if (a.size>0):
    if (len(ii) == 0):
      print("X: This cell was already picked choose another one")
      chooseX()
    if ((a[xcoor,ycoor]!='X') or (a[xcoor,ycoor]!='O')):
      print('no existing')
      a[xcoor,ycoor]='X'
    print(a)
    
def chooseO():
  print ("O: Pick a number from 1 to 9 and make your move")
  o=input()
  jj = np.where(a == o)
  print(jj)
  x_coor=jj[0]
  y_coor=jj[1]
  print(x_coor)
  print(y_coor)
  if (a.size>0):
    if (len(x_coor) == 0 and len(y_coor)==0):
      print("This cell was already picked choose another one")
      chooseO()
    if ((a[x_coor,y_coor]!='X') or (a[x_coor,y_coor]!='O')):
      print('not existing')
      a[x_coor,y_coor]='O'
    print(a)

while True:
  for step in range(0,9):
    #chooseX()
    chooseO()
      
     
