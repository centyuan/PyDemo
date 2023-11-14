import json
import time
import requests
from PyQt5.QtCore import QTimer, Qt,QThread,pyqtSignal
from PyQt5.QtGui import QPalette, QIcon
from PyQt5.QtWidgets import QWidget, QDialog, QMainWindow, QApplication,QMessageBox
import sys
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


    def __init__(self,maindow):
        super(MyThread, self).__init__()
        self.maindow = maindow

    def run(self):
        while True:
            for idx in range(100):
                print('run',idx)
                self.send_signal.emit(str(idx))
                time.sleep(1)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 61, 20))
        self.label.setObjectName("label")
        self.lineEdit_wbesite = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_wbesite.setGeometry(QtCore.QRect(70, 50, 171, 20))
        self.lineEdit_wbesite.setObjectName("lineEdit_wbesite")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(700, 50, 75, 23))
        self.pushButton_start.setObjectName("pushButton_start")
        self.textEdit_payloadtoken = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_payloadtoken.setGeometry(QtCore.QRect(70, 100, 231, 181))
        self.textEdit_payloadtoken.setAcceptRichText(False)
        self.textEdit_payloadtoken.setObjectName("textEdit_payloadtoken")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.label_2.setObjectName("label_2")
        self.textEdit_response_display = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_response_display.setGeometry(QtCore.QRect(420, 120, 341, 391))
        self.textEdit_response_display.setObjectName("textEdit_response_display")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 290, 401, 131))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_USDI_input = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_USDI_input.setGeometry(QtCore.QRect(90, 31, 111, 21))
        self.lineEdit_USDI_input.setObjectName("lineEdit_USDI_input")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(230, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_J9BC_display = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_J9BC_display.setGeometry(QtCore.QRect(270, 30, 121, 21))
        self.lineEdit_J9BC_display.setObjectName("lineEdit_J9BC_display")
        self.buy_button = QtWidgets.QPushButton(self.groupBox)
        self.buy_button.setGeometry(QtCore.QRect(340, 80, 51, 23))
        self.buy_button.setObjectName("buy_button")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 430, 401, 131))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_J9BC_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_J9BC_input.setGeometry(QtCore.QRect(90, 30, 111, 21))
        self.lineEdit_J9BC_input.setText("")
        self.lineEdit_J9BC_input.setObjectName("lineEdit_J9BC_input")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(230, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_USDT_display = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_USDT_display.setGeometry(QtCore.QRect(270, 30, 121, 21))
        self.lineEdit_USDT_display.setObjectName("lineEdit_USDT_display")
        self.pushButton_sell = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_sell.setGeometry(QtCore.QRect(340, 80, 51, 23))
        self.pushButton_sell.setObjectName("pushButton_sell")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit_balance_price = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_balance_price.setGeometry(QtCore.QRect(270, 50, 411, 21))
        self.lineEdit_balance_price.setText("")
        self.lineEdit_balance_price.setObjectName("lineEdit_balance_price")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_start.clicked.connect(MainWindow.keep_wallet)
        self.buy_button.clicked.connect(MainWindow.J9BC_in)
        self.pushButton_sell.clicked.connect(MainWindow.J9BC_out)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "访问网址："))
        self.label.adjustSize()
        self.lineEdit_wbesite.setText(_translate("MainWindow", "https://j9con.com/swap"))
        self.lineEdit_wbesite.adjustSize()
        self.pushButton_start.setText(_translate("MainWindow", "开始"))
        self.label_2.setText(_translate("MainWindow", "请求数据："))
        self.label_2.adjustSize()
        self.label_4.setText(_translate("MainWindow", "单笔："))
        self.lineEdit_J9BC_display.setToolTip(_translate("MainWindow", "<html><head/><body><p>买入</p></body></html>"))
        self.buy_button.setText(_translate("MainWindow", "买入"))
        self.checkBox.setText(_translate("MainWindow", "买入,阈值"))
        self.checkBox.adjustSize()
        self.groupBox_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>卖出</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "单笔："))
        self.pushButton_sell.setText(_translate("MainWindow", "卖出"))
        self.checkBox_2.setText(_translate("MainWindow", "卖出,阈值"))
        self.checkBox_2.adjustSize()

class action_class(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.auth_data = ''
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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 初始化窗口
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_keep)
        self.my_thread = MyThread(self)

    def strat_for(self):
        self.my_thread.send_signal.connect(self.update_view)  # 重点代码2
        self.my_thread.start()
    def while_tran(self,data):
        pass


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

                self.ui.lineEdit_USDI_input.setText(str(dis_value_1))
                self.ui.lineEdit_J9BC_input.setText(str(dis_value_2))
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

                self.ui.lineEdit_USDI_input.setText(str(dis_value_1))
                self.ui.lineEdit_J9BC_input.setText(str(dis_value_2))
            else:
                QMessageBox.information(self, "九游", "输入不能为空",
                                        QMessageBox.Yes)
            self.timer.start(10000)
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
            v = self.ui.lineEdit_USDT_display.text()
            if v:
                value, to_value = self.J9BC_sellunitprice(v)
                # print('卖出', value, to_value)
                tran_url = 'https://www.j9bcrest.com/api/swap/trading-pair/transaction'
                tran_data = {"fromToken": "J9BC", "fromValue": value, "slippageTolerance": 0.02, "toValue": to_value,
                             "tradeCode": "J9BC_USDT"}
                tran_res = requests.post(tran_url, json=tran_data, headers=self.new_h)
                # print('tran_res:', tran_res.text)
                time_str = time.strftime("%Y-%m-%d %H:%M:%S")
                message = f'{time_str}卖出成功:{tran_res.json().get("data").get("message")}'
                self.ui.textEdit_response_display.setStyleSheet("color:green")
                self.ui.textEdit_response_display.append(message)
                self.ui.lineEdit_USDT_display.clear()
                # print('tran_res:', tran_res.text)
                with open('jiuyou.txt','a') as file:
                    file.writelines(message+'\n')
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
            v = self.ui.lineEdit_J9BC_display.text()
            if v:
                to_value, value = self.J9BC_buyunitprice(v)
                # print('买入', to_value, value)
                tran_url = 'https://www.j9bcrest.com/api/swap/trading-pair/transaction'
                tran_data = {"fromToken": "USDT", "fromValue": value, "slippageTolerance": 0.02, "toValue": to_value,
                             "tradeCode": "J9BC_USDT"}
                tran_res = requests.post(tran_url, json=tran_data, headers=self.new_h)
                time_str = time.strftime("%Y-%m-%d %H:%M:%S")
                message = f'{time_str}买入成功:{tran_res.json().get("data").get("message")}'

                # print('usdt买入成功', message)
                self.ui.textEdit_response_display.setStyleSheet("color:green")
                self.ui.textEdit_response_display.append(message)
                self.ui.lineEdit_J9BC_display.clear()
                # print('tran_res:', tran_res.text)
                with open('jiuyou.txt','a') as file:
                    file.writelines(message+'\n')
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
    mainwindow = action_class()
    mainwindow.setWindowTitle("九游合约_v1.1")
    mainwindow.setWindowIcon(QIcon('icon.ico'))
    mainwindow.show()
    mainwindow.resize(800,600)
    sys.exit(app.exec_())
    # exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    # sys.exit(exit_code)
