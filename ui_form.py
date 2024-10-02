# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(714, 256)
        palette = QPalette()
        brush = QBrush(QColor(61, 56, 70, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QIcon()
        iconThemeName = u"computer"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"untitled1", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(61, 56, 70);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 704, 231))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.verticalLayoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_clock = QWidget()
        self.page_clock.setObjectName(u"page_clock")
        self.clock_time = QLCDNumber(self.page_clock)
        self.clock_time.setObjectName(u"clock_time")
        self.clock_time.setGeometry(QRect(-10, 10, 651, 151))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clock_time.sizePolicy().hasHeightForWidth())
        self.clock_time.setSizePolicy(sizePolicy)
        self.clock_time.setMinimumSize(QSize(500, 0))
        font = QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.clock_time.setFont(font)
        self.clock_time.setAutoFillBackground(False)
        self.clock_time.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.clock_time.setFrameShape(QFrame.Box)
        self.clock_time.setFrameShadow(QFrame.Plain)
        self.clock_time.setLineWidth(0)
        self.clock_time.setSmallDecimalPoint(False)
        self.clock_time.setDigitCount(8)
        self.clock_time.setSegmentStyle(QLCDNumber.Flat)
        self.stackedWidget.addWidget(self.page_clock)
        self.page_timer = QWidget()
        self.page_timer.setObjectName(u"page_timer")
        self.stopwatch_time = QLCDNumber(self.page_timer)
        self.stopwatch_time.setObjectName(u"stopwatch_time")
        self.stopwatch_time.setGeometry(QRect(10, 60, 700, 91))
        sizePolicy.setHeightForWidth(self.stopwatch_time.sizePolicy().hasHeightForWidth())
        self.stopwatch_time.setSizePolicy(sizePolicy)
        self.stopwatch_time.setMinimumSize(QSize(700, 0))
        self.stopwatch_time.setFont(font)
        self.stopwatch_time.setAutoFillBackground(False)
        self.stopwatch_time.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stopwatch_time.setFrameShape(QFrame.Box)
        self.stopwatch_time.setFrameShadow(QFrame.Plain)
        self.stopwatch_time.setLineWidth(0)
        self.stopwatch_time.setSmallDecimalPoint(False)
        self.stopwatch_time.setDigitCount(8)
        self.stopwatch_time.setSegmentStyle(QLCDNumber.Flat)
        self.stackedWidget.addWidget(self.page_timer)
        self.page_Stopwatch = QWidget()
        self.page_Stopwatch.setObjectName(u"page_Stopwatch")
        self.timer_time = QLCDNumber(self.page_Stopwatch)
        self.timer_time.setObjectName(u"timer_time")
        self.timer_time.setGeometry(QRect(120, 70, 311, 81))
        sizePolicy.setHeightForWidth(self.timer_time.sizePolicy().hasHeightForWidth())
        self.timer_time.setSizePolicy(sizePolicy)
        self.timer_time.setMinimumSize(QSize(300, 0))
        self.timer_time.setFont(font)
        self.timer_time.setAutoFillBackground(False)
        self.timer_time.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.timer_time.setFrameShape(QFrame.Box)
        self.timer_time.setFrameShadow(QFrame.Plain)
        self.timer_time.setLineWidth(0)
        self.timer_time.setSmallDecimalPoint(False)
        self.timer_time.setDigitCount(8)
        self.timer_time.setSegmentStyle(QLCDNumber.Flat)
        self.boxSec = QSpinBox(self.page_Stopwatch)
        self.boxSec.setObjectName(u"boxSec")
        self.boxSec.setGeometry(QRect(340, 20, 91, 27))
        font1 = QFont()
        font1.setFamilies([u"URW Gothic"])
        font1.setBold(True)
        self.boxSec.setFont(font1)
        self.boxSec.setWrapping(False)
        self.boxSec.setMaximum(59)
        self.boxHour = QSpinBox(self.page_Stopwatch)
        self.boxHour.setObjectName(u"boxHour")
        self.boxHour.setGeometry(QRect(120, 20, 91, 27))
        self.boxHour.setFont(font1)
        self.boxHour.setMaximum(23)
        self.boxMin = QSpinBox(self.page_Stopwatch)
        self.boxMin.setObjectName(u"boxMin")
        self.boxMin.setGeometry(QRect(230, 20, 91, 27))
        self.boxMin.setFont(font1)
        self.boxMin.setMaximum(59)
        self.timer_button = QPushButton(self.page_Stopwatch)
        self.timer_button.setObjectName(u"timer_button")
        self.timer_button.setGeometry(QRect(490, 60, 141, 41))
        font2 = QFont()
        font2.setFamilies([u"URW Gothic"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.timer_button.setFont(font2)
        self.timer_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(220, 138, 221);\n"
"	font: 600 11pt \"URW Gothic\";\n"
"    background-color: white; /* White background */\n"
"    color: #555; /* Dark text */\n"
"    border: 2px solid #555; /* Dark border */\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #88db14; /* Dark background on hover */\n"
"    color: white; /* White text on hover */\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.page_Stopwatch)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.clock = QPushButton(self.verticalLayoutWidget)
        self.clock.setObjectName(u"clock")
        self.clock.setStyleSheet(u"QPushButton {\n"
"	color: rgb(220, 138, 221);\n"
"	font: 600 11pt \"URW Gothic\";\n"
"    background-color: white; /* White background */\n"
"    color: #555; /* Dark text */\n"
"    border: 2px solid #555; /* Dark border */\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #555; /* Dark background on hover */\n"
"    color: white; /* White text on hover */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.clock)

        self.timer = QPushButton(self.verticalLayoutWidget)
        self.timer.setObjectName(u"timer")
        self.timer.setStyleSheet(u"QPushButton {\n"
"	font: 600 11pt \"URW Gothic\";\n"
"    background-color: white; /* White background */\n"
"    color: #555; /* Dark text */\n"
"    border: 2px solid #555; /* Dark border */\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #555; /* Dark background on hover */\n"
"    color: white; /* White text on hover */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.timer)

        self.stopwatch = QPushButton(self.verticalLayoutWidget)
        self.stopwatch.setObjectName(u"stopwatch")
        self.stopwatch.setStyleSheet(u"QPushButton {\n"
"	color: rgb(220, 138, 221);\n"
"	font: 600 11pt \"URW Gothic\";\n"
"    background-color: white; /* White background */\n"
"    color: #555; /* Dark text */\n"
"    border: 2px solid #555; /* Dark border */\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #555; /* Dark background on hover */\n"
"    color: white; /* White text on hover */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.stopwatch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DogeClock", None))
        self.timer_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.clock.setText(QCoreApplication.translate("MainWindow", u"Clock", None))
        self.timer.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stopwatch", None))
    # retranslateUi

