import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QMessageboxDemo(QWidget):
    def __init__(self):
        super(QMessageboxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QMessageBox案例")

        self.resize(300,400)

        layout = QVBoxLayout()
        self.button1 = QPushButton('显示关于对话框')
        self.button1.clicked.connect(self.showdialog)
        #显示消息对话框
        self.button2 = QPushButton('显示消息对话框')
        self.button2.clicked.connect(self.showdialog)
        #警告
        self.button3 = QPushButton('显示警告对话框')
        self.button3.clicked.connect(self.showdialog)
        #错误对话框
        self.button4 = QPushButton('显示错误对话框')
        self.button4.clicked.connect(self.showdialog)

        #提问对话框
        self.button5 = QPushButton('显示提问对话框')
        self.button5.clicked.connect(self.showdialog)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        self.setLayout(layout)
    def showdialog(self):
        text = self.sender().text()

        if text == '显示关于对话框':
            #QMessageBox.about(self,'标题','内容')
            QMessageBox.about(self,'关于','这是一个关于对话框')
        elif text == '显示消息对话框':
            reply = QMessageBox.information(self,'消息','这是一个消息对话框',
            QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            print(reply)
        elif text == '显示警告对话框':
            QMessageBox.warning(self,'警告','这是警告对话框', QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        elif text == '显示错误对话框':
            QMessageBox.critical(self, '错误', '这是错误对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif text == '显示提问对话框':
            QMessageBox.critical(self, '提示', '这是提示对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


if __name__ == '__main__':
    app =QApplication(sys.argv)
    main = QMessageboxDemo()
    main.show()
    app.exit(app.exec_())
