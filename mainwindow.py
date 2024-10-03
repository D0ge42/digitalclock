# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtGui import QKeyEvent, QPainter, QPolygon
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QTimer, Qt, QPoint
from datetime import datetime
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

#--------------------------------------------------------------------------------------------------#
#                                CLOCK SETUP                                                       #
#--------------------------------------------------------------------------------------------------#
        #Initialize a clock, that starts on execute and update every second.
        self.clock = QTimer()
        self.clock.timeout.connect(self.set_clock_time)
        self.clock.start(1000)

        #Clock button event
        self.set_clock_time()
        self.ui.clock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
#-------------------------------------------------------------------------------------------------#
#                                  TIMER SETUP                                                    #
#-------------------------------------------------------------------------------------------------#

        #Set initial timer  display time
        self.ui.timer_time.display("00:00:00")

        #Switch to timer interface when the timer button is clicked.
        self.hour = 0
        self.min = 0
        self.sec = 0
        self.total_time = 0
        self.ui.timer.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.increaseHour.clicked.connect(self.increase_hour)
        self.ui.increaseMin.clicked.connect(self.increase_min)
        self.ui.increaseSec.clicked.connect(self.increase_sec)
        self.ui.decreaseHour.clicked.connect(self.decrease_hour)
        self.ui.decreaseMin.clicked.connect(self.decrease_min)
        self.ui.decreaseSec.clicked.connect(self.decrease_sec)
        self.ui.startButton.clicked.connect(self.update_countdown)
        self.ui.stopButton.clicked.connect(lambda: self.countdown_timer.stop())

        #Initialize a timer. It will take an amount of time to wait for,  as input from user.
        self.countdown_timer = QTimer()
        #Function to scale time
        self.countdown_timer.timeout.connect(self.decrease_time)

#--------------------------------------------------------------------------------------------------#
#                                         CLOCK FUNCTIONS                                          #
#--------------------------------------------------------------------------------------------------#
        #Function to display clock time.
    def set_clock_time(self): 
        now = datetime.now()
        formatted_time = f"{now.hour:02}:{now.minute:02}:{now.second:02}"
        self.ui.clock_time.display(formatted_time)  # Display total seconds
#----------------------------------------------------------------------------------------------------#
#                                          TIMER FUNCTIONS                                           #
#----------------------------------------------------------------------------------------------------#

    def increase_hour(self):
        self.hour += 1
        if self.hour > 23:
            self.hour = 0
        self.countdown_timer.stop()
        formatted_time = f"{self.hour:02}:{self.min:02}:{self.sec:02}"
        self.ui.timer_time.display(formatted_time)

    def increase_min(self):
        self.min += 1
        if self.min > 59:
            self.min = 0
            self.hour += 1
            if self.hour > 23:
                self.hour = 23
        self.countdown_timer.stop()
        formatted_time = f"{self.hour:02}:{self.min:02}:{self.sec:02}"
        self.ui.timer_time.display(formatted_time)

    def increase_sec(self):
        self.sec += 1
        if self.sec > 59:
            self.sec = 0
            self.min += 1
            if self.min > 59:
                self.min = 0
        self.countdown_timer.stop()
        formatted_time = f"{self.hour:02}:{self.min:02}:{self.sec:02}"
        self.ui.timer_time.display(formatted_time)
    
    def decrease_hour(self):
        self.hour -= 1
        if self.hour < 0:
            self.hour = 23
        self.countdown_timer.stop()
        formatted_time = f"{self.hour:02}:{self.min:02}:{self.sec:02}"
        self.ui.timer_time.display(formatted_time)

    def decrease_min(self):
        self.min -= 1
        if self.min < 0:
            self.min = 59
            self.hour -= 1
            if self.hour < 0:
                self.hour = 23
        self.countdown_timer.stop()
        formatted_time = f"{self.hour:02}:{self.min:02}:{self.sec:02}"
        self.ui.timer_time.display(formatted_time)

    def decrease_sec(self):
        self.sec -= 1
        if self.sec < 0:
            self.sec = 59
        self.countdown_timer.stop()
        formatted_time = f"{self.hour:02}:{self.min:02}:{self.sec:02}"
        self.ui.timer_time.display(formatted_time)

    def update_countdown(self):
        self.total_time = (self.hour * 3600) + (self.min * 60) + self.sec
        if self.total_time > 0:
            self.countdown_timer.start(1000)  # Start the countdown timer
        else:
            self.ui.timer_time.display("00:00:00")

    def decrease_time(self):
        if self.total_time > 0:
            self.total_time -= 1
            hours = self.total_time // 3600
            minutes = (self.total_time % 3600) // 60
            seconds = self.total_time % 60
            formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"  # Use updated values
            self.ui.timer_time.display(formatted_time)
        else:
            self.countdown_timer.stop()
            self.ui.timer_time.display("00:00:00")  # Show 00:00:00 when finished
#----------------------------------------------------------------------------------------------------#

 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
