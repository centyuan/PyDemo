import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QApplication, QWidget, QLabel
from bs4 import BeautifulSoup as bs


class coordinate(QWidget):
    def __init__(self, url):
        super(coordinate, self).__init__()
        self.url = url
        self.setup_ui()

    def setup_ui(self):
        """init ui : include webEngineView and a button"""
        btn = QPushButton('start', self)
        self.label1 = QLabel()
        self.browser = QWebEngineView(self)
        self.browser.resize(1000, 800)
        self.browser.load(QUrl(self.url))
        self.browser.show()

        layout = QVBoxLayout(self)
        layout.addWidget(self.browser)
        layout.addWidget(btn)
        layout.addWidget(self.label1)
        btn.clicked.connect(self.get_coordinate)
        # 设置大小与widget一致
        self.browser.setGeometry(0, 0, self.widget.width(), self.widget.height())
        # 设置缩放
        self.browser.setZoomFactor(0.5)
    def get_coordinate(self):
        # self.browser.page().toHtml(self.parse_html)
        # self.web_browser.page().toPlainText(lambda x: print(x))
        self.browser.page().toHtml(lambda x:print(x))

        print('上面是异步执行打印验证')

    def parse_html(self, html_doc):
        longitude, latitude = None, None
        print('源码',html_doc)



if __name__ == "__main__":
    url = 'https://1382.hu/'
    app = QApplication(sys.argv)
    form = coordinate(url)
    form.setGeometry(300, 300, 800, 400)
    form.show()
    sys.exit(app.exec_())