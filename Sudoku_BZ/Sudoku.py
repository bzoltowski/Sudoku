# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sudoku.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal, QEvent
from PyQt5.QtWidgets import QApplication, QMessageBox, QAction, QFileDialog, QLineEdit
from Grid import *
from SudokuThreads import SudokuThreads
import threading
import sys
import os

OwnGameFlag = 0
ColorTop = [240,240,240]
ColorBottom = [240,160,160]


Sudoku = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]


	
def ChangeBackground(self, Form, ColorGradientTop, ColorGradientBottom):
    #Form = QtWidgets.QWidget()
    p = QPalette()
    gradient = QLinearGradient(0,0,0,400)
    gradient.setColorAt(0.0, QColor(ColorGradientTop[0], ColorGradientTop[1], ColorGradientTop[2]))
    gradient.setColorAt(1.0, QColor(ColorGradientBottom[0], ColorGradientBottom[1], ColorGradientBottom[2]))
    p.setBrush(QPalette.Window, QBrush(gradient))
    Form.setPalette(p)
	
class extQLineEdit(QLineEdit):
    clicked= pyqtSignal()
    def __init__(self,widget):
        super().__init__(widget)
    def mousePressEvent(self,QMouseEvent):
        if (PromptStatus):
            tmpUserPromptCount = WriteToCurrent(self)
            if (tmpUserPromptCount==0):
                Form1 = QtWidgets.QWidget()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.question(Form1, "Information", "Nie możesz już używać podpowiedzi dla tej rozgrywki :(",msg.NoButton)
                return
            else:
                Form1 = QtWidgets.QWidget()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.question(Form1, "Information", "Pozostały Ci "+str(tmpUserPromptCount)+" podpowiedzi do wykorzystania w tej rozgrywce.",msg.NoButton)
        self.clicked.emit()
'''    ShiftKey=0
    def event(self, event):
        if (event.type()==QEvent.KeyPress):
            if(event.key()==QtCore.Qt.Key_Shift):
                return True
            if(event.key()==QtCore.Qt.Key_Tab) or QKeySequence(QtCore.Qt.ShiftModifier and QtCore.Qt.Key_Tab):
                self.clicked.emit()
        return QLineEdit.event(self, event)
	'''	
