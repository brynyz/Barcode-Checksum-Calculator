# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BarcodeCheckSum.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(688, 551)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"QMainWindow, QFrame, QLabel{\n"
"	background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.Calculator = QWidget()
        self.Calculator.setObjectName(u"Calculator")
        self.verticalLayout_3 = QVBoxLayout(self.Calculator)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.Push_4 = QPushButton(self.Calculator)
        self.Push_4.setObjectName(u"Push_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.Push_4.sizePolicy().hasHeightForWidth())
        self.Push_4.setSizePolicy(sizePolicy1)
        self.Push_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;\n"
"}")

        self.gridLayout.addWidget(self.Push_4, 5, 0, 1, 1)

        self.Push_3 = QPushButton(self.Calculator)
        self.Push_3.setObjectName(u"Push_3")
        sizePolicy1.setHeightForWidth(self.Push_3.sizePolicy().hasHeightForWidth())
        self.Push_3.setSizePolicy(sizePolicy1)
        self.Push_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;\n"
"}")

        self.gridLayout.addWidget(self.Push_3, 6, 2, 1, 1)

        self.Push_0 = QPushButton(self.Calculator)
        self.Push_0.setObjectName(u"Push_0")
        sizePolicy1.setHeightForWidth(self.Push_0.sizePolicy().hasHeightForWidth())
        self.Push_0.setSizePolicy(sizePolicy1)
        self.Push_0.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;\n"
"}")

        self.gridLayout.addWidget(self.Push_0, 7, 1, 1, 1)

        self.Push_Clear = QPushButton(self.Calculator)
        self.Push_Clear.setObjectName(u"Push_Clear")
        sizePolicy1.setHeightForWidth(self.Push_Clear.sizePolicy().hasHeightForWidth())
        self.Push_Clear.setSizePolicy(sizePolicy1)
        self.Push_Clear.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(186, 186, 0);\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(149, 149, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"	background-color: rgb(172, 172, 0);\n"
"}")

        self.gridLayout.addWidget(self.Push_Clear, 5, 3, 1, 1)

        self.Label_Enter_Barcode = QLabel(self.Calculator)
        self.Label_Enter_Barcode.setObjectName(u"Label_Enter_Barcode")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(14)
        sizePolicy2.setHeightForWidth(self.Label_Enter_Barcode.sizePolicy().hasHeightForWidth())
        self.Label_Enter_Barcode.setSizePolicy(sizePolicy2)
        self.Label_Enter_Barcode.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid #ffffff;")
        self.Label_Enter_Barcode.setTextFormat(Qt.PlainText)
        self.Label_Enter_Barcode.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Label_Enter_Barcode.setWordWrap(False)
        self.Label_Enter_Barcode.setMargin(6)

        self.gridLayout.addWidget(self.Label_Enter_Barcode, 0, 0, 1, 4)

        self.Push_8 = QPushButton(self.Calculator)
        self.Push_8.setObjectName(u"Push_8")
        sizePolicy1.setHeightForWidth(self.Push_8.sizePolicy().hasHeightForWidth())
        self.Push_8.setSizePolicy(sizePolicy1)
        self.Push_8.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;\n"
"}")

        self.gridLayout.addWidget(self.Push_8, 3, 1, 1, 1)

        self.Push_5 = QPushButton(self.Calculator)
        self.Push_5.setObjectName(u"Push_5")
        sizePolicy1.setHeightForWidth(self.Push_5.sizePolicy().hasHeightForWidth())
        self.Push_5.setSizePolicy(sizePolicy1)
        self.Push_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;\n"
"}")

        self.gridLayout.addWidget(self.Push_5, 5, 1, 1, 1)

        self.Push_Del = QPushButton(self.Calculator)
        self.Push_Del.setObjectName(u"Push_Del")
        sizePolicy1.setHeightForWidth(self.Push_Del.sizePolicy().hasHeightForWidth())
        self.Push_Del.setSizePolicy(sizePolicy1)
        self.Push_Del.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(186, 186, 0);\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(149, 149, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"	background-color: rgb(172, 172, 0);\n"
"}")

        self.gridLayout.addWidget(self.Push_Del, 3, 3, 1, 1)

        self.Push_6 = QPushButton(self.Calculator)
        self.Push_6.setObjectName(u"Push_6")
        sizePolicy1.setHeightForWidth(self.Push_6.sizePolicy().hasHeightForWidth())
        self.Push_6.setSizePolicy(sizePolicy1)
        self.Push_6.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;\n"
