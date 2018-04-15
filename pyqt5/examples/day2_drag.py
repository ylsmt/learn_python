from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)
import sys


class Button(QPushButton):
    def __init__(self, title, parent):
        # super().__init__()
        # 这里 要加参数
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Window(QWidget):
    def __init__(self):
        super().__init__()

        edit = QLineEdit('drag', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button('btn', self)
        button.move(190, 65)

        self.resize(1066, 670)


app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec_())
