from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(50,50,1080, 640)
        self.setWindowTitle("PYQT5 App")
        
#        self.horizontal()
#        self.vertical()
#        self.verticalAndHorizontal()
#        self.formlayout()
#        self.qsplitter()
        self.gridLayout()
        self.show()
        
    def horizontal(self):
        
        hbox = QHBoxLayout()
        
        # widgets
        button1 = QPushButton("yes",self)
        text1 = QLabel("hello",self)
        button2 = QPushButton("no",self)
        text2 = QLabel("world",self)
        button3 = QPushButton("1",self)
        text3 = QLabel("2",self)
        
        # add widgets into hbox
        hbox.addStretch()
        hbox.addWidget(button1)
        hbox.addWidget(text1)
        hbox.addWidget(button2)
        hbox.addWidget(text2)
        hbox.addWidget(button3)
        hbox.addWidget(text3)
        hbox.addStretch()
        
        self.setLayout(hbox)
    
    def vertical(self):
        
        vbox = QVBoxLayout()
        
        # widgets
        button1 = QPushButton("yes",self)
        text1 = QLabel("hello",self)
        button2 = QPushButton("no",self)
        text2 = QLabel("world",self)
        button3 = QPushButton("1",self)
        text3 = QLabel("2",self)
        
        # add widgets into hbox
#        vbox.addStretch()
        vbox.addWidget(button1)
        vbox.addWidget(text1)
        vbox.addWidget(button2)
        vbox.addWidget(text2)
        vbox.addWidget(button3)
        vbox.addWidget(text3)
        vbox.addStretch()
        
        self.setLayout(vbox)
        
    def verticalAndHorizontal(self):
        
        mainlayout = QHBoxLayout()
        
        leftlayout = QVBoxLayout()
        midlayout = QVBoxLayout()
        rightlayout = QVBoxLayout()
        
        mainlayout.addLayout(leftlayout)
        mainlayout.addLayout(midlayout)
        mainlayout.addLayout(rightlayout)
        
        # widgets
        button1 = QPushButton("left")
        button2 = QPushButton("mid")
        button3 = QPushButton("r1")
        button4 = QPushButton("r2")
        
        leftlayout.addWidget(button1)
        
        midlayout.addWidget(button2)

        rightlayout.addStretch()
        rightlayout.addWidget(button3)
        rightlayout.addWidget(button4)
        rightlayout.addStretch()
        
        self.setLayout(mainlayout)

    def formlayout(self):
        
        hbox1= QHBoxLayout()
        
        hbox1.addWidget(QPushButton("1"))
        hbox1.addWidget(QPushButton("2"))
        hbox1.addStretch()
        
        formLayout = QFormLayout()
        formLayout.addRow(QLabel("Push 1 or 2"), hbox1)
        
        self.setLayout(formLayout)
        
    def qsplitter(self):
        
        hbox = QHBoxLayout(self)
        
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
        
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
        
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        
        
    def createButton(self):
        
        groupBox = QGroupBox("Buttons")
        button1 = QPushButton("1")
        button2 = QPushButton("2")
        button3 = QPushButton("3")
        
        vbox = QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        vbox.addStretch()
        
        groupBox.setLayout(vbox)
        
        return groupBox
        
    def gridLayout(self):
        
        grid = QGridLayout()
        
        grid.addWidget(self.createButton(),0,0)
        grid.addWidget(self.createButton(),1,0)
        
        
        self.setLayout(grid)
        
        
        
        
        
        
        
        
        
        
        
window = Window()        















