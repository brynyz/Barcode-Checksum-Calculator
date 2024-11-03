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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(360, 487)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"QMainWindow, QFrame, QLabel{\n"
"	background-color: rgb(13, 13, 13);\n"
"}\n"
"\n"
"QPushButton {\n"
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
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.Push_9 = QPushButton(self.frame)
        self.Push_9.setObjectName(u"Push_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.Push_9.sizePolicy().hasHeightForWidth())
        self.Push_9.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.Push_9, 2, 2, 1, 1)

        self.Push_Del = QPushButton(self.frame)
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

        self.gridLayout.addWidget(self.Push_Del, 2, 3, 1, 1)

        self.Push_6 = QPushButton(self.frame)
        self.Push_6.setObjectName(u"Push_6")
        sizePolicy1.setHeightForWidth(self.Push_6.sizePolicy().hasHeightForWidth())
        self.Push_6.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.Push_6, 4, 2, 1, 1)

        self.Label_Show_CheckDigit = QLabel(self.frame)
        self.Label_Show_CheckDigit.setObjectName(u"Label_Show_CheckDigit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(14)
        sizePolicy2.setHeightForWidth(self.Label_Show_CheckDigit.sizePolicy().hasHeightForWidth())
        self.Label_Show_CheckDigit.setSizePolicy(sizePolicy2)
        self.Label_Show_CheckDigit.setStyleSheet(u"font: 700 28pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255)")
        self.Label_Show_CheckDigit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.Label_Show_CheckDigit, 1, 0, 1, 4)

        self.Push_7 = QPushButton(self.frame)
        self.Push_7.setObjectName(u"Push_7")
        sizePolicy1.setHeightForWidth(self.Push_7.sizePolicy().hasHeightForWidth())
        self.Push_7.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.Push_7, 2, 0, 1, 1)

        self.Push_8 = QPushButton(self.frame)
        self.Push_8.setObjectName(u"Push_8")
        sizePolicy1.setHeightForWidth(self.Push_8.sizePolicy().hasHeightForWidth())
        self.Push_8.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.Push_8, 2, 1, 1, 1)

        self.Label_Enter_Barcode = QLabel(self.frame)
        self.Label_Enter_Barcode.setObjectName(u"Label_Enter_Barcode")
        sizePolicy2.setHeightForWidth(self.Label_Enter_Barcode.sizePolicy().hasHeightForWidth())
        self.Label_Enter_Barcode.setSizePolicy(sizePolicy2)
        self.Label_Enter_Barcode.setStyleSheet(u"font: 700 28pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid #ffffff;")
        self.Label_Enter_Barcode.setTextFormat(Qt.PlainText)
        self.Label_Enter_Barcode.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Label_Enter_Barcode.setWordWrap(False)
        self.Label_Enter_Barcode.setMargin(6)

        self.gridLayout.addWidget(self.Label_Enter_Barcode, 0, 0, 1, 4)

        self.Push_0 = QPushButton(self.frame)
        self.Push_0.setObjectName(u"Push_0")
        sizePolicy1.setHeightForWidth(self.Push_0.sizePolicy().hasHeightForWidth())
        self.Push_0.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.Push_0, 6, 1, 1, 1)

        self.Push_3 = QPushButton(self.frame)
        self.Push_3.setObjectName(u"Push_3")
        sizePolicy1.setHeightForWidth(self.Push_3.sizePolicy().hasHeightForWidth())
        self.Push_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.Push_3, 5, 2, 1, 1)

        self.Push_2 = QPushButton(self.frame)
        self.Push_2.setObjectName(u"Push_2")
        sizePolicy1.setHeightForWidth(self.Push_2.sizePolicy().hasHeightForWidth())
        self.Push_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.Push_2, 5, 1, 1, 1)

        self.Push_4 = QPushButton(self.frame)
        self.Push_4.setObjectName(u"Push_4")
        sizePolicy1.setHeightForWidth(self.Push_4.sizePolicy().hasHeightForWidth())
        self.Push_4.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.Push_4, 4, 0, 1, 1)

        self.Push_5 = QPushButton(self.frame)
        self.Push_5.setObjectName(u"Push_5")
        sizePolicy1.setHeightForWidth(self.Push_5.sizePolicy().hasHeightForWidth())
        self.Push_5.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.Push_5, 4, 1, 1, 1)

        self.Push_1 = QPushButton(self.frame)
        self.Push_1.setObjectName(u"Push_1")
        sizePolicy1.setHeightForWidth(self.Push_1.sizePolicy().hasHeightForWidth())
        self.Push_1.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.Push_1, 5, 0, 1, 1)

        self.Push_Submit = QPushButton(self.frame)
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

        self.gridLayout.addWidget(self.Push_Submit, 5, 3, 2, 1)

        self.Push_Clear = QPushButton(self.frame)
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

        self.gridLayout.addWidget(self.Push_Clear, 4, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Push_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.Push_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.Push_Del.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
#if QT_CONFIG(shortcut)
        self.Push_Del.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.Push_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.Push_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.Label_Show_CheckDigit.setText(QCoreApplication.translate("MainWindow", u"Check Digit", None))
        self.Push_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.Push_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.Push_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.Push_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.Label_Enter_Barcode.setText(QCoreApplication.translate("MainWindow", u"Enter Barcode", None))
        self.Push_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.Push_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.Push_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.Push_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.Push_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.Push_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.Push_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.Push_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.Push_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.Push_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.Push_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.Push_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.Push_Submit.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
#if QT_CONFIG(shortcut)
        self.Push_Submit.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.Push_Clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

