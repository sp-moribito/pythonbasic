import sys
import pyupbit
from PyQt5.QtWidgets import *
from PyQt5 import uic
 
form_class = uic.loadUiType("mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)
        self.pushButton_2.clicked.connect(self.rule)

    def inquiry(self):
        price1=pyupbit.get_current_price("KRW-BTC")
        self.lineEdit.setText(str(price1)) 
    def rule(self):
        price2=pyupbit.get_current_price("KRW-XRP")
        self.lineEdit_2.setText(str(price2)) 
        print("버튼2 클릭")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()