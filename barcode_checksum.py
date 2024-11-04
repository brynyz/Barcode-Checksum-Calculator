from PySide6.QtWidgets import QMainWindow
from Ui_BarcodeCheckSum import Ui_MainWindow

class BarcodeChecksum(QMainWindow):
    def __init__(self):
        super(BarcodeChecksum, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Barcode Checksum Calculator")
        self.setFixedSize(400, 500)

        self.first_input = True
        self.first_calculate=False

        self.ui.pushButton.clicked.connect(self.push_show_solution)
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
        self.ui.pushButton_2.clicked.connect(self.push_back)


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
        self.ui.label.clear()
        self.ui.label_2.clear()
        self.ui.label_3.clear()
        self.ui.label_4.clear()
        self.ui.label_5.clear()
        self.ui.label_6.clear()
        self.ui.Label_Enter_Barcode.clear()
        self.ui.Label_Show_CheckDigit.setText("Check Digit")
        self.first_calculate = False

    def push_back(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def push_submit(self):
        text = self.ui.Label_Enter_Barcode.text()
        answer = ""
        if len(text)==12:
            checkdigit = "EAN Check digit:                  " + str(self.calculateEAN(text)) + "  "
            self.ui.Label_Show_CheckDigit.setText(checkdigit)
        elif len(text)==11:
            checkdigit = "UPC Check digit:                  " + str(self.calculateUPC(text)) + "  "
            self.ui.Label_Show_CheckDigit.setText(checkdigit)
        else:
            self.ui.Label_Show_CheckDigit.setText("Invalid: Enter 11(UPC) or 12(EAN) digits")

    def push_show_solution(self):
        if self.first_calculate:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.Label_Show_CheckDigit.setText("No solution yet")

    def sum_odd_position_digits(self, number):
        oddText = "Sum of Odd:  "
        num_str = str(number)
        total_sum = 0

        for index in range(len(num_str)):
            if index % 2 == 0:
                oddText += num_str[index]
                total_sum += int(num_str[index])
                if index < len(num_str) - 1:
                    oddText += "+"

        oddText += "= " + str(total_sum) + " -> " + str(total_sum%10)
        self.ui.label_2.setText(oddText)
        return total_sum

    def sum_even_position_digits(self, number):
        evenText = "Sum of Even:  "
        num_str = str(number)
        total_sum = 0

        for index in range(len(num_str)):
            if index % 2 == 1:
                evenText += num_str[index]
                total_sum += int(num_str[index])
                if index < len(num_str) - 1:
                    evenText += "+"

        evenText += "= " + str(total_sum) + " -> " + str(total_sum % 10)
        self.ui.label.setText(evenText)
        return total_sum

    def calculateEAN(self, number):
        self.first_calculate = True
        sumEven = self.sum_even_position_digits(number)
        sumOdd = self.sum_odd_position_digits(number)

        sumEvenOnes = abs(sumEven) % 10
        sumOddOnes = abs(sumOdd) % 10

        multiplyConstant = sumEvenOnes * 3
        self.ui.label_3.setText("Step 3:             " + str(sumEvenOnes) + " * 3 = " + str(multiplyConstant))
        multiplyConstantOnes = abs(multiplyConstant) % 10
        sumConstantProductOddOnes = multiplyConstantOnes + sumOddOnes
        self.ui.label_4.setText("Step 4:             " + str(multiplyConstantOnes) + str(sumEvenOnes) + " = " + str(sumConstantProductOddOnes)+ "  -> " + str(sumConstantProductOddOnes % 10))
        self.ui.label_5.setText("Step 5:             " + str(sumConstantProductOddOnes % 10) + " + " + str((10 - (sumConstantProductOddOnes % 10)) % 10) + " = 10"  + "  -> " + str((10 - (sumConstantProductOddOnes % 10)) % 10))
        self.ui.label_6.setText("The check digit now is:   " + str(10 - (sumConstantProductOddOnes % 10) % 10) + "\nFormat: EAN")

        if ((10 - (sumConstantProductOddOnes % 10)) % 10) == 0:
            self.ui.label_6.setText(
                "The check digit now is:    0" + "\nFormat: EAN")
            return 0
        else:
            self.ui.label_6.setText(
                "The check digit now is:   " + str(10 - (sumConstantProductOddOnes % 10) % 10) + "\nFormat: EAN")
            return (10 - (sumConstantProductOddOnes % 10)) % 10

    def calculateUPC(self, number):
        self.first_calculate = True
        sumEven = self.sum_even_position_digits(number)
        sumOdd = self.sum_odd_position_digits(number)

        sumEvenOnes = abs(sumEven) % 10
        sumOddOnes = abs(sumOdd) % 10

        multiplyConstant = sumOddOnes * 3
        multiplyConstantOnes = abs(multiplyConstant) % 10
        self.ui.label_3.setText(
            "Step 3:             " + str(sumOddOnes) + " * 3 = " + str(multiplyConstant) + "  -> " + str(multiplyConstantOnes))

        sumConstantProductEvenOnes = multiplyConstantOnes + sumEvenOnes
        self.ui.label_4.setText("Step 4:             " + str(multiplyConstantOnes) + " + " + str(sumEvenOnes) + " = " + str(sumConstantProductEvenOnes) + "  -> " + str(sumConstantProductEvenOnes % 10))
        self.ui.label_5.setText("Step 5:             " + str(sumConstantProductEvenOnes % 10) + " + " + str((10 - (sumConstantProductEvenOnes % 10)) % 10) + " = 10" + "  -> " + str((10 - (sumConstantProductEvenOnes % 10)) % 10))



        if ((10 - (sumConstantProductEvenOnes % 10)) % 10) == 0:
            self.ui.label_6.setText(
                "The check digit now is:    0" + "\nFormat: UPC")
            return 0
        else:
            self.ui.label_6.setText(
                "The check digit now is:   " + str(10 - (sumConstantProductEvenOnes % 10) % 10) + "\nFormat: UPC")
            return (10 - (sumConstantProductEvenOnes % 10)) % 10
