import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QHBoxLayout


class MyThread(QThread):
    send_signal = pyqtSignal(str)

    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        for idx in range(100):
            print('run',idx)
            self.send_signal.emit(str(idx))
            time.sleep(1)


class MainApp(QWidget):
    def __init__(self):
        super(MainApp, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('我的窗口')

        # 实例化线程类
        self.my_thread = MyThread()

        # 创建进度条和下载按钮
        layout = QHBoxLayout()
        self.progress = QProgressBar()
        self.btn = QPushButton('下载')
        layout.addWidget(self.progress, stretch=9)
        layout.addWidget(self.btn, stretch=1)
        self.setLayout(layout)

        self.btn.clicked.connect(self.on_clicked)  # 重点代码1

        self.resize(400, 100)
        self.show()

    def on_clicked(self):
        self.my_thread.send_signal.connect(self.update_view)  # 重点代码2
        self.my_thread.start()

    def update_view(self, data):
        print('update',data)
        self.progress.setValue(int(data))  # 重点代码3


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())
