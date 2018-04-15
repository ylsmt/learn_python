
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint


class GuessNum(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.num = randint(1, 100)

    def initUI(self):
        # 窗体，位置，大小，标题，图标
        self.setGeometry(200, 50, 800, 600)
        self.setWindowTitle('hello')
        self.setWindowIcon(QIcon('ni.jpg'))

        # 按钮，位置，提示， 点击事件
        self.bt1 = QPushButton('我猜', self)
        #  setGeometry是相对于父窗体来说的一种对子窗体进行位置设置的方法
        self.bt1.setGeometry(350, 260, 120, 50)
        self.bt1.setToolTip('点此猜数字')
        #
        self.bt1.clicked.connect(self.showMessage)

        # 输入框，全选，聚焦，位置
        self.text = QLineEdit('input number', self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(320, 200, 180, 30)

        self.show()

    def showMessage(self):

        # 获取输入
        guessnum = int(self.text.text())

        # messagebox
        if guessnum > self.num:
            QMessageBox.about(self, 'result', '猜大了')
            self.text.setFocus()

        elif guessnum < self.num:
            QMessageBox.about(self, 'result', '猜小了')
            self.text.setFocus()

        else:
            QMessageBox.about(self, 'result', 'right!!')
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()

# 如果关闭QWidget，则生成QCloseEvent
    # def closeEvent(self, event):
    #     reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         event.accept()

    #     else:
    #         event.ignore()


if __name__ == '__main__':
    # 每个Pyqt的程序都必须创建一个application对象
    app = QApplication(sys.argv)
    guess = GuessNum()
    # sys.exit(app.exec_())消息循环结束之后返回0，接着调用sys.exit(0)退出程序
    # app.exec_() 消息循环结束之后，进程自然也会结束
    sys.exit(app.exec_())
