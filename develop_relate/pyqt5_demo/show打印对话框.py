import sys

from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *

"""
显示打印对话框
"""

class PrintDialog(QWidget):
    def __init__(self):
        super(PrintDialog, self).__init__()
        self.printer = QPrinter()
        self.initUi()

    def initUi(self):
        self.setGeometry(300,300,1200,800)
        self.setWindowTitle('打印对话框')
        self.editor = QTextEdit(self)
        self.setGeometry(20,20,300,270)

        self.openButton = QPushButton('打开文件',self)
        self.openButton.move(350,20)

        self.settignsButton = QPushButton('打印设置',self)
        self.settignsButton.move(350,50)

        self.printButton = QPushButton('打印文档',self)
        self.printButton.move(350,80)

        self.openButton.clicked.connect(self.openfile)
        self.settignsButton.clicked.connect(self.showsettingsDialog)
        self.printButton.clicked.connect(self.showprintDialog)
    # 打开文件
    def openfile(self):
        fname = QFileDialog.getOpenFileName(self,'打开文本文件','./')
        if fname[0]:
            with open(fname[0],'r',encoding='utf-8') as f:
                self.editor.setText(f.read())

    # 显示打印设置对话框
    def showsettingsDialog(self):
        printDialog = QPageSetupDialog(self.printer,self)
        printDialog.exec()

    # 显示打印对话框
    def showprintDialog(self):
        printDialog = QPrintDialog(self.printer,self)
        if QDialog.Accepted == printDialog.exec():
            self.editor.print(self.printer)



if __name__ == '__main__':
     app = QApplication(sys.argv)
     widget = PrintDialog()
     widget.show()
     app.exec_()
