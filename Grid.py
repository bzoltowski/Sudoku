import random

def GenGrid():


  FirstRandomNumbers=random.sample(xrange(1,10),9)
  Grid=[FirstRandomNumbers]


  tmp = FirstRandomNumbers[3:] + FirstRandomNumbers[:3]
  Grid.append(tmp)
  tmp = FirstRandomNumbers[6:] + FirstRandomNumbers[:6]
  Grid.append(tmp)
  tmp = FirstRandomNumbers[1:] + FirstRandomNumbers[:1]
  Grid.append(tmp)
  tmp = FirstRandomNumbers[4:] + FirstRandomNumbers[:4]
  Grid.append(tmp)
  tmp = FirstRandomNumbers[7:] + FirstRandomNumbers[:7]
  Grid.append(tmp)
  tmp = FirstRandomNumbers[2:] + FirstRandomNumbers[:2]
  Grid.append(tmp)
  tmp = FirstRandomNumbers[5:] + FirstRandomNumbers[:5]
  Grid.append(tmp)
  tmp = FirstRandomNumbers[8:] + FirstRandomNumbers[:8]
  Grid.append(tmp)
  return Grid

  
Grid = GenGrid()
  

def SaveToFile():
  file  = open('out.txt', 'w')
  for i in range(0,9):
    for j in range(0,9):
      z = str(Grid[i][j])
      file.write(z+' ' )
    file.write('\n')
  file.close()  
  
def printGrid( tmp ):
  for i in range(0,9):
    for j in range(0,9):
      print '{:4}'.format(tmp[i][j]),
    print
#printGrid(Grid)
	
