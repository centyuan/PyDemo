import re
import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from selenium import webdriver
from PyQt5 import QtCore
from aip import AipOcr
import json


class BaiduSdk:
    def __init__(self, app_id, api_key, secret_key, level=1):
        """

        :param app_id:
        :param api_key:
        :param secret_key:
        :param level:识别级别
        (1:调用通用文字识别（标准版）
         2:调用通用文字识别（高精度版）
         3:网络图片文字识别
        )
        """
        self.client = AipOcr(app_id, api_key, secret_key)
        self.level = level

    def get_text(self, file_path=None, file_url=None):
        """
        识别验证码
        :param file_path:
        :param file_url:
        :return: {'words_result': [{'words': '6RS5'}], 'words_result_num': 1, 'log_id': 1581898086821811984}
        """
        try:
            if file_path:
                with open(file_path, 'rb') as f:
                    image = f.read()
                    if self.level == 2:
                        res_image = self.client.basicAccurate(image)
                    elif self.level == 3:
                        res_image = self.client.webImage(image)
                    else:
                        # options 可选参数：CHN_ENG中英混合
                        res_image = self.client.basicGeneral(image, options={'language_type': 'CHN_ENG'})
                    # result = json.loads(res_image)
                    result = res_image
                    # return True, result['words_result'][0]['words']
                    return True, ''.join([item.get('words') for item in result['words_result']])
            elif file_url:
                if self.level == 2:
                    res_url = self.client.basicAccurateUrl(file_url)
                elif self.level == 3:
                    res_url = self.client.webImageUrl(file_url)
                else:
                    res_url = self.client.basicGeneralUrl(file_url, options={'language_type': 'CHN_ENG'})
                result = json.loads(res_url)
                return True, result['words_result'][0]['words']
        except Exception as e:
            return False, str(e)


def filter_url(origin_str):
    try:
        url_regex = r"(http|ftp|https):\/\/([\w\-]+(\.[\w\-]+)*\/)*[\w\-]+(\.[\w\-]+)*\/?(\?([\w\-\.,@?^=%&:\/~\+#]*)+)?"
        # x.group() 或x.groups[0]
        match_re = [x.group() for x in re.finditer(url_regex, origin_str)]
        return match_re
    except Exception as e:
        return None


