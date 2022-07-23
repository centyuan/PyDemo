import json
import time
from random import random

import requests
from PyQt5.QtCore import QTimer, Qt,QThread,pyqtSignal
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5 import QtCore, QtGui, QtWidgets



auth_data = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJIWDFqOXRhb2xvdjEzMTQiLCJib2R5Ijp7ImNvdW50cnlDb2RlIjoiKzg2IiwibWVyY2hhbnQiOiJIWDEiLCJvcmlnaW4iOiIyMjIuMjA5LjIwOC4xNjYiLCJyZWdEZXZpY2UiOiJtb2JpbGUiLCJyZWdIb3N0IjoiMTI3LjAuMC4xIiwicmVnSXAiOiIxMjcuMC4wLjEiLCJzdGF0ZSI6Ik5PUk1BTCIsInVzZXJuYW1lIjoiSFgxajl0YW9sb3YxMzE0In0sImJvZHlDbGFzcyI6ImNvbS5wZy5sb2JieS5qOWJjLmF1dGguc2hpcm8uU2hpcm9Vc2VyIiwiZXhwIjoxNjU3NzEzNDI3OTk2LCJpYXQiOjE2NTc3MDk4Mjc5OTYsImp0aSI6ImU3NDRlNGU1LTM3MjctNGZmMi05NDkyLTI0N2I5MjE0MWIyYyIsIm5iZiI6MTY1NzcwOTgyNzk5Nn0.mQGtViitkQSg80gqD79dhfuvbDb9C6BLkJXBFZkBgwI'
wallet_url = 'https://j9bcrest.com/api/customer/wallet'
to_url = 'https://j9bcrest.com/api/swap/open/calc/to'
tran_url = 'https://j9bcrest.com/api/swap/trading-pair/transaction'
# https://j9con.com/

new_h = {
    'authority': 'j9bcrest.com',
    'x-request-domain': 'j9con.com',
    'accept-language': 'cn',
    'sec-ch-ua-mobile': '?0',
    'display-language': 'cn',
    'authorization': auth_data,
    'product-id': 'HX1',
    'accept': 'application/json, text/plain, */*',
    'x-website-code': 'HX1_PC',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://j9con.com/',
}


