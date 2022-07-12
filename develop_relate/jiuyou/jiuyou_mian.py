import json
import requests
# import jiuyou
from PyQt5.QtWidgets import QWidget,QDialog,QMainWindow,QApplication
import sys

auth_data = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJIWDFqOXRhb2xvdjEzMTQiLCJib2R5Ijp7ImNvdW50cnlDb2RlIjoiKzg2IiwibWVyY2hhbnQiOiJIWDEiLCJvcmlnaW4iOiIyMjIuMjA5LjIwOC4xNjYiLCJyZWdEZXZpY2UiOiJtb2JpbGUiLCJyZWdIb3N0IjoiMTI3LjAuMC4xIiwicmVnSXAiOiIxMjcuMC4wLjEiLCJzdGF0ZSI6Ik5PUk1BTCIsInVzZXJuYW1lIjoiSFgxajl0YW9sb3YxMzE0In0sImJvZHlDbGFzcyI6ImNvbS5wZy5sb2JieS5qOWJjLmF1dGguc2hpcm8uU2hpcm9Vc2VyIiwiZXhwIjoxNjU3NjI4ODcxNjgwLCJpYXQiOjE2NTc2MjUyNzE2ODAsImp0aSI6ImNhZWE3OTgwLTMzYjItNDM5My1iZDZlLTIwZWFiNDhhYmE3MyIsIm5iZiI6MTY1NzYyNTI3MTY4MH0.lza0XhdQKWNMA32_onNp7VcalMBofrYVl-dP5D93KbU'
wallet_url = 'https://j9bcrest.com/api/customer/wallet'
to_url = 'https://j9bcrest.com/api/swap/open/calc/to'
tran_url = 'https://j9bcrest.com/api/swap/trading-pair/transaction'
#https://j9con.com/

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


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.lineEdit_wbesite.setGeometry(QtCore.QRect(70, 50, 231, 20))
        self.lineEdit_wbesite.setObjectName("lineEdit_wbesite")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(570, 50, 75, 23))
        self.pushButton_start.setObjectName("pushButton_start")

        self.pushButton_balance = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_balance.setGeometry(QtCore.QRect(650, 50, 50, 23))
        self.pushButton_balance.setObjectName("pushButton_balance")

        self.textEdit_payloadtoken = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_payloadtoken.setGeometry(QtCore.QRect(70, 140, 231, 141))
        self.textEdit_payloadtoken.setObjectName("textEdit_payloadtoken")
        self.textEdit_payloadtoken.setFontFamily('黑体')
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 61, 21))
        self.label_2.setObjectName("label_2")
        self.textEdit_response_display = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_response_display.setGeometry(QtCore.QRect(420, 120, 341, 391))
        self.textEdit_response_display.setObjectName("textEdit_response_display")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 290, 401, 131))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_USDI_input = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_USDI_input.setGeometry(QtCore.QRect(50, 30, 101, 21))
        self.lineEdit_USDI_input.setObjectName("lineEdit_USDI_input")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(230, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_J9BC_display = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_J9BC_display.setGeometry(QtCore.QRect(270, 30, 121, 21))
        self.lineEdit_J9BC_display.setObjectName("lineEdit_J9BC_display")
        self.buy_button = QtWidgets.QPushButton(self.groupBox)
        self.buy_button.setGeometry(QtCore.QRect(170, 80, 51, 23))
        self.buy_button.setObjectName("buy_button")
        self.pushButton_sure_1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_sure_1.setGeometry(QtCore.QRect(170, 30, 51, 23))
        self.pushButton_sure_1.setObjectName("pushButton_sure_1")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 430, 401, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_J9BC_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_J9BC_input.setGeometry(QtCore.QRect(50, 30, 101, 21))
        self.lineEdit_J9BC_input.setText("")
        self.lineEdit_J9BC_input.setObjectName("lineEdit_J9BC_input")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(230, 30, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_USDT_display = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_USDT_display.setGeometry(QtCore.QRect(270, 30, 131, 21))
        self.lineEdit_USDT_display.setObjectName("lineEdit_USDT_display")
        self.pushButton_sell = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_sell.setGeometry(QtCore.QRect(170, 80, 51, 23))
        self.pushButton_sell.setObjectName("pushButton_sell")
        self.pushButton_sure_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_sure_2.setGeometry(QtCore.QRect(170, 30, 51, 23))
        self.pushButton_sure_2.setObjectName("pushButton_sure_2")
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
        self.pushButton_sure_1.clicked.connect(MainWindow.USDT_to_value)
        self.pushButton_sure_2.clicked.connect(MainWindow.J9BC_to_value)
        self.buy_button.clicked.connect(MainWindow.USDT_J9BC)
        self.pushButton_sell.clicked.connect(MainWindow.J9BC_USDT)
        self.pushButton_balance.clicked.connect(MainWindow.keep_wallet)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "访问网址："))
        self.lineEdit_wbesite.setText(_translate("MainWindow", "https://j9con.com/swap"))
        self.pushButton_start.setText(_translate("MainWindow", "开始"))
        self.pushButton_balance.setText(_translate("MainWindow", "余额"))
        self.label_2.setText(_translate("MainWindow", "请求数据："))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_3.setText(_translate("MainWindow", "USDT："))
        self.label_4.setText(_translate("MainWindow", "J9BC："))
        self.buy_button.setText(_translate("MainWindow", "买入"))
        self.pushButton_sure_1.setText(_translate("MainWindow", "确定=>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_6.setText(_translate("MainWindow", "J9BC："))
        self.label_7.setText(_translate("MainWindow", "USDT："))
        self.pushButton_sell.setText(_translate("MainWindow", "卖出"))
        self.pushButton_sure_2.setText(_translate("MainWindow", "确定=>"))



class action_class(QMainWindow):
    def __init__(self,parent=None):
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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 初始化窗口

    def USDT_J9BC(self):
        value = self.ui.lineEdit_USDI_input.text()
        to_value = self.ui.lineEdit_J9BC_display.text()
        tran_url = 'https://j9bcrest.com/api/swap/trading-pair/transaction'
        # to_data = {
        #     'token':'USDT',
        #     'value':value,
        #     'tradeCode':'J9BC_USDT',
        # }
        # print('买入',to_data)
        # wall_res = requests.get(wallet_url,headers=new_h)
        # print('wall_res:',wall_res.text)
        # to_res = requests.post(to_url,headers=new_h,json=to_data)
        # to_value = to_res.json().get('data').get('value')
        # print('to_res:',to_res.text,to_value)
        tran_data = {"fromToken": "USDT", "fromValue": value, "slippageTolerance": 0.02, "toValue":to_value,
                     "tradeCode": "J9BC_USDT"}
        tran_res = requests.post(tran_url,json=tran_data,headers=self.new_h)
        message = f'买入成功:{tran_res.json().get("data").get("message")}'
        print('usdt买入成功',message)
        self.ui.textEdit_response_display.append(message)
        print('tran_res:',tran_res.text)

    def J9BC_USDT(self,value):
        # try:
        # to_data = {
        #     'token': 'J9BC',
        #     'value': value,
        #     'tradeCode': 'J9BC_USDT',
        # }
        # wall_res = requests.get(wallet_url, headers=new_h)
        # print('wall_res:', wall_res.text)
        # to_res = requests.post(to_url, headers=new_h, json=to_data)
        # to_value = to_res.json().get('data').get('value')
        # print('to_res:', to_res.text, to_value)
        value = self.ui.lineEdit_J9BC_input.text()
        to_value = self.ui.lineEdit_USDT_display.text()
        tran_url = 'https://j9bcrest.com/api/swap/trading-pair/transaction'
        tran_data = {"fromToken":"J9BC","fromValue":value,"slippageTolerance":0.02,"toValue":to_value,"tradeCode":"J9BC_USDT"}
        tran_res = requests.post(tran_url, json=tran_data, headers=self.new_h)
        print('tran_res:', tran_res.text)
        message = f'卖出成功:{tran_res.json().get("data").get("message")}'
        self.ui.textEdit_response_display.append(message)
        print('tran_res:', tran_res.text)
        # except Exception as e:
        #     print('请稍后再试')

    def keep_wallet(self):
        wallet_url = 'https://j9bcrest.com/api/customer/wallet'
        auth_d = self.ui.textEdit_payloadtoken.toPlainText()
        # new_h = self.new_h
        # new_h['authorization'] = auth_d
        self.new_h['authorization'] = auth_d
        wall_res = requests.get(wallet_url, headers=self.new_h)
        res_data = wall_res.json()
        # print('余额',wall_res.json())
        if not res_data.get('code'):
            balance = res_data.get('data')
            display_str = f'余额: USDT:{balance.get("USDT")}  J9BC:{balance.get("J9BC")}'
            print(f'余额: USDT:{balance.get("USDT")}  J9BC:{balance.get("J9BC")}')
            self.ui.textEdit_response_display.append(display_str)
            return f'余额: USDT:{balance.get("USDT")}  J9BC:{balance.get("J9BC")}'
        else:
            display_str = f'错误:{res_data.get("message")}'
            print(f'错误:{res_data.get("message")}')
            self.ui.textEdit_response_display.append(display_str)
            return f'错误:{res_data.get("message")}'
    def USDT_to_value(self):
        to_url = 'https://j9bcrest.com/api/swap/open/calc/to'
        # token: J9BC, USDT
        value = self.ui.lineEdit_USDI_input.text()
        to_data = {
            'token': 'USDT',
            'value': value,
            'tradeCode': 'J9BC_USDT',
        }
        print('转换u',to_data)
        to_res = requests.post(to_url, headers=self.new_h, json=to_data)
        to_value = to_res.json().get('data').get('value')
        print('to_res:', to_res.text, to_value)
        self.ui.lineEdit_J9BC_display.setText(str(to_value))
        return value,to_value

    def J9BC_to_value(self):
        to_url = 'https://j9bcrest.com/api/swap/open/calc/to'
        # token: J9BC, USDT
        value = self.ui.lineEdit_J9BC_input.text()
        to_data = {
            'token': 'J9BC',
            'value': value,
            'tradeCode': 'J9BC_USDT',
        }
        print('转换J',to_data)
        to_res = requests.post(to_url, headers=self.new_h, json=to_data)
        to_value = to_res.json().get('data').get('value')
        print('to_res:', to_res.text, to_value)
        self.ui.lineEdit_USDT_display.setText(str(to_value))
        return value, to_value

def init_window():
    action_obj = action_class()
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = jiuyou.Ui_MainWindow()
    ui.setupUi(mainwindow,action_obj)  # 初始化窗口
    mainwindow.setWindowTitle("九游合约_v1.1"
                              "")
    mainwindow.show()
    sys.exit(app.exec_())

def main():
    init_window()


def keep_wallet():
    wall_res = requests.get(wallet_url, headers=new_h)
    res_data = wall_res.json()
    # print('余额',wall_res.json())
    if not res_data.get('code'):
        balance = res_data.get('data')
        print(f'余额: USDT:{balance.get("USDT")}  J9BC:{balance.get("J9BC")}')
        return f'余额: USDT:{balance.get("USDT")}  J9BC:{balance.get("J9BC")}'
    else:
        print(f'错误:{res_data.get("message")}')
        return f'错误:{res_data.get("message")}'
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # mainwindow = QMainWindow()
    # mainwindow.setWindowTitle("九游合约_v1.1")
    mainwindow = action_class()
    mainwindow.setWindowTitle("九游合约_v1.1")
    mainwindow.show()
    sys.exit(app.exec_())