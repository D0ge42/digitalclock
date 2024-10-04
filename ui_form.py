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
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

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
        self.page_stopwatch = QWidget()
        self.page_stopwatch.setObjectName(u"page_stopwatch")
        self.stopwatch_time = QLCDNumber(self.page_stopwatch)
        self.stopwatch_time.setObjectName(u"stopwatch_time")
        self.stopwatch_time.setGeometry(QRect(70, 80, 500, 81))
        sizePolicy.setHeightForWidth(self.stopwatch_time.sizePolicy().hasHeightForWidth())
        self.stopwatch_time.setSizePolicy(sizePolicy)
        self.stopwatch_time.setMinimumSize(QSize(500, 0))
        self.stopwatch_time.setFont(font)
        self.stopwatch_time.setAutoFillBackground(False)
        self.stopwatch_time.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stopwatch_time.setFrameShape(QFrame.Box)
        self.stopwatch_time.setFrameShadow(QFrame.Plain)
        self.stopwatch_time.setLineWidth(0)
        self.stopwatch_time.setSmallDecimalPoint(False)
        self.stopwatch_time.setDigitCount(13)
        self.stopwatch_time.setSegmentStyle(QLCDNumber.Flat)
        self.stop = QPushButton(self.page_stopwatch)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(290, 10, 101, 41))
        self.stop.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stop.setStyleSheet(u"QPushButton {\n"
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
        self.resume = QPushButton(self.page_stopwatch)
        self.resume.setObjectName(u"resume")
        self.resume.setGeometry(QRect(430, 10, 101, 41))
        self.resume.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.resume.setStyleSheet(u"QPushButton {\n"
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
        self.reset = QPushButton(self.page_stopwatch)
        self.reset.setObjectName(u"reset")
        self.reset.setGeometry(QRect(130, 10, 101, 41))
        self.reset.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reset.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget.addWidget(self.page_stopwatch)
        self.page_timer = QWidget()
        self.page_timer.setObjectName(u"page_timer")
        self.timer_time = QLCDNumber(self.page_timer)
        self.timer_time.setObjectName(u"timer_time")
        self.timer_time.setGeometry(QRect(120, 50, 311, 81))
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
        self.startButton = QPushButton(self.page_timer)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(490, 20, 141, 41))
        font1 = QFont()
        font1.setFamilies([u"URW Gothic"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        self.startButton.setFont(font1)
        self.startButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.startButton.setStyleSheet(u"QPushButton {\n"
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
        self.increaseHour = QPushButton(self.page_timer)
        self.increaseHour.setObjectName(u"increaseHour")
        self.increaseHour.setGeometry(QRect(150, 30, 21, 26))
        self.increaseHour.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.increaseHour.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"    border: none;                /* No border */\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"   /* Same background color when pressed */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(191, 64, 64, 0); /* Optional hover color */\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;               /* No focus outline */\n"
"}\n"
"")
        self.increaseHour.setCheckable(False)
        self.increaseHour.setAutoDefault(False)
        self.increaseHour.setFlat(True)
        self.increaseMin = QPushButton(self.page_timer)
        self.increaseMin.setObjectName(u"increaseMin")
        self.increaseMin.setGeometry(QRect(265, 30, 21, 26))
        self.increaseMin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.increaseMin.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"    border: none;                /* No border */\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"   /* Same background color when pressed */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(191, 64, 64, 0); /* Optional hover color */\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;               /* No focus outline */\n"
"}\n"
"")
        self.increaseMin.setCheckable(False)
        self.increaseMin.setAutoDefault(False)
        self.increaseMin.setFlat(True)
        self.increaseSec = QPushButton(self.page_timer)
        self.increaseSec.setObjectName(u"increaseSec")
        self.increaseSec.setGeometry(QRect(375, 30, 21, 26))
        self.increaseSec.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.increaseSec.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"    border: none;                /* No border */\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"   /* Same background color when pressed */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(191, 64, 64, 0); /* Optional hover color */\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;               /* No focus outline */\n"
"}\n"
"")
        self.increaseSec.setCheckable(False)
        self.increaseSec.setAutoDefault(False)
        self.increaseSec.setFlat(True)
        self.decreaseSec = QPushButton(self.page_timer)
        self.decreaseSec.setObjectName(u"decreaseSec")
        self.decreaseSec.setGeometry(QRect(375, 125, 21, 26))
        self.decreaseSec.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.decreaseSec.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"    border: none;                /* No border */\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"   /* Same background color when pressed */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(191, 64, 64, 0); /* Optional hover color */\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;               /* No focus outline */\n"
"}\n"
"")
        self.decreaseSec.setCheckable(False)
        self.decreaseSec.setAutoDefault(False)
        self.decreaseSec.setFlat(True)
        self.decreaseHour = QPushButton(self.page_timer)
        self.decreaseHour.setObjectName(u"decreaseHour")
        self.decreaseHour.setGeometry(QRect(150, 125, 21, 26))
        self.decreaseHour.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.decreaseHour.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"    border: none;                /* No border */\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"   /* Same background color when pressed */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(191, 64, 64, 0); /* Optional hover color */\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;               /* No focus outline */\n"
