import re
import sys
import os
import time
from PyQt5.Qt import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from selenium import webdriver
from bs4 import BeautifulSoup
from PyQt5 import QtCore

def filter_url(origin_str):
    url_regex = r"(http|ftp|https):\/\/([\w\-]+(\.[\w\-]+)*\/)*[\w\-]+(\.[\w\-]+)*\/?(\?([\w\-\.,@?^=%&:\/~\+#]*)+)?"
    # x.group() 或x.groups[0]
    match_re = [x.group() for x in re.finditer(url_regex, origin_str)]
    return match_re


def read_text(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            url_text = f.readlines()
            return [item.strip() for item in url_text]


class KeyInfoThread(QThread):
    update_ui_signal = pyqtSignal(str)

    def __init__(self, url, keywords,browser=None):
        super(KeyInfoThread, self).__init__()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  # 无头
        print('运行当前文件夹',os.getcwd())
        self.browser = webdriver.Chrome(
            executable_path=r"resource/chromedriver.exe",
            options=options
        )
        self.url = url
        self.keywords = keywords

    def run(self):
        try:
            self.browser.get(url=self.url)
            self.browser.maximize_window()
            # QApplication.processEvents()
            self.sleep(5)
            ht_page = self.browser.page_source
            # 关键字匹配
            result = re.findall(self.keywords, ht_page)
            if result:
                self.update_ui_signal.emit((str(self.url)))
                self.browser.save_screenshot('resource/screen_shot.png')
            else:
                self.update_ui_signal.emit((str('')))
                self.browser.save_screenshot('resource/screen_shot.png')
                print('图片识别')
            self.browser.close()
        except Exception as e:
            self.browser.close()
            print(e.__traceback__.tb_lineno, e, e.__traceback__.tb_frame.f_globals['__file__'])


class WebSiteFilter(QWidget):
    """QWdidget派生桌面应用程序窗口类"""

    def __init__(self, title='IDCard information'):
        super(WebSiteFilter, self).__init__()
        # 初始化界面
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')  # 无头
        # self.browser = webdriver.Chrome(
        #     executable_path=r"resource/chromedriver.exe",
        #     options=options
        # )
        self.initUI(title)
        self.show()
        self.path = os.getcwd()

    def initUI(self, title):
        root_path = os.path.dirname(__file__)
        # 设置标题图标
        self.setWindowTitle(title)
        # self.setWindowIcon(QIcon(os.path.join(root_path, 'resources/yuan.ico')))
        self.setWindowIcon(QIcon(os.path.join('yuan.ico')))
        self.setFixedSize(1000, 800)
        # 定义控件
        self.website_label = QLabel('输入网址:')
        self.total_line_edit = QLineEdit('总计: 剩余: ')
        self.website_text_edit = QTextEdit('https://www.baidu.com')
        self.website_text_edit.setGeometry(QtCore.QRect(70, 100, 231, 181))
        self.website_text_edit.setAcceptRichText(False)
        self.filter_label = QLabel('筛选关键字:')
        self.filter_line_edit = QLineEdit('图片')
        self.choose_file_btn = QPushButton()
        # self.btn_chooseFile.setObjectName("choose_file_btn")
        self.choose_file_btn.setText('选择文件')
        self.query_button = QPushButton('查询筛序')
        self.result_info_label = QLabel('筛选结果:')
        self.result_info_edit = QTextEdit()

        # self.web_driver = Q
        # 创建网格布局管理器
        self.grid = QGridLayout()
        # 添加控件 addWidget(QWidget, row, col, r, c, alignment) - 在row行col列添加控件，占r行c列，并设置对齐方式
        # 在几行几列，跨越几行几列
        self.grid.addWidget(self.filter_label, 0, 0, 1, 3)
        self.grid.addWidget(self.filter_line_edit, 0, 1, 1, 3)
        self.grid.addWidget(self.choose_file_btn, 0, 8, 1, 1)
        self.grid.addWidget(self.query_button, 1, 8, 1, 1)
        self.grid.addWidget(self.website_label, 2, 0, 1, 4)
        self.grid.addWidget(self.total_line_edit, 2, 1, 1, 2)
        self.grid.addWidget(self.result_info_label, 2, 6, 1, 4)
        self.grid.addWidget(self.website_text_edit, 3, 0, 1, 5)
        self.grid.addWidget(self.result_info_edit, 3, 6, 1, 6)
        # 添加点击事件
        self.query_button.clicked.connect(self.get_keyinfo)
        self.choose_file_btn.clicked.connect(self.choose_file)
        # 设置布局管理器
        self.setLayout(self.grid)

    def choose_file(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                self.path,  # 起始路径
                                                                "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,用双分号间隔
        if fileName_choose == "":
            print("\n取消选择")
            return
        print("\n你选择的文件为:", fileName_choose)
        url_list = read_text(fileName_choose)
        keywords = self.filter_line_edit.text()
        self.number = len(url_list)
        self.total = self.number
        for url in url_list:
            QApplication.processEvents()
            self.getThread_object = KeyInfoThread(url, keywords)
            self.getThread_object.start()
            self.getThread_object.update_ui_signal.connect(self.update_text)

    def get_keyinfo(self):
        urls = self.website_text_edit.toPlainText()
        keywords = self.filter_line_edit.text()
        url_list = filter_url(urls)
        self.number = len(url_list)
        self.total = self.number
        for url in url_list:
            QApplication.processEvents()
            self.getThread_object = KeyInfoThread(url, keywords)
            self.getThread_object.start()
            self.getThread_object.update_ui_signal.connect(self.update_text)

    def update_text(self, url):
        # self.result_info_edit.setText('url信息:' + result)
        self.number = self.number - 1
        print('更新', url)
        self.total_line_edit.setText(f'总计:{self.total} 剩余:{self.number} ')
        if url:
            self.result_info_edit.append('url信息:' + url)
            self.result_info_edit.setStyleSheet('color:green')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序,接受命令行参数
    widget = WebSiteFilter(title='网址筛选')  # 创建窗口
    widget.show()
    sys.exit(app.exec())  # 应用程序主循环结束后，调用sys.exit()方法清理现场
