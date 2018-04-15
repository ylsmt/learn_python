import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Window(QWidget):
    distance_to_center = 0

    def __init__(self):
        super().__init__()

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0},    y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        # self.setMouseTracking(True)

        self.setLayout(grid)

        self.resize(1022, 670)

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x: {0},    y: {1}".format(x, y)
        self.label.setText(text)


app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec_())