def Switch_Boxs(Box1, Box2):
  Boxs=[[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
  tmpBox2=Boxs[Box2][1]
  for i in range(Boxs[Box1][0],Boxs[Box1][0]+3):
    for j in range(Boxs[Box1][1],Boxs[Box1][1]+3):
      Grid[i][j], Grid[Boxs[Box2][0]][Boxs[Box2][1]] = Grid[Boxs[Box2][0]][Boxs[Box2][1]], Grid[i][j]
      #print i,j,Boxs[Box2][0],Boxs[Box2][1]      
      Boxs[Box2][1]+=1

#      print '{:4}'.format(Grid[i][j]),
    Boxs[Box2][1]=tmpBox2
    Boxs[Box2][0]=(Boxs[Box2][0]+1)
  print
  

 
  
def Switch_Cubes_x(Cube1_x, Cube2_x):
  for i in range(0,9):
    Grid[i][Cube1_x], Grid[i][Cube2_x] = Grid[i][Cube2_x], Grid[i][Cube1_x]  

def Switch_Cubes_y(Cube1_y, Cube2_y):
  for i in range(0,9):
    Grid[Cube1_y][i], Grid[Cube2_y][i] = Grid[Cube2_y][i], Grid[Cube1_y][i]  
 
def Switch_Diagonal_Matrix():
  tmpGrid = Grid
  tmpGrid = zip(tmpGrid[0], tmpGrid[1], tmpGrid[2], tmpGrid[3], tmpGrid[4], tmpGrid[5], tmpGrid[6], tmpGrid[7], tmpGrid[8])
  for i in range(0,9):
    for j in range(0,9):
      Grid[i][j]=tmpGrid[i][j]

def Switch_Diagonal_Revers_Matrix():
  tmpGrid = Grid
  tmpGrid.reverse()
  tmpGrid = zip(tmpGrid[0], tmpGrid[1], tmpGrid[2], tmpGrid[3], tmpGrid[4], tmpGrid[5], tmpGrid[6], tmpGrid[7], tmpGrid[8])
  tmpGrid.reverse()
  for i in range(0,9):
    for j in range(0,9):
      Grid[i][j]=tmpGrid[i][j]
  
  
  
def Colision():
  
  for i in range(9):
    Test_x=[0,0,0,0,0,0,0,0,0,0,0]
    Test_y=[0,0,0,0,0,0,0,0,0,0,0]
    for j in range(9):
      Test_x[Grid[i][j]]+=1
      Test_y[Grid[j][i]]+=1
    for k in range(1,10):
      if(Test_x[k]>1 or Test_y[k]>1):
        return 1
  Boxs=[[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
  
  for k in range(9):
    tmp = [0,0,0,0,0,0,0,0,0,0]
    for i in range(Boxs[k][0],Boxs[k][0]+3):
      for j in range(Boxs[k][1],Boxs[k][1]+3):
        #print (i%3)*3+(j%3)
        tmp[(i%3)*3+(j%3)+1]+=1      
    for i in range(1,10):
        if(tmp[i]>1):
          return 1
      
  
  return 0
   

#####################################
#	Prezentacja na pierwsza ocene	#
#####################################
print "Wygenerowana Tablica"
printGrid(Grid)


if(Colision()):
  print "Kolizja"
else:
  print "Brak kolizji" 


Switch_Cubes_x(0,2)
print "Zamiana kolumn 1 oraz 3"
printGrid(Grid)

if(Colision()):
  print "Kolizja"
else:
  print "Brak kolizji"

Switch_Cubes_y(0,8)
print "Zamiana wierszy 1 oraz 9"
printGrid(Grid)

if(Colision()):
  print "Kolizja"
else:
  print "Brak kolizji"

Switch_Diagonal_Matrix()
print "Zamiana wzgledem przekatnej"
printGrid(Grid)

if(Colision()):
  print "Kolizja"
else:
  print "Brak kolizji"
Switch_Diagonal_Revers_Matrix()

print "Zamiana wzgledem drugiej przekatnej"
printGrid(Grid)


if(Colision()):
  print "Kolizja"
else:
  print "Brak kolizji"
'''
#####################################

#AFTER MAKE GRID, SWITCHS && CHECK COLISIONS:

Sudoku = Grid

 #  Boxs=[[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
def GenZeroCount( lv,  min=0, max=0 ):
  if(lv<0 or lv>=3):
    return 1
  if(lv==0):#lv low
    min=17
    max=32
  if(lv==1):#lv medium
    min=33
    max=44
  if(lv==2):#lv High
    min=45
    max=60

  while True:#OGRANICZYC ILOSC!!
    ZeroCount = [0,0,0,0,0]
    randtmp = random.randint(min,max)
    sumZero = randtmp
    
#    print "####",sumZero
    while (sumZero>0):
      
      for i in range (0,4):
        #print "!!!!",sumZero
        tmp = random.randint(1,9)
        ZeroCount[i]=tmp
        sumZero-=tmp
      if(max-(2*sum(ZeroCount)) > 9 and (2*sumZero)+1 >= min):
        ZeroCount[4] = random.randint(1,9)
        sumZero-=ZeroCount[4]
    #print
    if((2*sum(ZeroCount)-2*ZeroCount[4])>min and (2*sum(ZeroCount)-2*ZeroCount[4])<max):
      return ZeroCount

printGrid(Grid)
print
 
  

def GenSudoku( inputGrid, lvl ):
  pair = [[0,0,6,6],[0,3,6,3],[0,6,6,0], [3,0,3,6]]
  ZeroCount = GenZeroCount(lvl)
  tmpGrid = inputGrid
  print ZeroCount, (2*sum(ZeroCount)-ZeroCount[4])
  for i in range(0,4):
    tmpZero=ZeroCount[i]
    while (tmpZero>0):
      row2 = pair[i][2]  
      for row in range(pair[i][0],pair[i][0]+3):
        cow2 = pair[i][3] 
        
        for cow in range(pair[i][1],pair[i][1]+3):
        #print row,cow,"\t",row2,cow2
          if(tmpZero == 0):
            break
          tmp = random.randint(0,1)
          if(tmp and inputGrid[row][cow]>0 and inputGrid[row2][cow2]>0):
            inputGrid[row][cow]=0
            inputGrid[row2][cow2]=0
            #print tmpZero
            tmpZero-=1
          cow2+=1
        row2+=1
  tmpZero=ZeroCount[4]
  while (tmpZero>0):
    for row in range(3,6):
      for cow in range(3,6):
        #print row,cow,"\t",row2,cow2
        if(tmpZero == 0):
          break
        tmp = random.randint(0,1)
        if(tmp and inputGrid[row][cow]>0 ):
          inputGrid[row][cow]=0
            #print tmpZero
          tmpZero-=1

  
GenSudoku(Grid, 1)

printGrid(Grid)
print

def readGrid():
  file = open("out.txt","r")
  lista = file.readlines()	 
  lista = lista[0:9]
  temp = [x.split() for x in lista]
  file.close()
  checkSum=0
  for i in range(0,9):
    for j in range(0,9):
      try: 
        tmpInt = int(temp[i][j])
        if(tmpInt>=0 and tmpInt<=9):
          temp[i][j]=tmpInt
          checkSum+=1
		
      except ValueError:
        return 1

  if(checkSum == 81):
    return temp
  else:
    return 1	  
  
  
#x =readGrid()
#if(x == 1):
#  print x
#else:
#  print readGrid()
  
def findNextCellToFill(grid, i, j):
  for x in range(i,9):
    for y in range(j,9):
      if grid[x][y] == 0:
        return x,y
  for x in range(0,9):
    for y in range(0,9):
      if grid[x][y] == 0:
        return x,y
  return -1,-1

def isValid(grid, i, j, e):
  rowOk = all([e != grid[i][x] for x in range(9)])
  if rowOk:
    columnOk = all([e != grid[x][j] for x in range(9)])
    if columnOk:
      # finding the top left x,y co-ordinates of the section containing the i,j cell
      secTopX, secTopY = 3 *(i/3), 3 *(j/3)
      for x in range(secTopX, secTopX+3):
        for y in range(secTopY, secTopY+3):
          if grid[x][y] == e:
            return False
      return True
  return False
  

def solveSudoku(grid, i=0, j=0):
  i,j = findNextCellToFill(grid, i, j)
  if i == -1:
    return True
  for e in range(1,10):
    if isValid(grid,i,j,e):
      grid[i][j] = e
      if solveSudoku(grid, i, j):
        return grid
      # Undo the current cell for backtracking
      grid[i][j] = 0
  return False
  
Grid =solveSudoku(Grid)
printGrid(Grid)
if(Colision()):
  print "Kolizja"
else:
  print "Brak kolizji" 
  
  
  ''' 

