import json
import requests
import jiuyou
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

        self.ui = jiuyou.Ui_MainWindow()
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


from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

# import sys
#
# if __name__ == '__main__':
#     appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
#     window = QMainWindow()
#     window.resize(1000, 800)
#     window.show()
#     exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
#     sys.exit(exit_code)

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    appctxt = ApplicationContext()
    mainwindow = action_class()
    mainwindow.setWindowTitle("九游合约_v1.1")
    mainwindow.show()
    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
    import fbs