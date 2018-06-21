import random
from SudokuSolver import solveSudoku

  
UserPromptCount = 3
PromptStatus = 0 #0 - Off, 1 - On

#When user input values to grid before thread finish then queue flag is set
QueueFlag = 0
#When thread finish solve grid and user doesn't input any new value to grid then CurrentSolvedGridFlag is set
CurrentSolvedGridFlag = 0
#Current Solved Grid
CurrentGrid = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],  [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]


#def Switch_Boxs(Box1, Box2):
#  Boxs=[[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
#  tmpBox2=Boxs[Box2][1]
#  for i in range(Boxs[Box1][0],Boxs[Box1][0]+3):
#    for j in range(Boxs[Box1][1],Boxs[Box1][1]+3):
#      Grid[i][j], Grid[Boxs[Box2][0]][Boxs[Box2][1]] = Grid[Boxs[Box2][0]][Boxs[Box2][1]], Grid[i][j]
#      #print i,j,Boxs[Box2][0],Boxs[Box2][1]      
#      Boxs[Box2][1]+=1
#
#      print '{:4}'.format(Grid[i][j]),
#    Boxs[Box2][1]=tmpBox2
#    Boxs[Box2][0]=(Boxs[Box2][0]+1)
#  print
  


def Switch_Cubes_x(tmpGrid, Cube1_x, Cube2_x):
  for i in range(0,9):
    tmpGrid[i][Cube1_x], Grid[i][Cube2_x] = Grid[i][Cube2_x], Grid[i][Cube1_x]
  return tmpGrid

def Switch_Cubes_y(tmpGrid, Cube1_y, Cube2_y):
  for i in range(0,9):
    tmpGrid[Cube1_y][i], Grid[Cube2_y][i] = Grid[Cube2_y][i], Grid[Cube1_y][i]  
  return tmpGrid
 
def Switch_Diagonal_Matrix(tmpGrid):
  tmpGrid = zip(tmpGrid[0], tmpGrid[1], tmpGrid[2], tmpGrid[3], tmpGrid[4], tmpGrid[5], tmpGrid[6], tmpGrid[7], tmpGrid[8])
  for i in range(0,9):
    for j in range(0,9):
      Grid[i][j]=tmpGrid[i][j]

def Switch_Diagonal_Revers_Matrix(tmpGrid):
  GridBC = tmpGrid
  tmpGrid.reverse()
  tmpGrid = zip(tmpGrid[0], tmpGrid[1], tmpGrid[2], tmpGrid[3], tmpGrid[4], tmpGrid[5], tmpGrid[6], tmpGrid[7], tmpGrid[8])
  tmpGrid.reverse()
  for i in range(0,9):
    for j in range(0,9):
      GridBC[i][j]=tmpGrid[i][j]
  return GridBC
  

  
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
        tmp[tmpGrid[i][j]]+=1	
    for i in range(1,10):
        if(tmp[i]>1):
          return 1
      
  
  return 0

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




  

def GenSudoku( inputGrid, lvl ):
  pair = [[0,0,6,6],[0,3,6,3],[0,6,6,0], [3,0,3,6]]
  ZeroCount = GenZeroCount(lvl)
  tmpGrid = inputGrid
  #print ZeroCount, (2*sum(ZeroCount)-ZeroCount[4])
  for i in range(0,4):
    tmpZero=ZeroCount[i]
    while (tmpZero>0):
      row2 = pair[i][2]  
      for row in range(pair[i][0],pair[i][0]+3):
        col2 = pair[i][3] 
        
        for col in range(pair[i][1],pair[i][1]+3):
        #print row,col,"\t",row2,col2
          if(tmpZero == 0):
            break
          tmp = random.randint(0,1)
          if(tmp and inputGrid[row][col]>0 and inputGrid[row2][col2]>0):
            inputGrid[row][col]=0
            inputGrid[row2][col2]=0
            #print tmpZero
            tmpZero-=1
          col2+=1
        row2+=1
  tmpZero=ZeroCount[4]
  while (tmpZero>0):
    for row in range(3,6):
      for col in range(3,6):
        #print row,col,"\t",row2,col2
        if(tmpZero == 0):
          break
        tmp = random.randint(0,1)
        if(tmp and inputGrid[row][col]>0 ):
          inputGrid[row][col]=0
            #print tmpZero
          tmpZero-=1
  return inputGrid




def readGrid(Fname):
  if(Fname[-4:]!='.txt'):
    tmpName= Fname+'.txt'
  else:
    tmpName= Fname
  file = open(tmpName,"r")
  lista = file.readlines()	 
  lista = lista[0:9]
  temp = [x.split() for x in lista]
  file.close()
  checkSum=0
  checkZeroSum = 0
  for i in range(0,9):
    for j in range(0,9):
      try: 
        tmpInt = int(temp[i][j])
        if(tmpInt>=0 and tmpInt<=9):
          temp[i][j]=tmpInt
          checkSum+=1
        if(temp[i][j] == 0):
          checkZeroSum+=1
      except ValueError:
        return 1
  if(checkZeroSum<14):
    print("Lamiesz zasady!")
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


def GenGrid(lv):

  FirstRandomNumbers=random.sample(range(1,10),9)
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
  #printGrid(Grid)
  Sudoku = GenSudoku(Grid, lv) 
  #print(UserPromptCount)
  global UserPromptCount
  #print(UserPromptCount)
  UserPromptCount = 3
  #print(UserPromptCount)
  global CurrentGrid
  CurrentGrid = Sudoku
  
  #print(CurrentGrid)

