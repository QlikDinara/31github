import numpy as np
a = np.array([['1', '2','3'],
              ['4', '5', '6'],
              ['7', '8', '9']])
print(a)

def chooseX():
    print ("X: Pick a number from 1 to 9 and make your move")
    o=input()
    jj = np.where(a == o)
    x_coor=jj[0]
    y_coor=jj[1]
    if((int(o)>=1) or (int(o)<=9) and a.size>0):
      if (len(x_coor) == 0 and len(y_coor)==0):
        print("This cell was already picked or out of the range, please choose another one")
        chooseO()
      elif ((a[x_coor,y_coor]!='X') or (a[x_coor,y_coor]!='O')):
        a[x_coor,y_coor]='X'
      print(a)
    
def chooseO():
  print ("O: Pick a number from 1 to 9 and make your move")
  o=input()
  jj = np.where(a == o)
  print(x_coor)
  print(y_coor)
  if((int(o)>=1) or (int(o)<=9) and a.size>0):
    if (len(x_coor) == 0 and len(y_coor)==0):
      print("This cell was already picked or out of the range, please choose another one")
      chooseO()
    elif ((a[x_coor,y_coor]!='X') or (a[x_coor,y_coor]!='O')):
      a[x_coor,y_coor]='O'
    print(a)

while True:
  for step in range(0,9):
    chooseX()
    chooseO()
      
     
