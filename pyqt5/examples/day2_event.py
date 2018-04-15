import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QLCDNumber, QDial, QSlider, QApplication)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # lcd = QLCDNumber(self)
        # dial = QDial(self)
        # qslider = QSlider(Qt.Horizontal, self)

        # qslider.setOrientation(Qt.Horizontal)

        self.resize(1067, 660)

        # lcd.setGeometry(100, 50, 150, 60)
        # dial.setGeometry(120, 120, 100, 100)
        # qslider.setGeometry(240, 160, 100, 40)
        # dial.valueChanged.connect(lcd.display)
        # qslider.valueChanged.connect(lcd.display)

        self.lab = QLabel('arrow', self)
        self.lab.setGeometry(120, 280, 100, 50)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.lab.setText('↑')
        elif e.key() == Qt.Key_Down:
            self.lab.setText('↓')
        elif e.key() == Qt.Key_Left:
            self.lab.setText('←')
        else:
            self.lab.setText('→')


app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec_())
