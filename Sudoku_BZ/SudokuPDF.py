from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from Grid import  CopyGrid, ResetGame
from SudokuSolver import solveSudoku
import os, subprocess
def GenPdf(UserSudoku):
  if(not os.path.exists("pdf")):
    os.makedirs("pdf")
  countOfPDFFiles=1
  for file in os.listdir("pdf"):
    if (file.endswith(".pdf") and file[:11]=="SudokuGame_"):
      countOfPDFFiles+=1
  FileName="pdf/SudokuGame_"+str(countOfPDFFiles)+".pdf"
  print(FileName)
  
  tmpGrid = CopyGrid(UserSudoku)
  SudokuSolved = solveSudoku(tmpGrid)
  
  if(SudokuSolved == False or SudokuSolved == True):
    print("Something go wrong with current game file:(\nTry again")
    return
  try:
    Game = canvas.Canvas(FileName, pagesize=letter)
    Game.drawString(210,750,'Plansza Sudoku - Bartek Zoltowski')
    
    Game.setLineWidth(2.5)       
    Game.line(165,725,435,725)
    Game.setLineWidth(1)
    Game.line(165,695,435,695)
    Game.line(165,665,435,665)
    Game.setLineWidth(2.5)
    Game.line(165,635,435,635)
    Game.setLineWidth(1)
    Game.line(165,605,435,605)
    Game.line(165,575,435,575)
    Game.setLineWidth(2.5)
    Game.line(165,545,435,545)
    Game.setLineWidth(1)
    Game.line(165,515,435,515)
    Game.line(165,485,435,485)
    Game.setLineWidth(2.5)
    Game.line(165,455,435,455)
    
    Game.line(165,725,165,455)
    Game.setLineWidth(1)
    Game.line(195,725,195,455)
    Game.line(225,725,225,455)
    Game.setLineWidth(2.5)
    Game.line(255,725,255,455)
    Game.setLineWidth(1)
    Game.line(285,725,285,455)
    Game.line(315,725,315,455)
    Game.setLineWidth(2.5)
    Game.line(345,725,345,455)
    Game.setLineWidth(1)
    Game.line(375,725,375,455)
    Game.line(405,725,405,455)
    Game.setLineWidth(2.5)
    Game.line(435,725,435,455)
    
    Game.drawString(265,400,'Rozwiazanie')
    
    Game.setLineWidth(2.5)       
    Game.line(165,375,435,375)
    Game.setLineWidth(1)
    Game.line(165,345,435,345)
    Game.line(165,315,435,315)
    Game.setLineWidth(2.5)
    Game.line(165,285,435,285)
    Game.setLineWidth(1)
    Game.line(165,255,435,255)
    Game.line(165,225,435,225)
    Game.setLineWidth(2.5)
    Game.line(165,195,435,195)
    Game.setLineWidth(1)
    Game.line(165,165,435,165)
    Game.line(165,135,435,135)
    Game.setLineWidth(2.5)
    Game.line(165,105,435,105)
    
    Game.line(165,375,165,105)
    Game.setLineWidth(1)
    Game.line(195,375,195,105)
    Game.line(225,375,225,105)
    Game.setLineWidth(2.5)
    Game.line(255,375,255,105)
    Game.setLineWidth(1)
    Game.line(285,375,285,105)
    Game.line(315,375,315,105)
    Game.setLineWidth(2.5)
    Game.line(345,375,345,105)
    Game.setLineWidth(1)
    Game.line(375,375,375,105)
    Game.line(405,375,405,105)
    Game.setLineWidth(2.5)
    Game.line(435,375,435,105)
    
    
    Sudoku_y=705
    SudokuSolved_y=355
    for i in range(9):
      Sudoku_x=177
      SudokuSolved_x=177
      for j in range(9):
        if(UserSudoku[i][j]!=0):
          Game.drawString(Sudoku_x,Sudoku_y,str(UserSudoku[i][j]))
        Game.drawString(SudokuSolved_x,SudokuSolved_y,str(SudokuSolved[i][j]))
        Sudoku_x+=30
        SudokuSolved_x+=30
      Sudoku_y-=30
      SudokuSolved_y-=30
    
    
    Game.save()

  except:
    print("Something go wrong :(\nTry again")
    return
  try:
    subprocess.Popen(["xdg-open", FileName])
  except:
    return