class Ui_Form(object):
		
    def setupUi(self, Form):
        Form.setObjectName("Sudoku - Bartek Żółtowski")
        Form.setEnabled(True)
        Form.resize(500, 370)
        #msgbox(self, Form)
        ChangeBackground(self, Form, ColorTop, ColorBottom)
        self.onlyInt = QIntValidator(0, 9)
        self.Sudoku_Vertical_1 = QtWidgets.QGraphicsView(Form)
        self.Sudoku_Vertical_1.setGeometry(QtCore.QRect(115, 68, 7, 272))
        self.Sudoku_Vertical_1.setObjectName("Sudoku_Vertical_1")
        self.Sudoku_Vertical_1.setStyleSheet("background-color:#9b9b9b;")
        self.Sudoku_Vertical_2 = QtWidgets.QGraphicsView(Form)
        self.Sudoku_Vertical_2.setGeometry(QtCore.QRect(227, 68, 7, 272))
        self.Sudoku_Vertical_2.setObjectName("Sudoku_Vertical_2")
        self.Sudoku_Vertical_2.setStyleSheet("background-color:#9b9b9b;")
        self.Sudoku_Horizontal_1 = QtWidgets.QGraphicsView(Form)
        self.Sudoku_Horizontal_1.setGeometry(QtCore.QRect(10, 153, 330, 8))
        self.Sudoku_Horizontal_1.setObjectName("Sudoku_Horizontal_1")
        self.Sudoku_Horizontal_1.setStyleSheet("background-color:#9b9b9b;")
        self.Sudoku_Horizontal_2 = QtWidgets.QGraphicsView(Form)
        self.Sudoku_Horizontal_2.setGeometry(QtCore.QRect(10, 248, 330, 8))
        self.Sudoku_Horizontal_2.setObjectName("Sudoku_Horizontal_2")
        self.Sudoku_Horizontal_2.setStyleSheet("background-color:#9b9b9b;")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 40, 350, 325))
        self.widget.setObjectName("widget")
        #self.widget.setStyleSheet("background-color:red;opacity:.1;")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_1 = extQLineEdit(Form)
        self.lineEdit_1.setObjectName("lineEdit_1")  
        #self.lineEdit_1.setMaxLength(1)
        self.horizontalLayout.addWidget(self.lineEdit_1)
        self.lineEdit_2 = extQLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = extQLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = extQLineEdit(Form)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_5 = extQLineEdit(Form)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_6 = extQLineEdit(Form)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout.addWidget(self.lineEdit_6)
        self.lineEdit_7 = extQLineEdit(Form)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout.addWidget(self.lineEdit_7)
        self.lineEdit_8 = extQLineEdit(Form)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout.addWidget(self.lineEdit_8)
        self.lineEdit_9 = extQLineEdit(Form)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout.addWidget(self.lineEdit_9)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 2, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_10 = extQLineEdit(Form)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_2.addWidget(self.lineEdit_10)
        self.lineEdit_11 = extQLineEdit(Form)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_2.addWidget(self.lineEdit_11)
        self.lineEdit_12 = extQLineEdit(Form)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_2.addWidget(self.lineEdit_12)
        self.lineEdit_13 = extQLineEdit(Form)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_2.addWidget(self.lineEdit_13)
        self.lineEdit_14 = extQLineEdit(Form)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_2.addWidget(self.lineEdit_14)
        self.lineEdit_15 = extQLineEdit(Form)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.horizontalLayout_2.addWidget(self.lineEdit_15)
        self.lineEdit_16 = extQLineEdit(Form)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.horizontalLayout_2.addWidget(self.lineEdit_16)
        self.lineEdit_17 = extQLineEdit(Form)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.horizontalLayout_2.addWidget(self.lineEdit_17)
        self.lineEdit_18 = extQLineEdit(Form)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.horizontalLayout_2.addWidget(self.lineEdit_18)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 2, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_19 = extQLineEdit(Form)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.horizontalLayout_3.addWidget(self.lineEdit_19)
        self.lineEdit_20 = extQLineEdit(Form)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.horizontalLayout_3.addWidget(self.lineEdit_20)
        self.lineEdit_21 = extQLineEdit(Form)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.horizontalLayout_3.addWidget(self.lineEdit_21)
        self.lineEdit_22 = extQLineEdit(Form)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.horizontalLayout_3.addWidget(self.lineEdit_22)
        self.lineEdit_23 = extQLineEdit(Form)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.horizontalLayout_3.addWidget(self.lineEdit_23)
        self.lineEdit_24 = extQLineEdit(Form)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.horizontalLayout_3.addWidget(self.lineEdit_24)
        self.lineEdit_25 = extQLineEdit(Form)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.horizontalLayout_3.addWidget(self.lineEdit_25)
        self.lineEdit_26 = extQLineEdit(Form)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.horizontalLayout_3.addWidget(self.lineEdit_26)
        self.lineEdit_27 = extQLineEdit(Form)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.horizontalLayout_3.addWidget(self.lineEdit_27)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 2, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_28 = extQLineEdit(Form)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.horizontalLayout_4.addWidget(self.lineEdit_28)
        self.lineEdit_29 = extQLineEdit(Form)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.horizontalLayout_4.addWidget(self.lineEdit_29)
        self.lineEdit_30 = extQLineEdit(Form)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.horizontalLayout_4.addWidget(self.lineEdit_30)
        self.lineEdit_31 = extQLineEdit(Form)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.horizontalLayout_4.addWidget(self.lineEdit_31)
        self.lineEdit_32 = extQLineEdit(Form)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.horizontalLayout_4.addWidget(self.lineEdit_32)
        self.lineEdit_33 = extQLineEdit(Form)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.horizontalLayout_4.addWidget(self.lineEdit_33)
        self.lineEdit_34 = extQLineEdit(Form)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.horizontalLayout_4.addWidget(self.lineEdit_34)
        self.lineEdit_35 = extQLineEdit(Form)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.horizontalLayout_4.addWidget(self.lineEdit_35)
        self.lineEdit_36 = extQLineEdit(Form)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.horizontalLayout_4.addWidget(self.lineEdit_36)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 2, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_37 = extQLineEdit(Form)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.horizontalLayout_5.addWidget(self.lineEdit_37)
        self.lineEdit_38 = extQLineEdit(Form)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.horizontalLayout_5.addWidget(self.lineEdit_38)
        self.lineEdit_39 = extQLineEdit(Form)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.horizontalLayout_5.addWidget(self.lineEdit_39)
        self.lineEdit_40 = extQLineEdit(Form)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.horizontalLayout_5.addWidget(self.lineEdit_40)
        self.lineEdit_41 = extQLineEdit(Form)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.horizontalLayout_5.addWidget(self.lineEdit_41)
        self.lineEdit_42 = extQLineEdit(Form)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.horizontalLayout_5.addWidget(self.lineEdit_42)
        self.lineEdit_43 = extQLineEdit(Form)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.horizontalLayout_5.addWidget(self.lineEdit_43)
        self.lineEdit_44 = extQLineEdit(Form)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.horizontalLayout_5.addWidget(self.lineEdit_44)
        self.lineEdit_45 = extQLineEdit(Form)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.horizontalLayout_5.addWidget(self.lineEdit_45)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 2, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_46 = extQLineEdit(Form)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.horizontalLayout_6.addWidget(self.lineEdit_46)
        self.lineEdit_47 = extQLineEdit(Form)
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.horizontalLayout_6.addWidget(self.lineEdit_47)
        self.lineEdit_48 = extQLineEdit(Form)
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.horizontalLayout_6.addWidget(self.lineEdit_48)
        self.lineEdit_49 = extQLineEdit(Form)
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.horizontalLayout_6.addWidget(self.lineEdit_49)
        self.lineEdit_50 = extQLineEdit(Form)
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.horizontalLayout_6.addWidget(self.lineEdit_50)
        self.lineEdit_51 = extQLineEdit(Form)
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.horizontalLayout_6.addWidget(self.lineEdit_51)
        self.lineEdit_52 = extQLineEdit(Form)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.horizontalLayout_6.addWidget(self.lineEdit_52)
        self.lineEdit_53 = extQLineEdit(Form)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.horizontalLayout_6.addWidget(self.lineEdit_53)
        self.lineEdit_54 = extQLineEdit(Form)
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.horizontalLayout_6.addWidget(self.lineEdit_54)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 2, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_55 = extQLineEdit(Form)
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.horizontalLayout_7.addWidget(self.lineEdit_55)
        self.lineEdit_56 = extQLineEdit(Form)
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.horizontalLayout_7.addWidget(self.lineEdit_56)
        self.lineEdit_57 = extQLineEdit(Form)
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.horizontalLayout_7.addWidget(self.lineEdit_57)
        self.lineEdit_58 = extQLineEdit(Form)
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.horizontalLayout_7.addWidget(self.lineEdit_58)
        self.lineEdit_59 = extQLineEdit(Form)
        self.lineEdit_59.setObjectName("lineEdit_59")
        self.horizontalLayout_7.addWidget(self.lineEdit_59)
        self.lineEdit_60 = extQLineEdit(Form)
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.horizontalLayout_7.addWidget(self.lineEdit_60)
        self.lineEdit_61 = extQLineEdit(Form)
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.horizontalLayout_7.addWidget(self.lineEdit_61)
        self.lineEdit_62 = extQLineEdit(Form)
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.horizontalLayout_7.addWidget(self.lineEdit_62)
        self.lineEdit_63 = extQLineEdit(Form)
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.horizontalLayout_7.addWidget(self.lineEdit_63)
        self.gridLayout.addLayout(self.horizontalLayout_7, 6, 0, 2, 2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_64 = extQLineEdit(Form)
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.horizontalLayout_8.addWidget(self.lineEdit_64)
        self.lineEdit_65 = extQLineEdit(Form)
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.horizontalLayout_8.addWidget(self.lineEdit_65)
        self.lineEdit_66 = extQLineEdit(Form)
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.horizontalLayout_8.addWidget(self.lineEdit_66)
        self.lineEdit_67 = extQLineEdit(Form)
        self.lineEdit_67.setObjectName("lineEdit_67")
        self.horizontalLayout_8.addWidget(self.lineEdit_67)
        self.lineEdit_68 = extQLineEdit(Form)
        self.lineEdit_68.setObjectName("lineEdit_68")
        self.horizontalLayout_8.addWidget(self.lineEdit_68)
        self.lineEdit_69 = extQLineEdit(Form)
        self.lineEdit_69.setObjectName("lineEdit_69")
        self.horizontalLayout_8.addWidget(self.lineEdit_69)
        self.lineEdit_70 = extQLineEdit(Form)
        self.lineEdit_70.setObjectName("lineEdit_70")
        self.horizontalLayout_8.addWidget(self.lineEdit_70)
        self.lineEdit_71 = extQLineEdit(Form)
        self.lineEdit_71.setObjectName("lineEdit_71")
        self.horizontalLayout_8.addWidget(self.lineEdit_71)
        self.lineEdit_72 = extQLineEdit(Form)
        self.lineEdit_72.setObjectName("lineEdit_72")
        self.horizontalLayout_8.addWidget(self.lineEdit_72)
        self.gridLayout.addLayout(self.horizontalLayout_8, 7, 0, 2, 2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_73 = extQLineEdit(Form)
        self.lineEdit_73.setObjectName("lineEdit_73")
        self.horizontalLayout_9.addWidget(self.lineEdit_73)
        self.lineEdit_74 = extQLineEdit(Form)
        self.lineEdit_74.setObjectName("lineEdit_74")
        self.horizontalLayout_9.addWidget(self.lineEdit_74)
        self.lineEdit_75 = extQLineEdit(Form)
        self.lineEdit_75.setObjectName("lineEdit_75")
        self.horizontalLayout_9.addWidget(self.lineEdit_75)
        self.lineEdit_76 = extQLineEdit(Form)
        self.lineEdit_76.setObjectName("lineEdit_76")
        self.horizontalLayout_9.addWidget(self.lineEdit_76)
        self.lineEdit_77 = extQLineEdit(Form)
        self.lineEdit_77.setObjectName("lineEdit_77")
        self.horizontalLayout_9.addWidget(self.lineEdit_77)
        self.lineEdit_78 = extQLineEdit(Form)
        self.lineEdit_78.setObjectName("lineEdit_78")
        self.horizontalLayout_9.addWidget(self.lineEdit_78)
        self.lineEdit_79 = extQLineEdit(Form)
        self.lineEdit_79.setObjectName("lineEdit_79")
        self.horizontalLayout_9.addWidget(self.lineEdit_79)
        self.lineEdit_80 = extQLineEdit(Form)
        self.lineEdit_80.setObjectName("lineEdit_80")
        self.horizontalLayout_9.addWidget(self.lineEdit_80)
        self.lineEdit_81 = extQLineEdit(Form)
        self.lineEdit_81.setObjectName("lineEdit_81")
        #self.lineEdit_81.insertPlainText("x")
        self.lineEdit_81.clear()
        self.horizontalLayout_9.addWidget(self.lineEdit_81)
        self.gridLayout.addLayout(self.horizontalLayout_9, 8, 0, 2, 2)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(340, 40, 150, 220))
        self.widget1.setObjectName("widget1")
        self.Game_Layout = QtWidgets.QVBoxLayout(self.widget1)
        self.Game_Layout.setObjectName("Game_Layout")
        self.NewBtn = QtWidgets.QPushButton(self.widget1)
        self.NewBtn.setEnabled(True)
        self.NewBtn.setObjectName("NewBtn")
        self.Game_Layout.addWidget(self.NewBtn)
        self.EasyRadioBtn = QtWidgets.QRadioButton(self.widget1)
        self.EasyRadioBtn.setObjectName("EasyRadioBtn")
        self.EasyRadioBtn.setChecked(True)
        self.Game_Layout.addWidget(self.EasyRadioBtn)
        self.AverageRadioBtn = QtWidgets.QRadioButton(self.widget1)
        self.AverageRadioBtn.setObjectName("AverageRadioBtn")
        self.Game_Layout.addWidget(self.AverageRadioBtn)
        self.HardRadioBtn = QtWidgets.QRadioButton(self.widget1)
        self.HardRadioBtn.setObjectName("HardRadioBtn")
        self.Game_Layout.addWidget(self.HardRadioBtn)
        self.PromptBtn = QtWidgets.QPushButton(self.widget1)
        self.PromptBtn.setObjectName("PromptBtn")
        self.Game_Layout.addWidget(self.PromptBtn)
        self.ShowErrorBtn = QtWidgets.QPushButton(self.widget1)
        self.ShowErrorBtn.setObjectName("ShowErrorBtn")
        self.Game_Layout.addWidget(self.ShowErrorBtn)
        self.SolveBtn = QtWidgets.QPushButton(self.widget1)
        self.SolveBtn.setAutoDefault(False)
        self.SolveBtn.setDefault(False)
        self.SolveBtn.setFlat(False)
        self.SolveBtn.setObjectName("SolveBtn")
        self.Game_Layout.addWidget(self.SolveBtn)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(10, 0, 480, 50))
        self.widget2.setObjectName("widget2")
        self.Menu_Layout = QtWidgets.QHBoxLayout(self.widget2)
        self.Menu_Layout.setObjectName("Menu_Layout")
        self.PrintBtn = QtWidgets.QPushButton(self.widget2)
        self.PrintBtn.setObjectName("PrintBtn")
        self.Menu_Layout.addWidget(self.PrintBtn)
        self.SaveBtn = QtWidgets.QPushButton(self.widget2)
        self.SaveBtn.setObjectName("SaveBtn")
        self.Menu_Layout.addWidget(self.SaveBtn)
        self.ReadBtn = QtWidgets.QPushButton(self.widget2)
        self.ReadBtn.setObjectName("ReadBtn")
        self.Menu_Layout.addWidget(self.ReadBtn)
        self.ResetBtn = QtWidgets.QPushButton(self.widget2)
        self.ResetBtn.setObjectName("ResetBtn")
        self.Menu_Layout.addWidget(self.ResetBtn)
        self.MakeOwnBtn = QtWidgets.QPushButton(self.widget2)
        self.MakeOwnBtn.setObjectName("MakeOwnBtn")
        self.Menu_Layout.addWidget(self.MakeOwnBtn)
        self.lineEdit_1.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_2.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_3.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_4.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_5.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_6.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_7.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_8.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_9.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_10.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_11.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_12.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_13.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_14.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_15.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_16.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_17.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_18.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_19.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_20.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_21.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_22.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_23.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_24.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_25.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_26.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_27.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_28.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_29.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_30.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_31.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_32.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_33.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_34.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_35.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_36.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_37.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_38.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_39.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_40.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_41.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_42.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_43.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_44.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_45.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_46.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_47.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_48.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_49.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_50.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_51.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_52.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_53.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_54.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_55.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_56.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_57.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_58.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_59.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_60.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_61.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_62.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_63.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_64.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_65.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_66.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_67.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_68.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_69.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_70.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_71.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_72.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_73.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_74.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_75.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_76.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_77.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_78.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_79.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_80.clicked.connect(lambda:clearLineEdit(self))
        self.lineEdit_81.clicked.connect(lambda:clearLineEdit(self))


        #self.lineEdit_1.clicked.connect(lambda:self.mouseMoveEvent(self))
        for i in range(1,82):
            exec("self.lineEdit_"+str(i)+".clear()")
            exec("self.lineEdit_"+str(i)+".setValidator(self.onlyInt)")
            exec("self.lineEdit_"+str(i)+".setDisabled(False)")
            #exec("self.lineEdit_"+str(i)+".selectAll()")
            exec("self.lineEdit_"+str(i)+".setMaxLength(1)")
            exec("self.lineEdit_"+str(i)+".setStyleSheet(\"background-color:white;color:black;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
            #exec("self.lineEdit_"+str(i)+".clicked.connect(lambda:clearLineEdit(self))")
        self.MakeSudoku(self)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)
        self.PromptBtn.clicked.connect(lambda:self.setPrompt(self))#lambda:self.setPrompt(self)
        self.SaveBtn.clicked.connect(lambda:self.file_save(Form))
        self.PrintBtn.clicked.connect(lambda:self.PrintSudoku(Form))
        self.ReadBtn.clicked.connect(lambda:self.file_open(Form))
        self.SolveBtn.clicked.connect(lambda:self.SolveCheck(self))
        self.ResetBtn.clicked.connect(lambda:self.Reset(self))#lambda:self.Reset(self)
        self.NewBtn.clicked.connect(lambda:self.MakeSudoku(self))
        self.ShowErrorBtn.clicked.connect(lambda:self.SError(self))
        self.MakeOwnBtn.clicked.connect(lambda:self.OwnGame(self))
			
			
    def OwnGame(self, From):
        self.CloseEvent(self)
        OwnGameFlag = 1
        for i in range(1,82):
            exec("self.lineEdit_"+str(i)+".clear()")
            exec("self.lineEdit_"+str(i)+".setDisabled(False)")
            exec("self.lineEdit_"+str(i)+".setStyleSheet(\"background-color:white;color:black;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
        
        ColorTop=[240,240,240]
        ColorBottom=[255,165,0]
        ChangeBackground(self, Form, ColorTop, ColorBottom)
        Sudoku = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],  [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        WriteTempGame("", Sudoku, 1)
        self.PromptBtn.setDisabled(True)
			
    def PrintSudoku(self, Form):
        UserSudoku =[[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],  [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        for i in range(1,82):
            tmpStrVal = eval("self.lineEdit_"+str(i)+".text()")
            if(len(tmpStrVal)==0):
                tmpStrVal=0
            tmpIntVal = int(tmpStrVal)    
            j = i-1
            tmprow = int(j/9)
            UserSudoku[tmprow][(j%9)]=tmpIntVal
        if(Colision(UserSudoku)==1):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.question(Form, "Warning", "W Twoim sudoku wystąpiła kolizja, usun ja aby kontynuowac.",msg.Ok)
            return			
        SudokuThreads(0, UserSudoku).start()
        

    def setPrompt(self, Form):
	
        global PromptStatus
        CurGrid = ResetGame()
        if(CurGrid==1):
            return
        if(PromptStatus == 1):
            self.SaveBtn.setDisabled(False)
            self.MakeOwnBtn.setDisabled(False)
            self.PrintBtn.setDisabled(False)
            self.ReadBtn.setDisabled(False)
            self.SolveBtn.setDisabled(False)
            self.ResetBtn.setDisabled(False)
            self.NewBtn.setDisabled(False)
            self.ShowErrorBtn.setDisabled(False)
            self.PromptBtn.setText("Podpowiedzi")
            for i in range(1,82):
                    if(CurGrid[int((i-1)/9)][int((i-1)%9)]==0):
                        exec("self.lineEdit_"+str(i)+".setStyleSheet(\"background-color:white;color:black;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
            PromptStatus = 0 
            return
        global UserPromptCount
        try:
            with open("CurrentGame.data","rb") as f:
                UserPromptCount = int(f.read(82).hex()[163])
        except:
            UserPromptCount = 3

        if(UserPromptCount < 0 or UserPromptCount > 3):
            return
        if(UserPromptCount == 0):
            Form1 = QtWidgets.QWidget()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.question(Form1, "Information", "Nie możesz już używać podpowiedzi dla tej rozgrywki :(",msg.NoButton)
            return
        
        
        for i in range(1,82):
            if(CurGrid[int((i-1)/9)][int((i-1)%9)]==0):
                exec("self.lineEdit_"+str(i)+".setStyleSheet(\"background-color:#99ff00;color:black;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
        PromptStatus = 1
        self.SaveBtn.setDisabled(True)
        self.MakeOwnBtn.setDisabled(True)
        self.PrintBtn.setDisabled(True)
        self.ReadBtn.setDisabled(True)
        self.SolveBtn.setDisabled(True)
        self.ResetBtn.setDisabled(True)
        self.NewBtn.setDisabled(True)
        self.ShowErrorBtn.setDisabled(True)
        self.PromptBtn.setText("Wył. Podpowiedzi")
		

		
    def file_save(self, Form):
        name, _ = QFileDialog.getSaveFileName(Form, "Save Game", 'saved_games', "Game (*.txt)", options=QFileDialog.DontUseNativeDialog)
        if(len(name)==0):
            return
        tmpGrid =[[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],  [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        for i in range(1,82):
            tmpStrVal = eval("self.lineEdit_"+str(i)+".text()")
            if(len(tmpStrVal)==0):
                tmpStrVal=0
            tmpIntVal = int(tmpStrVal)    
            j = i-1
            tmprow = int(j/9)
            tmpGrid[tmprow][(j%9)]=tmpIntVal
        SaveToFile(tmpGrid, name)
        if(name[-4:]=='.txt'):
          name = name[:-4]
        if(name[-5:]!='.data'):
          tmpName= name+'.data'
        else:
          tmpName= name
        import shutil
        shutil.copy2("CurrentGame.data",tmpName) 
		
    def file_open(self, Form):
        global UserPromptCount
        name, _ = QFileDialog.getOpenFileName(Form, "Save Game", 'saved_games', "Game (*.txt)", options=QFileDialog.DontUseNativeDialog)
        if(len(name)==0):
            return
        tmpDataName = str(name[:-3])+"data"
        Sudoku =readGrid(name)
        if(Sudoku==1 or Colision(Sudoku)==1):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.question(Form, "Warning", "Something go wrong with your game file :(\nTry again.",msg.Ok)
            return
        tmp = 1
        if(os.path.isfile(tmpDataName)):
            tmpGrid = ResetGame(tmpDataName,1)
            if(tmpGrid == 1):
                print("Something go wrong with your save file:(\nTry again")
            else:
                
                WriteTempGame("",tmpGrid,1)
                for row in range(0,9):
                    for cow in range(0,9):
                        tmp+=1
                        exec("self.lineEdit_"+str(tmp-1)+".clear()")
                        exec("self.lineEdit_"+str(tmp-1)+".setDisabled(False)")
                        exec("self.lineEdit_"+str(tmp-1)+".setStyleSheet(\"background-color:white;color:black;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
                        if(tmpGrid[row][cow]==0 and Sudoku[row][cow]!=0):
                            exec("self.lineEdit_"+str(tmp-1)+".setText(\'"+str(Sudoku[row][cow])+"\')")
                        if(tmpGrid[row][cow]!=0):            
                            exec("self.lineEdit_"+str(tmp-1)+".setText(\'"+str(tmpGrid[row][cow])+"\')")
                            exec("self.lineEdit_"+str(tmp-1)+".setDisabled(True)")
                            exec("self.lineEdit_"+str(tmp-1)+".setStyleSheet(\"background-color:#9b9b9b;color:white;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
                
                        else:
                            continue		
                return
        WriteTempGame("",Sudoku,1)
        for row in range(0,9):
            for cow in range(0,9):
                tmp+=1
                exec("self.lineEdit_"+str(tmp-1)+".clear()")
                exec("self.lineEdit_"+str(tmp-1)+".setDisabled(False)")
                exec("self.lineEdit_"+str(tmp-1)+".setStyleSheet(\"background-color:white;color:black;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
                if(Sudoku[row][cow]!=0):            
                    exec("self.lineEdit_"+str(tmp-1)+".setText(\'"+str(Sudoku[row][cow])+"\')")
                    exec("self.lineEdit_"+str(tmp-1)+".setDisabled(True)")
                    exec("self.lineEdit_"+str(tmp-1)+".setStyleSheet(\"background-color:#9b9b9b;color:white;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
        
                else:
                    continue  
        return

		
    def SError(self, b):
        Solved =[[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],  [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        OriginalGrid = ResetGame("")
        if(OriginalGrid == 1):
            print("Something go wrong:(\nTry again")
            return
        for i in range(1,82):
            tmpStrVal = eval("b.lineEdit_"+str(i)+".text()")
            if(len(tmpStrVal)==0):
                tmpStrVal=0
            tmpIntVal = int(tmpStrVal)    
            j = i-1
            tmprow = int(j/9)
            Solved[tmprow][(j%9)]=tmpIntVal
        for i in range(1,82):
            if(Solved[int((i-1)/9)][int((i-1)%9)]!=OriginalGrid[int((i-1)/9)][int((i-1)%9)]):
                exec("self.lineEdit_"+str(i)+".setStyleSheet(\"background-color:white;color:black;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
        if(Colision(Solved)==0):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.question(Form, "Information", "Nie znaleziono błedów ;)",msg.NoButton)
            return
        #SudokuThreads(1, Solved, OriginalGrid, self).start()
        ShowErrors(Solved,OriginalGrid, self)
        
			
			
    def CloseEvent(self, Form, CloseOption=1):#CloseOption: 1 - Current Game, 0 - Window
        Sudoku = ResetGame("")
        if(Sudoku == 1):
            return
        #print(Sudoku)
        for i in range(1,82):
            tmpStrVal = eval("self.lineEdit_"+str(i)+".text()")
            if(len(tmpStrVal)!=0 and Sudoku[int((i-1)/9)][int((i-1)%9)]==0):
                Form = QtWidgets.QWidget()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Question)
                answer = msg.question(Form, "Exit Event", "Are you sure you want to exit without saving?",msg.Save | msg.Discard)
                if(CloseOption):
                    if(answer == msg.Save):
                        self.file_save(Form)
                        os.remove("CurrentGame.data")
                        self.MakeSudoku(self)
                        break
                    if(answer == msg.Discard):
                        os.remove("CurrentGame.data")
                        self.MakeSudoku(self)
                        break
                else:
                    if(answer == msg.Save):
                        self.file_save(Form)
                        sys.exit()
                    if(answer == msg.Discard):
                        sys.exit()
                break
        os.remove("CurrentGame.data")
        return
	
	
    def SolveCheck(self, b):
        UserSudoku =[[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],  [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        checkSum=0
        for i in range(1,82):
            tmpStrVal = eval("b.lineEdit_"+str(i)+".text()")
            if(len(tmpStrVal)==0):
                tmpStrVal=0
                checkSum+=1
            tmpIntVal = int(tmpStrVal)
            if (tmpIntVal < 0 or tmpIntVal > 9):
                return 1
            else:
                j = i-1
                tmprow = int(j/9)
                UserSudoku[tmprow][(j%9)]=tmpIntVal
        if(checkSum==0 and Colision(UserSudoku)==0):
            print ("Good Job u solve this Sudoku")
            return
        else:
            print ("Almost, keep going ;)")
            return
        
            



    def Reset(self,b):
        for i in range(1,82):
            exec("b.lineEdit_"+str(i)+".clear()")
            exec("b.lineEdit_"+str(i)+".setDisabled(False)")
            exec("b.lineEdit_"+str(i)+".setStyleSheet(\"background-color:white;color:black;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
        Sudoku = ResetGame("")
        if(Sudoku == 1):
            print("Something go wrong:(\nTry again")
            return
        #print (Sudoku)
        for i in range(1,82):
            exec("b.lineEdit_"+str(i)+".clear()")
            #exec("b.lineEdit_"+str(i)+".setStyleSheet(\"background-color:white;color:black;\")")
        tmp = 1
        for row in range(0,9):
            for cow in range(0,9):
                tmp+=1
                if(Sudoku[row][cow]!=0):
                    exec("b.lineEdit_"+str(tmp-1)+".setText(\'"+str(Sudoku[row][cow])+"\')")
                    exec("b.lineEdit_"+str(tmp-1)+".setDisabled(True)")
                    #exec("print (len(b.lineEdit_"+str(tmp-1)+".toPlainText()))")
                    exec("b.lineEdit_"+str(tmp-1)+".setStyleSheet(\"background-color:#9b9b9b;color:white;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
                    
                else:
                    continue 

     
	
	
    def MakeSudoku(self, b):
        self.CloseEvent(self)
        OwnGameFlag = 0
        for i in range(1,82):
            exec("b.lineEdit_"+str(i)+".clear()")
            exec("b.lineEdit_"+str(i)+".setDisabled(False)")
            exec("b.lineEdit_"+str(i)+".setStyleSheet(\"background-color:white;color:black;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
        self.PromptBtn.setDisabled(False)
        tmp = 1
        GameLvl=0
        lambda:self.msgbox(self)
        if(b.EasyRadioBtn.isChecked()==True):
            GameLvl=0
            ColorTop=[240,240,240]
            ColorBottom=[206,255,117]
        if(b.AverageRadioBtn.isChecked()==True):
            GameLvl=1
            ColorTop=[240,240,240]
            ColorBottom=[5,200,224]
        if(b.HardRadioBtn.isChecked()==True):
            GameLvl=2
            ColorTop=[240,240,240]
            ColorBottom=[255,25,25]
        #print ("level:",GameLvl)
        ChangeBackground(self, Form, ColorTop, ColorBottom)
        SudokuThreads(2,GameLvl).start()
        Sudoku = CopyCurrentGrid()
        WriteTempGame("", Sudoku, 1)
        for row in range(0,9):
            for cow in range(0,9):
                tmp+=1
                if(Sudoku[row][cow]!=0):
                    exec("b.lineEdit_"+str(tmp-1)+".setText(\'"+str(Sudoku[row][cow])+"\')")
                    exec("b.lineEdit_"+str(tmp-1)+".setDisabled(True)")
                    exec("b.lineEdit_"+str(tmp-1)+".setStyleSheet(\"background-color:#9b9b9b;color:white;font-family:Arial; font-size:15px;font-weight:bold;padding-left:7%;\")")
                    
                else:
                    continue         


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.NewBtn.setText(_translate("Form", "Nowa Gra"))
        self.EasyRadioBtn.setText(_translate("Form", "Łatwy Poziom"))
        self.AverageRadioBtn.setText(_translate("Form", "Średni Poziom"))
        self.HardRadioBtn.setText(_translate("Form", "Trudny Poziom"))
        self.PromptBtn.setText(_translate("Form", "Podpowiedzi"))
        self.ShowErrorBtn.setText(_translate("Form", "Pokaż Błędy"))
        self.SolveBtn.setText(_translate("Form", "Sprawdź"))
        self.PrintBtn.setText(_translate("Form", "Drukuj"))
        self.SaveBtn.setText(_translate("Form", "Zapis"))
        self.ReadBtn.setText(_translate("Form", "Odczyt"))
        self.ResetBtn.setText(_translate("Form", "Reset"))
        self.MakeOwnBtn.setText(_translate("Form", "Własna Gra"))

    



if __name__ == "__main__":
    if(os.path.isfile("CurrentGame.data")):
        os.remove("CurrentGame.data")    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    app_icon = QtGui.QIcon()
    app_icon.addFile('icon.jpg', QtCore.QSize(256,256))
    #Form.setCursor(Qt.CrossCursor)
    app.setWindowIcon(app_icon)	
    if(not os.path.exists("saved_games")):
       os.makedirs("saved_games")
    ui = Ui_Form()
    ui.setupUi(Form)
    app.aboutToQuit.connect(lambda:ui.CloseEvent(Form,0))
    Form.setWindowTitle("Sudoku - Bartek Żółtowski")
    Form.show()
    Form.setFixedSize(Form.size())

    sys.exit(app.exec_())
    #ResetGame





