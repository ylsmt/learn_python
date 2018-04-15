import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton('btn1', self)
        btn1.move(30, 50)

        btn2 = QPushButton('btn2', self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.resize(1022, 670)

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec_())
