from PySide6.QtWidgets import QMainWindow
from Ui_BarcodeCheckSum import Ui_MainWindow

class BarcodeChecksum(QMainWindow):
    def __init__(self):
        super(BarcodeChecksum, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Barcode Checksum Calculator")
        self.setFixedSize(400,500)

        self.first_input = True

        self.ui.Push_0.clicked.connect(self.push_0)
        self.ui.Push_1.clicked.connect(self.push_1)
        self.ui.Push_2.clicked.connect(self.push_2)
        self.ui.Push_3.clicked.connect(self.push_3)
        self.ui.Push_4.clicked.connect(self.push_4)
        self.ui.Push_5.clicked.connect(self.push_5)
        self.ui.Push_6.clicked.connect(self.push_6)
        self.ui.Push_7.clicked.connect(self.push_7)
        self.ui.Push_8.clicked.connect(self.push_8)
        self.ui.Push_9.clicked.connect(self.push_9)

        self.ui.Push_Del.clicked.connect(self.push_del)
        self.ui.Push_Clear.clicked.connect(self.push_clear)
        self.ui.Push_Submit.clicked.connect(self.push_submit)


    def push_0(self):
        if self.first_input:
            self.ui.Label_Enter_Barcode.clear()
            self.first_input = False
        text = self.ui.Label_Enter_Barcode.text()
        self.ui.Label_Enter_Barcode.setText(text+"0")
    def push_1(self):
        if self.first_input:
            self.ui.Label_Enter_Barcode.clear()
            self.first_input = False
        text = self.ui.Label_Enter_Barcode.text()
        self.ui.Label_Enter_Barcode.setText(text+"1")
    def push_2(self):
        if self.first_input:
            self.ui.Label_Enter_Barcode.clear()
            self.first_input = False
        text = self.ui.Label_Enter_Barcode.text()
        self.ui.Label_Enter_Barcode.setText(text+"2")
    def push_3(self):
        if self.first_input:
            self.ui.Label_Enter_Barcode.clear()
            self.first_input = False
        text = self.ui.Label_Enter_Barcode.text()
        self.ui.Label_Enter_Barcode.setText(text+"3")
    def push_4(self):
        if self.first_input:
            self.ui.Label_Enter_Barcode.clear()
            self.first_input = False
        text = self.ui.Label_Enter_Barcode.text()
        self.ui.Label_Enter_Barcode.setText(text+"4")
    def push_5(self):
        if self.first_input:
            self.ui.Label_Enter_Barcode.clear()
            self.first_input = False
        text = self.ui.Label_Enter_Barcode.text()
        self.ui.Label_Enter_Barcode.setText(text+"5")
    def push_6(self):
        if self.first_input:
            self.ui.Label_Enter_Barcode.clear()
            self.first_input = False
        text = self.ui.Label_Enter_Barcode.text()
        self.ui.Label_Enter_Barcode.setText(text+"6")
    def push_7(self):
        if self.first_input:
            self.ui.Label_Enter_Barcode.clear()
            self.first_input = False
        text = self.ui.Label_Enter_Barcode.text()
        self.ui.Label_Enter_Barcode.setText(text+"7")
    def push_8(self):
        if self.first_input:
            self.ui.Label_Enter_Barcode.clear()
            self.first_input = False
        text = self.ui.Label_Enter_Barcode.text()
        self.ui.Label_Enter_Barcode.setText(text+"8")
    def push_9(self):
        if self.first_input:
            self.ui.Label_Enter_Barcode.clear()
            self.first_input = False
        text = self.ui.Label_Enter_Barcode.text()
        self.ui.Label_Enter_Barcode.setText(text+"9")

    def push_del(self):
        text = self.ui.Label_Enter_Barcode.text()
        self.ui.Label_Enter_Barcode.setText(text[:len(text)-1])

    def push_clear(self):
        self.ui.Label_Enter_Barcode.clear()

    def push_submit(self):
        text = self.ui.Label_Enter_Barcode.text()
        checkdigit = str(self.calculate(text))
        self.ui.Label_Show_CheckDigit.setText(checkdigit)

    def sum_odd_position_digits(self, number):
        num_str = str(number)
        total_sum = 0

        for index in range(len(num_str)):
            if index % 2 == 0:
                total_sum += int(num_str[index])

        return total_sum

    def sum_even_position_digits(self, number):
        num_str = str(number)
        total_sum = 0

        for index in range(len(num_str)):
            if index % 2 == 1:
                total_sum += int(num_str[index])

        return total_sum

    def calculate(self, number):
        sumEven = self.sum_even_position_digits(number)
        sumOdd = self.sum_odd_position_digits(number)

        sumEvenOnes = abs(sumEven) % 10
        sumOddOnes = abs(sumOdd) % 10
        multiplyConstant = sumEvenOnes * 3
        multiplyConstantOnes = abs(multiplyConstant) % 10
        sumConstantProductOddOnes = multiplyConstantOnes + sumOddOnes

        return (10 - (sumConstantProductOddOnes % 10)) % 10