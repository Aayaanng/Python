import sys
from PyQt5 import QtGui 
from PyQt5 import QtWidgets as qw

font = QtGui.QFont("Comic sans ms", 50)

class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.img = QtGui.QPixmap('car1.png')
        self.image.setPixmap(self.img)
        self.image.move(0, 190)
        self.setWindowTitle("hello world")
        self.setGeometry(750,400,800,800)
        self.Window2()
        self.button()
    def Window2(self):
        text1 = qw.QLabel("hello world", self)
        text1.move(0, 0)
        text1.setFont(font)
        text2 = qw.QLabel("Aayaann", self)
        text2.setFont(font)
        text2.move(0, 60)
        text3 = qw.QLabel("Gupta", self)
        text3.setFont(font)
        text3.move(0, 120)
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
def main():
    app = qw.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()