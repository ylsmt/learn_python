import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Communicate(QObject):
    closeApp = pyqtSignal()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(1022, 670)

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

    def mousePressEvent(self, e):
        # self.c.closeApp.emit()
        pass


app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec_())

# def keyPressEvent(self, e):

#     if e.key() == Qt.Key_Escape:
#         self.close()
