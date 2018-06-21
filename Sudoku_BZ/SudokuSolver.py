def findNextCell(tmpGrid, i, j):
  for x in range(i,9):
    for y in range(j,9):
      if tmpGrid[x][y] == 0:
        return x,y
  for x in range(0,9):
    for y in range(0,9):
      if tmpGrid[x][y] == 0:
        return x,y
  return -1,-1

def isValid(grid, i, j, e):
  rowOk = all([e != grid[i][x] for x in range(9)])
  if rowOk:
    columnOk = all([e != grid[x][j] for x in range(9)])
    if columnOk:
      # finding the top left x,y co-ordinates of the section containing the i,j cell
      secTopX, secTopY = 3 *int((i/3)), 3 *int((j/3))
      for x in range(secTopX, secTopX+3):
        for y in range(secTopY, secTopY+3):
          if grid[x][y] == e:
            return False
      return True
  return False
  

def solveSudoku(grid, i=0, j=0):
  i,j = findNextCell(grid, i, j)
  if i == -1:
    return True
  for e in range(1,10):
    if isValid(grid,i,j,e):
      grid[i][j] = e
      #print grid[i][j]
      if solveSudoku(grid, i, j):
        return grid
      # Undo the current cell for backtracking
      grid[i][j] = 0
  return False
#print
#printGrid(Grid)
#print