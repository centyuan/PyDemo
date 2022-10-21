import re
import sys
import os
import time
from PyQt5.Qt import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from selenium import webdriver
from bs4 import BeautifulSoup


class GetKeyInfoThread(QThread):
    update_ui_signal = pyqtSignal(str)

    def __init__(self, url):
        super(GetKeyInfoThread, self).__init__()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  # 无头
        self.browser = webdriver.Chrome(
            executable_path=r"D:\BaiduNetdiskDownload\python-demo\develop_relate\chromedriver.exe",
            options=options
        )
        self.url = url

    def run(self):
        self.browser.get(url=self.url)
        # QApplication.processEvents()
        time.sleep(3)
        ht_page = self.browser.page_source
        result = re.findall('网盘', ht_page)
        if result:
            print('结果', result)
        # print('源码', ht_page)
        self.browser.save_screenshot('resource/screen_shot.png')
        self.update_ui_signal.emit((str(result)))


class IdCardOperation(QWidget):
    """QWdidget派生桌面应用程序窗口类"""

    def __init__(self, title='IDCard information'):
        super(IdCardOperation, self).__init__()
        # 初始化界面
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  # 无头
        self.browser = webdriver.Chrome(
            executable_path=r"D:\BaiduNetdiskDownload\python-demo\develop_relate\chromedriver.exe",
            options=options
        )
        self.initUI(title)
        self.show()

    def initUI(self, title):
        root_path = os.path.dirname(__file__)
        # 设置标题图标
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(os.path.join(root_path, 'resources/yuan.jpg')))
        self.setFixedSize(1000, 800)
        # 定义控件
        self.birthday_label = QLabel('出生日期:')
        self.birthday_line_edit = QLineEdit('1997-03-01')
        self.address_label = QLabel('地址:')
        self.address_line_edit = QLineEdit('成都')
        self.sex_label = QLabel('性别:')
        # 单选
        self.sex_comboBox = QComboBox()
        self.sex_comboBox.addItem('男')
        self.sex_comboBox.addItem('女')
        self.random_button = QPushButton('随机')
        self.idcard_label = QLabel('身份证号码:')
        self.idcard_line_edit = QLineEdit()
        self.query_button = QPushButton('查询')
        self.idcard_info_label = QLabel('身份证信息:')
        self.idcard_info_text_edit = QTextEdit()
        # 创建网格布局管理器
        self.grid = QGridLayout()
        # 添加控件 addWidget(QWidget, row, col, r, c, alignment) - 在row行col列添加控件，占r行c列，并设置对齐方式
        self.grid.addWidget(self.birthday_label, 0, 0, 1, 1)
        self.grid.addWidget(self.birthday_line_edit, 0, 1, 1, 3)
        self.grid.addWidget(self.address_label, 0, 4, 1, 1)
        self.grid.addWidget(self.address_line_edit, 0, 5, 1, 3)
        self.grid.addWidget(self.sex_label, 0, 8, 1, 1)
        self.grid.addWidget(self.sex_comboBox, 0, 9, 1, 2)
        self.grid.addWidget(self.random_button, 0, 11, 1, 1)
        self.grid.addWidget(self.idcard_label, 1, 0, 1, 1)
        self.grid.addWidget(self.idcard_line_edit, 1, 1, 1, 10)
        self.grid.addWidget(self.query_button, 1, 11, 1, 1)
        self.grid.addWidget(self.idcard_info_label, 2, 0, 1, 1)
        self.grid.addWidget(self.idcard_info_text_edit, 3, 0, 1, 12)
        # 添加点击事件
        self.query_button.clicked.connect(self.get_keyinfo)
        # 设置布局管理器
        self.setLayout(self.grid)

    def update_text(self, result):
        self.idcard_info_text_edit.setText('url信息:' + result)
        self.idcard_info_text_edit.setStyleSheet('color:red')

    def get_keyinfo(self):
        url = self.idcard_line_edit.text()
        self.getThread_object = GetKeyInfoThread(url)
        self.getThread_object.start()
        self.getThread_object.update_ui_signal.connect(self.update_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序,接受命令行参数
    widget = IdCardOperation(title='身份证')  # 创建窗口
    widget.show()
    sys.exit(app.exec())  # 应用程序主循环结束后，调用sys.exit()方法清理现场
