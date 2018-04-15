from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
import sys


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        # e.buttons()
        # e.button() 不能进行拖动 ?
        if e.buttons() != Qt.RightButton:
            return
        mimeData = QMimeData()

        drag = QDrag(self)
        # print(help(drag))
        # print('mimedata:\t', mimeData, '\n', help(mimeData))
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        # print('sethotspot', help(drag.setHotSpot))

        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        super().mousePressEvent(e)

        # e.button()
        if e.button() == Qt.LeftButton:
            print('press')


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(1066, 670)

        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):

        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()


app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec())