"}")

        self.gridLayout.addWidget(self.Push_6, 5, 2, 1, 1)

        self.Push_7 = QPushButton(self.Calculator)
        self.Push_7.setObjectName(u"Push_7")
        sizePolicy1.setHeightForWidth(self.Push_7.sizePolicy().hasHeightForWidth())
        self.Push_7.setSizePolicy(sizePolicy1)
        self.Push_7.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;\n"
"}")

        self.gridLayout.addWidget(self.Push_7, 3, 0, 1, 1)

        self.Push_2 = QPushButton(self.Calculator)
        self.Push_2.setObjectName(u"Push_2")
        sizePolicy1.setHeightForWidth(self.Push_2.sizePolicy().hasHeightForWidth())
        self.Push_2.setSizePolicy(sizePolicy1)
        self.Push_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;\n"
"}")

        self.gridLayout.addWidget(self.Push_2, 6, 1, 1, 1)

        self.Label_Show_CheckDigit = QLabel(self.Calculator)
        self.Label_Show_CheckDigit.setObjectName(u"Label_Show_CheckDigit")
        sizePolicy2.setHeightForWidth(self.Label_Show_CheckDigit.sizePolicy().hasHeightForWidth())
        self.Label_Show_CheckDigit.setSizePolicy(sizePolicy2)
        self.Label_Show_CheckDigit.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255)")
        self.Label_Show_CheckDigit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.Label_Show_CheckDigit, 1, 0, 1, 4)

        self.Push_9 = QPushButton(self.Calculator)
        self.Push_9.setObjectName(u"Push_9")
        sizePolicy1.setHeightForWidth(self.Push_9.sizePolicy().hasHeightForWidth())
        self.Push_9.setSizePolicy(sizePolicy1)
        self.Push_9.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;\n"
"}")

        self.gridLayout.addWidget(self.Push_9, 3, 2, 1, 1)

        self.Push_1 = QPushButton(self.Calculator)
        self.Push_1.setObjectName(u"Push_1")
        sizePolicy1.setHeightForWidth(self.Push_1.sizePolicy().hasHeightForWidth())
        self.Push_1.setSizePolicy(sizePolicy1)
        self.Push_1.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6ea4;\n"
"}")

        self.gridLayout.addWidget(self.Push_1, 6, 0, 1, 1)

        self.Push_Submit = QPushButton(self.Calculator)
        self.Push_Submit.setObjectName(u"Push_Submit")
        sizePolicy1.setHeightForWidth(self.Push_Submit.sizePolicy().hasHeightForWidth())
        self.Push_Submit.setSizePolicy(sizePolicy1)
        self.Push_Submit.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(186, 186, 0);\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(149, 149, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"	background-color: rgb(172, 172, 0);\n"
"}")

        self.gridLayout.addWidget(self.Push_Submit, 6, 3, 1, 1)

        self.pushButton = QPushButton(self.Calculator)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(186, 186, 0);\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 15px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(149, 149, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"	background-color: rgb(172, 172, 0);\n"
"}")

        self.gridLayout.addWidget(self.pushButton, 7, 2, 1, 2)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.Calculator)
        self.Solution = QWidget()
        self.Solution.setObjectName(u"Solution")
        self.Solution.setStyleSheet(u"QLabel{\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid #ffffff;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.Solution)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_2 = QPushButton(self.Solution)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QSize(60, 30))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(186, 186, 0);\n"
"    color: #ffffff;         \n"
"    font-size: 14px;        \n"
"    padding: 8px 16px;        \n"
"    border: none;          \n"
"    border-radius: 10px;     \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(149, 149, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"	background-color: rgb(172, 172, 0);\n"
"}")
        self.pushButton_2.setIconSize(QSize(24, 14))

        self.verticalLayout_5.addWidget(self.pushButton_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.Solution)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.Solution)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(self.Solution)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_4 = QLabel(self.Solution)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.Solution)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.Solution)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"border: none;")

        self.verticalLayout_4.addWidget(self.label_6)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.stackedWidget.addWidget(self.Solution)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Push_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.Push_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.Push_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.Push_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.Push_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.Push_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.Push_Clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Label_Enter_Barcode.setText(QCoreApplication.translate("MainWindow", u"Enter Barcode", None))
        self.Push_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.Push_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.Push_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.Push_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.Push_Del.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
#if QT_CONFIG(shortcut)
        self.Push_Del.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.Push_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.Push_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.Push_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.Push_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.Push_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.Push_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.Label_Show_CheckDigit.setText(QCoreApplication.translate("MainWindow", u"Check Digit", None))
        self.Push_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.Push_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.Push_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.Push_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.Push_Submit.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
#if QT_CONFIG(shortcut)
        self.Push_Submit.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Show Solution", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sum of Even Positions:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sum of Odd Positions:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Step 3", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Step 4", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Step 5", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Step 6", None))
    # retranslateUi