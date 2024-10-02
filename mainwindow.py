# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QTimer
from datetime import datetime

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
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
        self.ui.timer.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.timer_button.clicked.connect(self.set_timer_start)

        #Initialize a timer. It will take an amount of time to wait for,  as input from user.
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.time_scale)

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


    #Function to set starting time of timer from spinboxes to lcd display.
    def set_timer_start(self):
        hour = self.ui.boxHour.value()
        min = self.ui.boxMin.value()
        sec = self.ui.boxSec.value()

        self.remaining_time = (hour * 3600) + (min * 60) + sec

        formatted_time = f"{hour:02}:{min:02}:{sec:02}"
        self.ui.timer_time.display(formatted_time)

        if self.remaining_time > 0:
            self.countdown_timer.start(1000)

    #Function that decreases the time until it reaches 0. It also format the time so display it on the lcd. 
    def time_scale(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
        hours = self.remaining_time // 3600
        minutes = (self.remaining_time % 3600) // 60
        sec = (self.remaining_time % 60)

        formatted_time = f"{hours:02}:{minutes:02}:{sec:02}"
        self.ui.timer_time.display(formatted_time)

#----------------------------------------------------------------------------------------------------#

 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