"}\n"
"")
        self.decreaseHour.setCheckable(False)
        self.decreaseHour.setAutoDefault(False)
        self.decreaseHour.setFlat(True)
        self.decreaseMin = QPushButton(self.page_timer)
        self.decreaseMin.setObjectName(u"decreaseMin")
        self.decreaseMin.setGeometry(QRect(265, 125, 21, 26))
        self.decreaseMin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.decreaseMin.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"    border: none;                /* No border */\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"   /* Same background color when pressed */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(191, 64, 64, 0); /* Optional hover color */\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;               /* No focus outline */\n"
"}\n"
"")
        self.decreaseMin.setCheckable(False)
        self.decreaseMin.setAutoDefault(False)
        self.decreaseMin.setFlat(True)
        self.stopButton = QPushButton(self.page_timer)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(490, 70, 141, 41))
        self.stopButton.setFont(font1)
        self.stopButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stopButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(220, 138, 221);\n"
"	font: 600 11pt \"URW Gothic\";\n"
"    background-color: white; /* White background */\n"
"    color: #555; /* Dark text */\n"
"    border: 2px solid #555; /* Dark border */\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff4d4d; /* Dark background on hover */\n"
"    color: white; /* White text on hover */\n"
"}\n"
"")
        self.resetButton = QPushButton(self.page_timer)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(490, 120, 141, 41))
        self.resetButton.setFont(font1)
        self.resetButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.resetButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(220, 138, 221);\n"
"	font: 600 11pt \"URW Gothic\";\n"
"    background-color: white; /* White background */\n"
"    color: #555; /* Dark text */\n"
"    border: 2px solid #555; /* Dark border */\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #935dba; /* Dark background on hover */\n"
"    color: white; /* White text on hover */\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.page_timer)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.clock = QPushButton(self.verticalLayoutWidget)
        self.clock.setObjectName(u"clock")
        self.clock.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.timer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.stopwatch.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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

        self.stackedWidget.setCurrentIndex(1)
        self.increaseHour.setDefault(False)
        self.increaseMin.setDefault(False)
        self.increaseSec.setDefault(False)
        self.decreaseSec.setDefault(False)
        self.decreaseHour.setDefault(False)
        self.decreaseMin.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DogeClock", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"\u23f8\ufe0f", None))
        self.resume.setText(QCoreApplication.translate("MainWindow", u"\u25b6\ufe0f", None))
        self.reset.setText(QCoreApplication.translate("MainWindow", u"\u25c0\ufe0f", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.increaseHour.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
        self.increaseMin.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
        self.increaseSec.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
        self.decreaseSec.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.decreaseHour.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.decreaseMin.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.clock.setText(QCoreApplication.translate("MainWindow", u"Clock", None))
        self.timer.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stopwatch", None))
    # retranslateUi

