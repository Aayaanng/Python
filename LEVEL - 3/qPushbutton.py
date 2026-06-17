from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui 

font = QtGui.QFont("Comic sans ms", 50)

def button(self):
        self.image = qw.QLabel("car1.png", self)
        self.image.setPixmap(self.img)
        self.image.move(0, 190)
        self.text4 = qw.QLabel("Hello world", self)
        self.text4.setFont(font)
        self.text4.move(0, 380)
        enterbtn = qw.QPushButton("ENTER", self)
        enterbtn.move(0, 320)
        enterbtn.clicked.connect(self.func_)
def func_ (self):
        self.image = qw.QLabel("car.png", self)
        self.text4.setText("Clicked Enter")
        self.text4.resize(500, 350)
        self.image.resize(590, 398)