# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtGui import QKeyEvent, QPainter, QPolygon
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QTimer, Qt, QPoint
from datetime import datetime
from ui_form import Ui_MainWindow
import time

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

        #Declearing time variables
        self.hour = 0
        self.min = 0
        self.sec = 0
        self.total_time = 0
    
        #Switch to timer interface when the timer button is clicked.
        self.ui.timer.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))

        #Decrease/Increase time buttons
        self.ui.increaseHour.clicked.connect(self.increase_hour)
        self.ui.increaseMin.clicked.connect(self.increase_min)
        self.ui.increaseSec.clicked.connect(self.increase_sec)
        self.ui.decreaseHour.clicked.connect(self.decrease_hour)
        self.ui.decreaseMin.clicked.connect(self.decrease_min)
        self.ui.decreaseSec.clicked.connect(self.decrease_sec)

        #Start and stop timer buttons
        self.ui.startButton.clicked.connect(self.update_countdown)
        self.ui.stopButton.clicked.connect(lambda: self.countdown_timer.stop())
        self.ui.resetButton.clicked.connect(self.reset_timer)

        #Initialize a timer. It will take an amount of time to wait for,  as input from user.
        self.countdown_timer = QTimer()
        #Eachtime a second expires the timeout signal will be emitted and the  slot function will be called
        self.countdown_timer.timeout.connect(self.decrease_time)

#--------------------------------------------------------------------------------------------------#
#                                        STOPWATCH SETUP                                           #
#--------------------------------------------------------------------------------------------------#
        #Variables
        self.is_running = False
        self.has_stopped = False
        self.resetted = False
        #Stopwatch button to switch interface
        self.stopwatch_timer = QTimer()
        self.ui.stopwatch.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.start_stop.clicked.connect(self.start_stop_stopwatch)
        self.ui.reset.clicked.connect(self.reset_stopwatch)
        self.stopwatch_timer.timeout.connect(self.start_stop_stopwatch)
        self.ui.stopwatch_time.display("00:00:00:000")
    
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

    #Function linked to button to increase hours
    def increase_hour(self):
        self.hour += 1
        if self.hour > 23:
            self.hour = 0
        self.countdown_timer.stop()
        formatted_time = f"{self.hour:02}:{self.min:02}:{self.sec:02}"
        self.ui.timer_time.display(formatted_time)

    #Function linked to button to increase mins
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

    #Function linked to button to increase secs
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

    #Function linked to button to decrease hours
    def decrease_hour(self):
        self.hour -= 1
        if self.hour < 0:
            self.hour = 23
        self.countdown_timer.stop()
        formatted_time = f"{self.hour:02}:{self.min:02}:{self.sec:02}"
        self.ui.timer_time.display(formatted_time)

    #Function linked to button to decrease mins
    def decrease_min(self):
        self.min -= 1
        if self.min < 0:
            self.min = 59
            if self.hour < 0: 
                self.hour = 23
        self.countdown_timer.stop()
        formatted_time = f"{self.hour:02}:{self.min:02}:{self.sec:02}"
        self.ui.timer_time.display(formatted_time)

    #Function linked to button to decrease secs
    def decrease_sec(self):
        self.sec -= 1
        if self.sec < 0:
            self.sec = 59
        self.countdown_timer.stop()
        formatted_time = f"{self.hour:02}:{self.min:02}:{self.sec:02}"
        self.ui.timer_time.display(formatted_time)

    #Function to calculate total seconds and start timer.
    def update_countdown(self):
        self.total_time = (self.hour * 3600) + (self.min * 60) + self.sec
        if self.total_time > 0:
            self.countdown_timer.start(1000)
        else:
            self.ui.timer_time.display("00:00:00")

    #Function that decreases the amount of time until it reaches 0. 
    #It also shows the time in a formatted manner.
    def decrease_time(self):
        if self.total_time > 0:
            self.total_time -= 1
            hours = self.total_time // 3600
            minutes = (self.total_time % 3600) // 60
            seconds = self.total_time % 60
            formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.ui.timer_time.display(formatted_time)
        else:
            self.countdown_timer.stop()
            self.ui.timer_time.display("00:00:00")

    def reset_timer(self):
        self.hour = 0
        self.min = 0
        self.sec = 0
        self.countdown_timer.stop()
        self.ui.timer_time.display("00:00:00")
#----------------------------------------------------------------------------------------------------#
#                                           STOPWATCH FUNCTIONS                                      #
#----------------------------------------------------------------------------------------------------#

    def start_stop_stopwatch(self):
        #Set buttot text
        self.ui.start_stop.setText("⏸️")

        #Disconnect any existing connections
        self.ui.start_stop.clicked.disconnect()

        #If button is clicked again stop time.
        self.ui.start_stop.clicked.connect(self.stop_stopwatch)
        
        #Stopwatch time handling
        if not hasattr(self, 'start_time'):
            self.start_time = time.time()
        self.stopwatch_timer.start(1)

        elapsed_time = time.time() - self.start_time

        if self.has_stopped == True:
            if self.resetted == True:
                self.start_time = time.time()
                self.resetted = False
            else:
                self.start_time += time.time() - self.time_stopped
            self.has_stopped = False

        self.stopwatch_time_hour = int(elapsed_time // 3600)
        self.stopwatch_time_min = int((elapsed_time % 3600) // 60)
        self.stopwatch_time_sec = int(elapsed_time % 60)
        self.stopwatch_time_millisec = int((elapsed_time * 1000) % 1000)
        self.time_to_display = f"{self.stopwatch_time_hour:02}:{self.stopwatch_time_min:02}:{self.stopwatch_time_sec:02}:{self.stopwatch_time_millisec:03}"
        self.ui.stopwatch_time.display(self.time_to_display)
        
    def stop_stopwatch(self):

        self.has_stopped = True
        if self.has_stopped == True:
            self.time_stopped = time.time()
            
        #Set button text
        self.ui.start_stop.setText("▶️")

        self.ui.start_stop.clicked.disconnect()

        self.stopwatch_timer.stop()
        #If button is clicked again star time.
        self.ui.start_stop.clicked.connect(self.start_stop_stopwatch)

    def reset_stopwatch(self):
        self.ui.stopwatch_time.display("00:00:00:000")
        self.start_time = time.time()
        self.resetted = True 

#----------------------------------------------------------------------------------------------------# 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
