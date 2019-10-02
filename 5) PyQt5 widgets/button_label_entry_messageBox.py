from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(50,50,1080, 640)
        self.setWindowTitle("PYQT5 App")
        
        self.button()
        self.label()
        self.entry()
        self.messageBox()
        self.font()
        self.show()
    
    # button
    def button(self):
        button = QPushButton("Hello World",self)
        button.setToolTip("This is a hello world button")
        button.resize(100,50)
        button.move(50,50)
        button.clicked.connect(self.buttonFunction)

    def buttonFunction(self):
        print("hello world")

    # label
    def label(self):
        
        text1 = QLabel("hello",self)
        self.text2 = QLabel("world",self)
        
        # geometry manager
        text1.move(170,50)
        self.text2.move(170,70)
        
        button1 = QPushButton("Change",self)
        button1.move(170,100)
        button1.clicked.connect(self.button1Function)

    def button1Function(self):
        self.text2.setText("Hello World")
        self.text2.resize(200,25)
        self.text2.setFont(QFont("Arial", 25, QFont.Bold))

    def entry(self):
        
        self.textBox = QLineEdit(self)
        self.textBox.setPlaceholderText("place holder")
        self.textBox.move(300,50)
        
        button1 = QPushButton("Save",self)
        button1.move(300,75)
        button1.clicked.connect(self.saveFunction)
        
    def saveFunction(self):
        
        txt = self.textBox.text()
        
        if txt != "":
            print(txt)
        else:
            print("write something")

    def messageBox(self):
        
        button1 = QPushButton("message",self)
        button1.move(500,50)
        button1.clicked.connect(self.messageFunction)
        
        button2 = QPushButton("message2",self)
        button2.move(500,75)
        button2.clicked.connect(self.messageFunction2)

    def messageFunction(self):
        m_box = QMessageBox.question(self,"Question","Did you enjoy the course?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
    
        if m_box == QMessageBox.Yes:
            print("yes")
        elif m_box == QMessageBox.No:
            print("no")
        else:
            print("cancel")
            
    def messageFunction2(self):
        m_box = QMessageBox.information(self,"Information","Enjor your course")

    
    def font(self):
        self.label = QLabel("Hello world",self)
        self.label.move(700,100)
        
        button2 = QPushButton("choose font",self)
        button2.move(700,50)
        button2.clicked.connect(self.setfont)

    def setfont(self):
        font, ok = QFontDialog.getFont()
        
        if ok:
            self.label.setFont(font)
            self.label.resize(200,75)




















#        
window = Window()







