from SudokuPDF import GenPdf
from Grid import ShowErrors, GenGrid
import threading
#######################################################
                      # THREADS #
#######################################################
class SudokuThreads (threading.Thread):
    def __init__(selfThread, threadID, Sudoku = 0, Original = 0, self=0):
        threading.Thread.__init__(selfThread)
        selfThread.threadID = threadID
        selfThread.arg1 = Sudoku
        selfThread.arg2 = Original
        selfThread.arg3 = self
        #print(Sudoku)
    def run(selfThread):
        if(selfThread.threadID == 0):#Print
            GenPdf(selfThread.arg1)
        if(selfThread.threadID == 1):
            ShowErrors(selfThread.arg1,selfThread.arg2, selfThread.arg3)
        if(selfThread.threadID == 2):
            GenGrid(selfThread.arg1)

#######################################################
                      # !THREADS #
#######################################################