class MyThread(QThread):
    send_signal = pyqtSignal(str)

    def __init__(self, maindow):
        super(MyThread, self).__init__()
        self.maindow = maindow

    def run(self):

        self.send_signal.emit(str(1))
        time.sleep(1)


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title of main window
        self.setWindowTitle('jiyou')
        # set the size of window
        # self.Width = 700
        # self.height = int(0.618 * self.Width)
        # self.resize(self.Width, self.height)
        self.resize(1300,800)
        # top
        self.Label_website = QLabel("访问网址:")
        self.Label_website.setFont(QFont('bold', 10))
        self.LineEdit_input_website = QLineEdit('https://j9con.com/swap')
        self.lineEdit_balance_price = QLineEdit()
        self.pushButton_start = QPushButton('开始')

        # first left
        self.Label_request_data = QLabel("请求数据")
        self.textEdit_payloadtoken = QTextEdit()
        self.textEdit_payloadtoken.setAcceptRichText(False) # 粘贴看不见

        #second left
        self.checkBox_buy = QCheckBox('买入,阈值')
        self.LineEdit_buy_dis = QLineEdit()
        self.Label_buy_danbi = QLabel('单笔')
        self.LineEdie_buy_input = QLineEdit()
        self.pushButton_buy = QPushButton('买入')

        #
        self.checkBox_sell = QCheckBox('卖出,阈值')
        self.LineEdit_sell_dis = QLineEdit()
        self.Label_sell_danbi = QLabel('单笔')
        self.LineEdie_sell_input = QLineEdit()
        self.pushButton_sell = QPushButton('卖出')

        # second right


        self.textBox_display = QTextEdit(self)

        # self.initUI()

    def initUI(self,MainWindow):
        # setting up layout of main window
        self.top_widget = self.create_top_widget()
        self.lower_widget = self.create_lower_widget()
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.top_widget)
        self.main_layout.addWidget(self.lower_widget)

        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 4)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        # self.setCentralWidget(self.main_widget)
        MainWindow.setCentralWidget(self.main_widget)
        self.pushButton_start.clicked.connect(MainWindow.keep_wallet)
        self.pushButton_buy.clicked.connect(MainWindow.J9BC_in)
        self.pushButton_sell.clicked.connect(MainWindow.J9BC_out)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_top_widget(self):
        self.top_layout = QHBoxLayout()
        self.top_layout.addWidget(self.Label_website)
        self.top_layout.setStretch(0, 1)
        self.top_layout.addWidget(self.LineEdit_input_website)
        self.top_layout.setStretch(1, 1)
        # top_layout.addStretch(1)
        self.top_layout.addWidget(self.lineEdit_balance_price)
        self.top_layout.setStretch(2, 3)
        self.top_layout.addWidget(self.pushButton_start)
        self.top_layout.setStretch(3, 1)

        self.top_widget = QWidget()
        self.top_widget.setLayout(self.top_layout)
        return self.top_widget

    def create_lower_widget(self):
        # 左边布局
        # 请求数据行
        self.layout_first = QHBoxLayout()
        self.layout_first.addWidget(self.Label_request_data)
        self.layout_first.addWidget(self.textEdit_payloadtoken)
        self.widget_first = QWidget()
        self.widget_first.setLayout(self.layout_first)
        # 买入
        self.layout_second = QHBoxLayout()
        self.layout_second.addWidget(self.checkBox_buy)
        self.layout_second.addWidget(self.LineEdit_buy_dis)
        self.layout_second.addWidget(self.Label_buy_danbi)
        self.layout_second.addWidget(self.LineEdie_buy_input)
        self.widget_second = QWidget()
        self.widget_second.setLayout(self.layout_second)

        # 买入按钮
        # 卖出
        self.layout_three = QHBoxLayout()
        self.layout_three.addWidget(self.checkBox_sell)
        self.layout_three.addWidget(self.LineEdit_sell_dis)
        self.layout_three.addWidget(self.Label_sell_danbi)
        self.layout_three.addWidget(self.LineEdie_sell_input)
        self.widget_three = QWidget()
        self.widget_three.setLayout(self.layout_three)

        self.lower_left_widget = QWidget()
        self.lower_left_layout = QVBoxLayout()

        self.lower_left_layout.addWidget(self.widget_first) # first
        self.lower_left_layout.addWidget(self.widget_second) # second
        self.lower_left_layout.addWidget(self.pushButton_buy) # buy_button
        self.lower_left_layout.addWidget(self.widget_three) # three
        self.lower_left_layout.addWidget(self.pushButton_sell)  # sell_button

        self.lower_left_widget.setLayout(self.lower_left_layout)
        # 右边布局
        self.lower_right_layout = QVBoxLayout()
        self.lower_right_layout.addWidget(self.textBox_display)
        self.lower_right_widget = QWidget()
        self.lower_right_widget.setLayout(self.lower_right_layout)

        self.lower_layout = QHBoxLayout()
        self.lower_layout.addWidget(self.lower_left_widget)
        self.lower_layout.addWidget(self.lower_right_widget)
        self.lower_layout.setStretch(0,1)
        self.lower_layout.setStretch(1,2)
        self.lower_widget = QWidget()
        self.lower_widget.setLayout(self.lower_layout)
        return self.lower_widget


