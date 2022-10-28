import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QPoint


class Drawing(QWidget):
    def __init__(self, parent=None):
        super(Drawing, self).__init__(parent)
        self.setWindowTitle('绘图应用')
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUi()

    def initUi(self):
        self.resize(600, 600)
        # 画布大小,背景白色
        self.pix = QPixmap(600, 600)
        self.pix.fill(Qt.white)

    def paintEvent(self, event):
        pp = QPainter(self.pix)
        # 根据鼠标移动的前后位置绘制直线
        pp.drawLine(self.lastPoint, self.endPoint)
        #
        self.lastPoint = self.endPoint
        # 更新画布
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self,event):
        # 鼠标左键按下
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()

    def mouseMoveEvent(self,event):
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()  # 触发paintEvent事件

    def mouseReleaseEvent(self, event):
        # 鼠标左键释放
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Drawing()
    widget.show()
    sys.exit(app.exec_())