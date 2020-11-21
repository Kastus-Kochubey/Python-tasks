import sys
from random import randint
from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

# from UI impotr Ui_form

# class MyWidget(Ui_form):
class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi("YellowCircles.ui", self)
        # self.setupUi(self)
        self.button.clicked.connect(self.draw)
        self.qp = QtGui.QPainter()

    def draw(self):
        self.repaint()

    def paintEvent(self, e: QtGui.QPaintEvent):
        self.qp.begin(self.label)
        d = randint(3, 100)
        self.qp.setBrush(Qt.yellow)
        self.qp.drawEllipse(randint(0, self.label.width() - d),
                            randint(0, self.label.height() - d),
                            d, d)
        self.qp.end()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