def read_text(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                url_text = f.readlines()
                return [item.strip() for item in url_text]
    except Exception as e:
        return None


class KeyInfoThread(QThread):
    update_ui_signal = pyqtSignal(str)

    def __init__(self, url_list, keywords, browser=None):
        super(KeyInfoThread, self).__init__()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  # 无头
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--ignore-certificate-errors')  # ssl报错
        options.add_argument('--ignore-ssl-errors')
        self.browser = webdriver.Chrome(executable_path=r"chromedriver.exe", options=options)
        self.url_list = url_list
        self.keywords = keywords
        self.mark = True
    def run(self):
        try:
            i = 1
            number = len(self.url_list)
            while self.mark:
                for url in self.url_list:
                    try:
                        i +=1
                        self.browser.get(url=url)
                        print('匹配run',url)
                        self.sleep(5)
                        # self.browser.implicitly_wait(10)
                        ht_page = self.browser.page_source
                        # 关键字匹配
                        result = re.findall(self.keywords, ht_page)
                        if result:
                            print('正则匹配',result)
                            self.update_ui_signal.emit((str(url)))
                        else:
                            self.browser.save_screenshot('screen_shot.png')
                            self.sleep(1)
                            app_id = '27962995'
                            api_key = 'lfQvGPWiWaYcPGt90n58PVhx'  # AK
                            secret_key = 'ind5NK0lUMFtAj87uMkcmQASF6IswIZh '  # Sk
                            baidu_client = BaiduSdk(app_id=app_id, api_key=api_key, secret_key=secret_key, level=2)
                            mark, text = baidu_client.get_text(file_path=r'screen_shot.png')
                            print('图片匹配',self.keywords,text)
                            os.remove(r'screen_shot.png')
                            if self.keywords in text:
                                self.update_ui_signal.emit((str(url)))
                                print('text:', text)
                            else:
                                self.update_ui_signal.emit((str('')))
                    except Exception as e:
                        print('错误信息', e.__traceback__.tb_lineno, e, e.__traceback__.tb_frame.f_globals['__file__'])
                        self.update_ui_signal.emit((str('超时:'+url)))
                        continue
                    finally:
                        if i == number:
                            self.mark=False
                self.browser.close()
        except Exception as e:
                self.browser.close()
                self.update_ui_signal.emit((str('错误:'+url)))
                print('错误信息',e.__traceback__.tb_lineno, e, e.__traceback__.tb_frame.f_globals['__file__'])


class WebSiteFilter(QWidget):
    """QWdidget派生桌面应用程序窗口类"""

    def __init__(self, title='website'):
        super(WebSiteFilter, self).__init__()
        self.initUI(title)
        self.show()
        self.path = os.getcwd()

    def show_message(self, messages):
        QMessageBox.warning(self, '警告', messages, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def initUI(self, title):
        root_path = os.path.dirname(__file__)
        # 设置标题图标
        self.setWindowTitle(title)
        # self.setWindowIcon(QIcon(os.path.join(root_path, 'resources/yuan.ico')))
        self.setWindowIcon(QIcon(os.path.join(r'logo.ico')))
        self.setFixedSize(1400, 1000)
        self.activateWindow()
        # self.maximumSize(Qtsize())
        # self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint);
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

        # 定义控件
        self.website_label = QLabel('输入网址:')
        self.website_label.setFont(QFont("微软雅黑",10,QFont.Bold))
        self.total_line_edit = QLineEdit('总计: 剩余: ')
        self.total_line_edit.setStyleSheet('color:red')
        self.website_text_edit = QTextEdit('https://www.3703yh.com/')
        self.website_text_edit.setGeometry(QtCore.QRect(70, 100, 231, 181))
        self.website_text_edit.setAcceptRichText(False)
        self.filter_label = QLabel('筛选关键字:')
        self.filter_label.setFont(QFont("微软雅黑",10,QFont.Bold))
        self.filter_line_edit = QLineEdit('公告')
        self.choose_file_btn = QPushButton()
        # self.btn_chooseFile.setObjectName("choose_file_btn")
        self.choose_file_btn.setText('选择文件')
        self.choose_file_btn.setFont(QFont("微软雅黑",10,QFont.Bold))
        self.query_button = QPushButton('查询')
        self.query_button.setFont(QFont("微软雅黑",10,QFont.Bold))
        self.result_info_label = QLabel('筛选结果:')
        self.result_info_label.setFont(QFont("微软雅黑",10,QFont.Bold))
        self.result_info_edit = QTextEdit()
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
        self.grid.addWidget(self.website_text_edit, 3, 0, 1, 4)
        self.grid.addWidget(self.result_info_edit, 3, 6, 1, 6)
        # 添加点击事件
        self.query_button.clicked.connect(self.input_site)
        self.choose_file_btn.clicked.connect(self.file_site)
        # 设置布局管理器
        self.setLayout(self.grid)

    def file_site(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                self.path,  # 起始路径
                                                                "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,用双分号间隔
        if fileName_choose == "":
            print("\n取消选择")
            return
        print("\n你选择的文件为:", fileName_choose)
        keywords = self.filter_line_edit.text()
        url_list = read_text(fileName_choose)
        if not url_list:
            self.show_message('无相关网址或信息有误')
        self.number = len(url_list)
        self.total = self.number
        self.total_line_edit.setText(f'总计:{self.total} 剩余:{self.number} ')
        QApplication.processEvents()
        self.getThread_object = KeyInfoThread(url_list, keywords)
        self.getThread_object.start()
        self.getThread_object.update_ui_signal.connect(self.update_text)

    def input_site(self):
        urls = self.website_text_edit.toPlainText()
        keywords = self.filter_line_edit.text()
        url_list = filter_url(urls)
        if not url_list:
            self.show_message('无相关网址或信息有误')
        self.number = len(url_list)
        self.total = self.number
        self.total_line_edit.setText(f'总计:{self.total} 剩余:{self.number} ')
        QApplication.processEvents()
        self.getThread_object = KeyInfoThread(url_list, keywords)
        self.getThread_object.start()
        self.getThread_object.update_ui_signal.connect(self.update_text)

    def update_text(self, url):
        # self.result_info_edit.setText('url信息:' + result)
        self.number = self.number - 1
        print('更新url', url)
        self.total_line_edit.setText(f'总计:【{self.total}】 剩余:【{self.number}】 ')
        self.total_line_edit.setStyleSheet('color:red')
        if url:
            self.result_info_edit.append(url)
            self.result_info_edit.setStyleSheet('color:blue')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序,接受命令行参数
    widget = WebSiteFilter(title='网址筛选')  # 创建窗口
    # widget.showMaximized()
    widget.show()
    sys.exit(app.exec())  # 应用程序主循环结束后，调用sys.exit()方法清理现场
