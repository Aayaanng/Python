from PyQt5 import QtWidgets as qw
class Window(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("hello world")
        self.setGeometry(600,600,600,600)
app = qw.QApplication([])
window = Window()
window.show()
app.exec_()