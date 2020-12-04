from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.setWindowTitle("使用Qpainter绘制图形")
        self.resize(1000, 800)

    def paintEvent(self, even):
        painter = QPainter(self)
        painter.setPen(Qt.red)
        # painter.drawEllipse(80, 10, 50, 30)
        # painter.drawRect(180, 10, 50, 30)
        # painter.drawLine(80, 70, 200, 70)
        # painter.drawText(90, 100, "敢想敢为，注重细节")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())