"""
QTimer:定时器
QTimer.singleShot(5000,func): 5秒后执行func
QThread:继承QThrea,重写run

"""
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ShowTime(QWidget):
    def __init__(self):
        super(ShowTime, self).__init__()
        self.setWindowTitle('定时器动态显示时间')
        self.label = QLabel('显示当前时间')
        self.startButton = QPushButton('开始')
        self.endButton = QPushButton('结束')
        layout = QGridLayout()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startButton, 1, 0)
        layout.addWidget(self.endButton, 1, 1)

        # 定时器开启
        self.startButton.clicked.connect(self.start_timer)
        # 定时器结束
        self.endButton.clicked.connect(self.stop_timer)

        self.setLayout(layout)

    def update_time(self):
        current_datetime = QDateTime.currentDateTime()
        time_display = current_datetime.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label.setText(time_display)

    def start_timer(self):
        # 开启定时器
        self.timer.start(1000)  # 1秒时间间隔
        self.startButton.setEnabled(False)
        self.endButton.setEnabled(True)

    def stop_timer(self):
        # 停止定时器
        self.timer.stop()
        self.startButton.setEnabled(True)
        self.endButton.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ShowTime()
    form.show()
    sys.exit(app.exec_())