class action_class(QMainWindow):
    def __init__(self, app,parent=None):
        super(QMainWindow, self).__init__(parent)
        self.auth_data = ''
        self.app = app
        print('app',self.app)
        self.new_h = {
            'authority': 'j9bcrest.com',
            'x-request-domain': 'j9con.com',
            'accept-language': 'cn',
            'sec-ch-ua-mobile': '?0',
            'display-language': 'cn',
            'authorization': auth_data,
            'product-id': 'HX1',
            'accept': 'application/json, text/plain, */*',
            'x-website-code': 'HX1_PC',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://j9con.com/',
        }

        # self.ui = jiuyou.Ui_MainWindow()
        # self.ui = Ui_MainWindow()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)  # 初始化窗口
        self.ui = Ui_MainWindow()
        self.ui.initUI(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_keep)
        # self.my_thread = MyThread(self)
        self.timer_buy = QTimer(self)
        self.timer_buy.timeout.connect(self.while_buy)
        self.timer_sell = QTimer(self)
        self.timer_sell.timeout.connect(self.while_sell)

    def start_for(self):

        if self.ui.LineEdie_sell_input.text():
            print('start_for,卖出')
            self.my_thread.send_signal.connect(self.while_sell)  # 重点代码2
            self.my_thread.start()
        else:
            print('start_for买入')
            self.my_thread.send_signal.connect(self.while_sell)  # 重点代码2
            self.my_thread.start()


    def while_sell(self):
        input_value = self.ui.LineEdie_sell_input.text()
        is_checked = self.ui.checkBox_sell.isChecked()
        singel_value = self.ui.LineEdit_sell_dis.text()
        print('while_sell', input_value, '2',singel_value,is_checked)
        # for i in range(1000):
        print('while_sell定时器', input_value, '2',singel_value,is_checked)

        try:
            # value, real_value = self.J9BC_sellunitprice(input_value)

            fake_value = float(singel_value) * float(input_value)
            print('卖出payload', input_value, singel_value, fake_value)
            tran_url = 'https://www.j9bcrest.com/api/swap/trading-pair/transaction'
            tran_data = {"fromToken": "J9BC", "fromValue": input_value, "slippageTolerance": 0.02,
                         "toValue": fake_value,
                         "tradeCode": "J9BC_USDT"}
            tran_res = requests.post(tran_url, json=tran_data, headers=self.new_h)
            print('返回:tran_res', tran_res.text)
            # print('tran_res:', tran_res.text)
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            message = f'{time_str}单价:{singel_value}---卖出成功:{tran_res.json().get("data").get("message")}'
            print('返回:message', message)
            self.update_text(message)

            with open('jiuyou.txt', 'a') as file:
                file.writelines(message + '\n')
            time.sleep(10)
        except Exception as e:
            print('异常',e.__traceback__.tb_frame.f_globals['__file__'],e.__traceback__.tb_lineno,e)
            QMessageBox.information(self, "九游", "输入不能为空",QMessageBox.Yes)

    def while_buy(self):
        input_value = self.ui.LineEdie_buy_input.text()
        is_checked = self.ui.checkBox_buy.isChecked()
        single_value = self.ui.LineEdit_buy_dis.text()
        print('while buy定时器', input_value,is_checked,single_value,is_checked)
        # for i in range(1000):
        try:

            if input_value:
                # to_value, real_value = self.J9BC_buyunitprice(input_value)

                fake_value = float(single_value) * float(input_value)
                print('买入', input_value, single_value, fake_value)
                tran_url = 'https://www.j9bcrest.com/api/swap/trading-pair/transaction'
                tran_data = {"fromToken": "USDT", "fromValue": fake_value, "slippageTolerance": 0.02,
                             "toValue": input_value,
                             "tradeCode": "J9BC_USDT"}
                tran_res = requests.post(tran_url, json=tran_data, headers=self.new_h)
                print('买入返回tran_res', tran_res.text)
                time_str = time.strftime("%Y-%m-%d %H:%M:%S")
                message = f'{time_str}单价:{single_value}---买入成功:{tran_res.json().get("data").get("message")}-买入设置价格+{str(single_value)}'
                self.update_text(message)

                with open('jiuyou.txt', 'a') as file:
                    file.writelines(message + '\n')
            else:
                QMessageBox.information(self, "九游", "输入不能为空",
                                        QMessageBox.Yes)
            time.sleep(10)
        except Exception as e:
            print('异常',e.__traceback__.tb_frame.f_globals['__file__'],e.__traceback__.tb_lineno,e)
            QMessageBox.information(self, "九游", "输入不能为空",QMessageBox.Yes)


    def update_text(self,message):
        # self.ui.textBox_display.repaint((message,))
        self.ui.textBox_display.setStyleSheet("color:green")
        self.ui.textBox_display.append(message)
        # self.app.processEvents()  # 循环函数不执行玩更新
        QApplication.processEvents()
        time.sleep(2)
        print('更新完成')


    def time_keep(self):
        try:
            wallet_url = 'https://www.j9bcrest.com/api/customer/wallet'
            auth_d = self.ui.textEdit_payloadtoken.toPlainText()
            if auth_d:
                self.new_h['authorization'] = auth_d
                wall_res = requests.get(wallet_url, headers=self.new_h)
                # print('余额', wall_res.text)
                res_data = wall_res.json()

                if not res_data.get('code'):
                    balance = res_data.get('data')
                    display_str = f'余额: USDT:{balance.get("USDT")}  J9BC:{balance.get("J9BC")}'
                    # print(f'余额: USDT:{balance.get("USDT")}  J9BC:{balance.get("J9BC")}')
                    self.ui.lineEdit_balance_price.setStyleSheet("color:red")
                    self.ui.lineEdit_balance_price.setText(display_str)
                else:
                    display_str = f'错误:{res_data.get("message")}'
                    # print(f'错误:{res_data.get("message")}')
                    self.ui.lineEdit_balance_price.setText(display_str)
                # 卖出 1 J9BC -> 0.xxx USDT
                to_data = {'token': 'J9BC', 'value': 1, 'tradeCode': 'J9BC_USDT',
                           }
                to_url = 'https://www.j9bcrest.com/api/swap/open/calc/to'
                to_res = requests.post(to_url, headers=self.new_h, json=to_data)
                dis_value_1 = to_res.json().get('data').get('value')
                # 买入 0.xxx USDT -> 1J9BC
                from_url = 'https://www.j9bcrest.com/api/swap/open/calc/from'
                # token: J9BC, USDT
                from_data = {'token': 'J9BC', 'value': 1, 'tradeCode': 'J9BC_USDT', }
                from_res = requests.post(from_url, headers=self.new_h, json=from_data)
                dis_value_2 = from_res.json().get('data').get('value')

                # self.ui.lineEdit_USDI_input.setText(str(dis_value_1))
                # self.ui.lineEdit_J9BC_input.setText(str(dis_value_2))
                message = f'卖出价:{dis_value_1}=买入价:{dis_value_2}'
                print('定时器')
                self.ui.lineEdit_balance_price.setText(display_str+'='+message)
                # self.ui.lineEdit_balance_price.adjustSize()
            else:
                QMessageBox.information(self, "九游", "输入不能为空",
                                        QMessageBox.Yes)
        except Exception as e:
            QMessageBox.information(self, "九游", "稍后再试"+str(e),
                                    QMessageBox.Yes)


    def keep_wallet(self):
        try:
            wallet_url = 'https://www.j9bcrest.com/api/customer/wallet'
            auth_d = self.ui.textEdit_payloadtoken.toPlainText()
            if auth_d:
                self.new_h['authorization'] = auth_d
                wall_res = requests.get(wallet_url, headers=self.new_h)
                print('余额',wall_res.text)
                res_data = wall_res.json()

                if not res_data.get('code'):
                    balance = res_data.get('data')
                    display_str = f'余额: USDT:{balance.get("USDT")}  J9BC:{balance.get("J9BC")}'
                    print(f'余额: USDT:{balance.get("USDT")}  J9BC:{balance.get("J9BC")}')
                    self.ui.lineEdit_balance_price.setStyleSheet("color:red")
                    self.ui.lineEdit_balance_price.setText(display_str)
                else:
                    display_str = f'错误:{res_data.get("message")}'
                    print(f'错误:{res_data.get("message")}')
                    self.ui.lineEdit_balance_price.setText(display_str)
                # 卖出 1 J9BC -> 0.xxx USDT
                to_data = {'token': 'J9BC','value': 1,'tradeCode': 'J9BC_USDT',
                }
                to_url = 'https://www.j9bcrest.com/api/swap/open/calc/to'
                to_res = requests.post(to_url, headers=self.new_h, json=to_data)
                dis_value_1= to_res.json().get('data').get('value')
                # 买入 0.xxx USDT -> 1J9BC
                from_url = 'https://www.j9bcrest.com/api/swap/open/calc/from'
                # token: J9BC, USDT
                from_data = {'token': 'J9BC','value': 1,'tradeCode': 'J9BC_USDT',}
                from_res = requests.post(from_url, headers=self.new_h, json=from_data)
                dis_value_2 = from_res.json().get('data').get('value')

                self.ui.LineEdit_sell_dis.setText(str(dis_value_1))
                self.ui.LineEdit_buy_dis.setText(str(dis_value_2))
                message = f'卖出价:{dis_value_1}=买入价:{dis_value_2}'
                self.ui.lineEdit_balance_price.setText(display_str +'='+ message)
                self.ui.lineEdit_balance_price.adjustSize()
            else:
                QMessageBox.information(self, "九游", "输入不能为空",
                                        QMessageBox.Yes)
            self.timer.start(6000)
        except Exception as e:
            QMessageBox.information(self, "九游", "稍后再试"+str(e),
                                    QMessageBox.Yes)


    def J9BC_sellunitprice(self,value):
        # 卖出 1 J9BC -> 0.0157 USDT
        try:
            to_url = 'https://www.j9bcrest.com/api/swap/open/calc/to'
            # token: J9BC, USDT
            to_data = {
                'token': 'J9BC',
                'value': value,
                'tradeCode': 'J9BC_USDT',
            }
            # print('卖出J9BC', to_data)
            to_res = requests.post(to_url, headers=self.new_h, json=to_data)
            print(to_res.text)
            to_value = to_res.json().get('data').get('value')
            # print('to_res:', to_res.text, to_value)
            return value, to_value
        except Exception as e:
            QMessageBox.information(self, "九游", "稍后再试"+str(e),
                                    QMessageBox.Yes)

    def J9BC_out(self):
        # 卖出 1 J9BC -> 0.0157 USDT
        try:
            input_value = self.ui.LineEdie_sell_input.text()
            is_checked = self.ui.checkBox_sell.isChecked()
            # is_checked = False
            print('进入卖出',input_value,is_checked)
            if input_value:

                if is_checked :
                    # for i in range(100):
                    #     # value, real_value = self.J9BC_sellunitprice(input_value)
                    #     singel_value = self.ui.LineEdit_sell_dis.text()
                    #     fake_value = float(singel_value) * float(input_value)
                    #     print('循环卖出', input_value, singel_value, fake_value)
                    #     tran_url = 'https://www.j9bcrest.com/api/swap/trading-pair/transaction'
                    #     tran_data = {"fromToken": "J9BC", "fromValue": input_value, "slippageTolerance": 0.02,
                    #                  "toValue": fake_value,
                    #                  "tradeCode": "J9BC_USDT"}
                    #     tran_res = requests.post(tran_url, json=tran_data, headers=self.new_h)
                    #     print('卖出返回:tran_res', tran_res.text)
                    #     # print('tran_res:', tran_res.text)
                    #     time_str = time.strftime("%Y-%m-%d %H:%M:%S")
                    #     message = f'{time_str}单价:{singel_value}---卖出成功:{tran_res.json().get("data").get("message")}'
                    #     print('卖出返回:message', message)
                    #     self.update_text(message)
                    #     # self.ui.textBox_display.setStyleSheet("color:green")
                    #     # self.ui.textBox_display.append(message+'卖出设置价格'+str(singel_value))
                    #     # self.ui.pushButton_sell.clear()
                    #     # print('tran_res:', tran_res.text)
                    #     with open('jiuyou.txt', 'a') as file:
                    #         file.writelines(message + '\n')
                    #     time.sleep(30)
                    # self.start_for()
                    self.timer_sell.start(25000)
                else:
                    # value, real_value = self.J9BC_sellunitprice(input_value)
                    singel_value = self.ui.LineEdit_sell_dis.text()
                    fake_value = float(singel_value) * float(input_value)
                    print('一次卖出', input_value, singel_value, fake_value)
                    tran_url = 'https://www.j9bcrest.com/api/swap/trading-pair/transaction'
                    tran_data = {"fromToken": "J9BC", "fromValue": input_value, "slippageTolerance": 0.02,
                                 "toValue": fake_value,
                                 "tradeCode": "J9BC_USDT"}
                    tran_res = requests.post(tran_url, json=tran_data, headers=self.new_h)
                    print('卖出返回:tran_res', tran_res.text)
                    # print('tran_res:', tran_res.text)
                    time_str = time.strftime("%Y-%m-%d %H:%M:%S")
                    message = f'{time_str}单价:{singel_value}---卖出成功:{tran_res.json().get("data").get("message")}'
                    print('卖出返回:message', message)
                    self.update_text(message)

                    with open('jiuyou.txt', 'a') as file:
                        file.writelines(message + '\n')

            else:
                QMessageBox.information(self, "九游", "输入不能为空",
                                        QMessageBox.Yes)




        except Exception as e:
            QMessageBox.information(self, "九游", "稍后再试" + str(e),
                                    QMessageBox.Yes)

    def J9BC_buyunitprice(self,value):
        # 0.xxUSDT 兑换1 J9BC 买入1 J9BC
        try:
            to_url = 'https://www.j9bcrest.com/api/swap/open/calc/from'
            # token: J9BC, USDT
            to_data = {
                'token': 'J9BC',
                'value': value,
                'tradeCode': 'J9BC_USDT',
            }
            # print('买进J9BC', to_data)
            to_res = requests.post(to_url, headers=self.new_h, json=to_data)
            to_value = to_res.json().get('data').get('value')
            # print('to_res:', to_res.text, to_value)
            return value, to_value
        except Exception as e:
            QMessageBox.information(self, "九游", "稍后再试" + str(e),
                                    QMessageBox.Yes)

    def J9BC_in(self):
        # 0.xxUSDT 兑换1 J9BC 买入1 J9BC
        try:
            input_value = self.ui.LineEdie_buy_input.text()
            is_checked = self.ui.checkBox_buy.isChecked()
            # is_checked = False
            print('第一次',input_value)
            print('第二次',self.ui.LineEdie_buy_input.text())
            print('进入买入',input_value,is_checked)

            if input_value:
                if is_checked:
                    # for i in range(100):
                    #     print('买入循环')
                    #
                    #     # to_value, real_value = self.J9BC_buyunitprice(input_value)
                    #     single_value = self.ui.LineEdit_buy_dis.text()
                    #     fake_value = float(single_value) * float(input_value)
                    #     print('买入', input_value, single_value, fake_value)
                    #     tran_url = 'https://www.j9bcrest.com/api/swap/trading-pair/transaction'
                    #     tran_data = {"fromToken": "USDT", "fromValue": fake_value, "slippageTolerance": 0.02,
                    #                  "toValue": input_value,
                    #                  "tradeCode": "J9BC_USDT"}
                    #     tran_res = requests.post(tran_url, json=tran_data, headers=self.new_h)
                    #     print('买入返回tran_res', tran_res.text)
                    #     time_str = time.strftime("%Y-%m-%d %H:%M:%S")
                    #     message = f'{time_str}单价:{single_value}---买入成功:{tran_res.json().get("data").get("message")}-买入设置价格+{str(single_value)}'
                    #     self.update_text(message)
                    #
                    #     with open('jiuyou.txt', 'a') as file:
                    #         file.writelines(message + '\n')
                    #
                    #     time.sleep(30)
                    # self.start_for()
                    self.timer_buy.start(25000)
                else:
                    # to_value, real_value = self.J9BC_buyunitprice(input_value)
                    single_value = self.ui.LineEdit_buy_dis.text()
                    fake_value = float(single_value) * float(input_value)
                    print('买入', input_value, single_value, fake_value)
                    tran_url = 'https://www.j9bcrest.com/api/swap/trading-pair/transaction'
                    tran_data = {"fromToken": "USDT", "fromValue": fake_value, "slippageTolerance": 0.02,
                                 "toValue": input_value,
                                 "tradeCode": "J9BC_USDT"}
                    tran_res = requests.post(tran_url, json=tran_data, headers=self.new_h)
                    print('买入返回tran_res', tran_res.text)
                    time_str = time.strftime("%Y-%m-%d %H:%M:%S")
                    message = f'{time_str}单价:{single_value}---买入成功:{tran_res.json().get("data").get("message")}-买入设置价格+{str(single_value)}'
                    self.update_text(message)

                    with open('jiuyou.txt', 'a') as file:
                        file.writelines(message + '\n')
            else:
                QMessageBox.information(self, "九游", "输入不能为空",
                                        QMessageBox.Yes)


        except Exception as e:
            QMessageBox.information(self, "九游", "稍后再试" + str(e),
                                    QMessageBox.Yes)





if __name__ == '__main__':
    # QMainWindow
    app = QApplication([])
    # app.setStyle('Fusion')  # 设置风格 'Fusion', 'Windows', 'WindowsVista'
    app.setWindowIcon(QIcon('icon.ico'))
    # palette = QPalette()  # 调色板
    # palette.setColor(QPalette.ButtonText, Qt.blue)
    # app.setPalette(palette)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    mainwindow = action_class(app)
    mainwindow.setWindowTitle("九游合约_v1.1")
    mainwindow.setWindowIcon(QIcon('icon.ico'))
    mainwindow.show()
    mainwindow.resize(1500,1000)
    sys.exit(app.exec_())
    # exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    # sys.exit(exit_code)