def CopyCurrentGrid():
  global CurrentGrid
  return CurrentGrid
 
def SaveToFile(GridToSave, Fname):
  if(Fname[-4:]!='.txt'):
    tmpName= Fname+'.txt'
  else:
    tmpName= Fname
  #file  = open(tmpName, 'w')
  with open(tmpName,"w") as file:
    try:
      for i in range(0,9):
        for j in range(0,9):
          z = str(GridToSave[i][j])
          file.write(z+' ')   
        #print("new line",i)
        file.write('\n')
    except:
      print("something go wrong")
	  
def WriteTempGame(Filename, GridGame, current=0):
  if(current):
    try:
      with open('CurrentGame.data','wb') as tempFile:
        for row in range(9):
          for col in range(9):
            tempFile.write(bytes((GridGame[row][col],)))
        tempFile.write(bytes((UserPromptCount,)))
      return
    except:
      return 1
  if(Filename[-5:]!='.data'):
    tmpName= Filename+'.data'
  else:
    tmpName= Filename
  try:
    with open(Filename,'wb') as tempFile:
       for row in range(9):
         for col in range(9):
           tempFile.write(bytes((GridGame[row][col],)))
       tempFile.write(bytes((UserPromptCount,)))
    
  except:
    return 1

	

def ResetGame(filename="", fromFile=0):
  global UserPromptCount
  temp = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
  if(fromFile):
    try:
      with open(filename,"rb") as f:
        for i in range(81):
          tmpRow = int(i/9)
          tmpNumber = f.read(1).hex()
          temp[tmpRow][(i%9)] = int(tmpNumber[1])
        UserPromptCount = int(f.read(82).hex()[1])
      if(Colision(temp)==0):
        return temp
      else:
        return 1
    except:
      return 1
  try:
    with open("CurrentGame.data","rb") as f:
      for i in range(81):
        tmpRow = int(i/9)
        tmpNumber = f.read(1).hex()
        temp[tmpRow][(i%9)] = int(tmpNumber[1], 16)
      UserPromptCount =int(f.read(82).hex()[1])
    if(Colision(temp)==0):
      return temp
    else:
      return 1
  except:
    return 1

def clearLineEdit(self):
  CurrentGrid = ResetGame()
  if(CurrentGrid == 1):
    return
  for i in range(1,82):
    if(CurrentGrid[int((i-1)/9)][int((i-1)%9)]==0):
      exec("self.lineEdit_"+str(i)+".setStyleSheet(\"background-color:white;color:black;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
  return
  

#Grid = GenGrid()
def WriteToCurrent(self):
  global UserPromptCount
  global PromptStatus
  curGrid = ResetGame()
  if(UserPromptCount < 1 or UserPromptCount > 3):
    return 0
  ################################
  solvedCurGrid = CopyGrid(curGrid)
  #################################
  LineEditNumber = int(self.objectName()[9:])
  solveSudoku(solvedCurGrid)
  curGrid[int((LineEditNumber-1)/9)][int((LineEditNumber-1)%9)] = solvedCurGrid[int((LineEditNumber-1)/9)][int((LineEditNumber-1)%9)]
  UserPromptCount-=1
  self.setText(str(curGrid[int((LineEditNumber-1)/9)][int((LineEditNumber-1)%9)]))
  self.setDisabled(True)
  self.setStyleSheet("background-color:#9b9b9b;color:white;font-family:Arial;font-size:15px;font-weight:bold;padding-left:7%;")

  try:
    with open('CurrentGame.data','wb') as tempFile:
      for row in range(9):
        for col in range(9):
          tempFile.write(bytes((curGrid[row][col],)))
      tempFile.write(bytes((UserPromptCount,)))
  except:
    return UserPromptCount
  return UserPromptCount	  

  
  

#print
#printGrid(Grid)
#print
def CopyGrid(Grid):
  tempGrid = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],  [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
  for row in range(9):
    for col in range(9):
      tempGrid[row][col]=Grid[row][col]
  return tempGrid
  
  
  


def ShowErrors(ValidGrid, OriginalGrid,self,C=1):
  if(Colision(ValidGrid)==0):
    C=0
    return 
  for row in range(9):
    for col in range(9):
      if(C):
        if(ValidGrid[row][col]!=OriginalGrid[row][col]):
          tmpGrid = CopyGrid(OriginalGrid)
          tmpGrid[row][col]=ValidGrid[row][col]   
          #Grid=	solveSudoku(tmpGrid)
          if(Colision(tmpGrid)):
            exec("self.lineEdit_"+str((((row%9)*9+(col%9))+1))+".setStyleSheet(\"background-color:red;color:black;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
          #  tmpGrid[row][col]=0
            ValidGrid[row][col]=0
          else:
            if(solveSudoku(tmpGrid)):
              tmpGrid = CopyGrid(OriginalGrid)
              tmpGrid[row][col]=ValidGrid[row][col]
              exec("self.lineEdit_"+str((((row%9)*9+(col%9))+1))+".setStyleSheet(\"background-color:white;color:black;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")	  
              ShowErrors(ValidGrid, tmpGrid, self)
      else:
        break



	


