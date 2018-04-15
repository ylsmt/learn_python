import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1066, 670)
        self.text = "Лев Николаевич Толстой\nАнна Каренина"

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decoratvie', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)


app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec())
