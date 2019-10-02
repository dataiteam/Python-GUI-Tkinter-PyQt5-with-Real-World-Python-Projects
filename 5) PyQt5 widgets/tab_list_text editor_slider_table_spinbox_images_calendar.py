from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPixmap
import numpy as np
from datetime import datetime
import calendar

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(50,50,1080, 640)
        self.setWindowTitle("PYQT5 App")
        
#        self.tabs()
#        self.listW()
#        self.textEditor()
#        self.slider()
#        self.table()
#        self.spinbox()
#        self.image()
        self.calendar()
        self.show()
       
    def tabs(self):
        
        mainLayout = QVBoxLayout()
        
        self.tab = QTabWidget()
        
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        
        self.button1 = QPushButton("First tab")
        self.button2 = QPushButton("Second tab")
        self.button3 = QPushButton("Third tab")
        
        vbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox2.addWidget(self.button3)
        
        self.tab1.setLayout(vbox)
        self.tab2.setLayout(hbox)
        self.tab3.setLayout(hbox2)
        
        self.tab.addTab(self.tab1, "First")
        self.tab.addTab(self.tab2, "Second")
        self.tab.addTab(self.tab3, "Third")
        
        mainLayout.addWidget(self.tab)
        
        self.setLayout(mainLayout)
     
    def listW(self):
        
        self.list = QListWidget(self)
        
        c = 2019
        
        for i in range(10):
            self.list.addItem(str(c-i))

    def textEditor(self):
        
        self.editor = QTextEdit(self)
        self.editor.move(50,50)
        
        button = QPushButton("Text Editor",self)
        button.move(50,25)
        button.clicked.connect(self.textEditorFunction)

    def textEditorFunction(self):
        text = self.editor.toPlainText()
        print(text)

    def slider(self):
        
        vbox = QVBoxLayout()
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        
        self.slider.valueChanged.connect(self.sliderFunction)
        
        vbox.addWidget(self.slider)
        vbox.addStretch()
        self.setLayout(vbox)
        
    def sliderFunction(self):
        print(self.slider.value())        
        
    def table(self):
        
        vbox = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setRowCount(2)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("method1"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("method2"))
        
        arr = np.array([[1,2],[3,4]])
        for r in range(arr.shape[0]):
            for c in range(arr.shape[1]):
                self.table.setItem(r,c,QTableWidgetItem(str(arr[r,c])))
          
        button = QPushButton("Table")
        button.clicked.connect(self.getValue)

        vbox.addWidget(self.table)
        vbox.addWidget(button)
        self.setLayout(vbox)

    def getValue(self):
        for item in self.table.selectedItems():
            print("Value: {}, row: {}, column: {}".format(item.text(),item.row(),item.column()))

    def spinbox(self):
        
        self.spinbox = QSpinBox(self)
        self.spinbox.move(50,50)
        self.spinbox.setRange(30,40)
        self.spinbox.setSingleStep(1)
        self.spinbox.setSuffix(" $")
            
        button = QPushButton("spin button",self)
        button.move(50,25)
        button.clicked.connect(self.spinFunction)

    def spinFunction(self):
        print(self.spinbox.value())

    def image(self):
        
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap("icon1.png"))
        self.image.move(50,50)

    def calendar(self):
        
        self.calendar = QCalendarWidget(self)
        self.calendar.move(20,20)
        self.calendar.setGridVisible(True)
        
        self.calendar.clicked.connect(self.printDateInfo)  

    def printDateInfo(self, qDate):
        print("{}/{}/{}".format(qDate.month(),qDate.day(),qDate.year()))


window = Window()     























