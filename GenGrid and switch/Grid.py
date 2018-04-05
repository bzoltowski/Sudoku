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

#      print '{:4}'.format(Grid[i][j]),  dsa
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
  
  
  
def Colision(tmpGrid):
  
  for i in range(9):
    Test_x=[0,0,0,0,0,0,0,0,0,0,0]
    Test_y=[0,0,0,0,0,0,0,0,0,0,0]
    for j in range(9):
      Test_x[tmpGrid[i][j]]+=1
      Test_y[tmpGrid[j][i]]+=1
    for k in range(1,10):
      if(Test_x[k]>1 or Test_y[k]>1):
        return 1
  Boxs=[[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
  
  for k in range(9):
    tmp = [0,0,0,0,0,0,0,0,0,0]
    for i in range(Boxs[k][0],Boxs[k][0]+3):
      for j in range(Boxs[k][1],Boxs[k][1]+3):
        #print (i%3)*3+(j%3)
        #tmp[(i%3)*3+(j%3)+1]+=1
        #print tmpGrid[i][j]
        tmp[tmpGrid[i][j]]+=1		
    for i in range(1,10):
        print tmp
        if(tmp[i]>1):
          return 1
      
  
  return 0
   

#####################################
#	Prezentacja na pierwsza ocene	#
#####################################
print "Wygenerowana Tablica"
printGrid(Grid)

if(Colision(Grid)):
  print "Kolizja"
else:
  print "Brak kolizji"

Switch_Cubes_x(0,2)
print "Zamiana kolumn 1 oraz 3"
printGrid(Grid)

Switch_Cubes_y(0,8)
print "Zamiana wierszy 1 oraz 9"
printGrid(Grid)


Switch_Diagonal_Matrix()
print "Zamiana wzgledem przekatnej"
printGrid(Grid)

Switch_Diagonal_Revers_Matrix()

print "Zamiana wzgledem drugiej przekatnej"
printGrid(Grid)


