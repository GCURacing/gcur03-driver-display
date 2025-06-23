from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QTimer, QPropertyAnimation)
from PyQt5 import QtCore
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainterPath, QPen, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
import time
import pandas as pd
import sys, os, vlc

oilTemp = 90
oilPress = 40
coolantTemp = 75
rpm = 4000
speed = 0
minutesRT = 0
secondsRT = 0


class SplashVideo(QWidget):
    def __init__(self, on_finished):
        super().__init__()

        self.resize(800, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QSize(800, 480))
        self.setBaseSize(QSize(800, 480))
        self.setStyleSheet(u"background-color: rgb(26, 31, 87)")
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint | 
            QtCore.Qt.WindowStaysOnTopHint
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        self.video_frame = QWidget(self)
        self.video_frame.setStyleSheet("border: none; background-color: rgb(26, 31, 87);")
        layout.addWidget(self.video_frame)
        self.video_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Setup VLC instance and player
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        video_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "media", "Intro.mp4")
        media = self.instance.media_new(video_path)
        self.player.set_media(media)

        # Embed video in widget (platform-specific)
        if sys.platform.startswith("linux"):
            self.player.set_xwindow(self.video_frame.winId())
        elif sys.platform == "win32":
            self.player.set_hwnd(self.video_frame.winId())
        elif sys.platform == "darwin":
            self.player.set_nsobject(int(self.video_frame.winId()))

        # Connect finished handler
        self.on_finished = on_finished
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(1)

        self.show()
        self.player.play()

        # Start timer to monitor playback
        self.check_timer = QTimer(self)
        self.check_timer.timeout.connect(self.check_finished)
        self.check_timer.start(500)

    def check_finished(self):
        if self.player.get_state() == vlc.State.Ended:
            self.check_timer.stop()
            self.fade_out()

    def fade_out(self):
        self.anim = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.anim.setDuration(1000)
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        self.anim.finished.connect(self.finish)
        self.anim.start()

    def finish(self):
        self.on_finished()
        self.close()

class OutlinedLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setFont(QFont("Arial", 40, QFont.Bold))
        self.setAlignment(Qt.AlignCenter)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Create path from text
        path = QPainterPath()
        font = self.font()
        metrics = self.fontMetrics()
        rect = self.rect()
        text = self.text()

        # Center the text
        x = rect.width()/2 - metrics.horizontalAdvance(text)/2
        y = rect.height()/2 + metrics.ascent()/2 - 4
        path.addText(x, y, font, text)

        # Draw outline
        pen = QPen(QColor("black"), 2)  # Border thickness here
        painter.setPen(pen)
        painter.drawPath(path)

        # Draw fill
        painter.fillPath(path, Qt.white)  # Proper fill

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        
        # count variable
        self.count = 0
 
        # start flag
        self.start = False
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(800, 480))
        MainWindow.setBaseSize(QSize(800, 480))
        MainWindow.setStyleSheet(u"background-color: rgb(26, 31, 87)")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setWindowFlags(
            MainWindow.windowFlags() | 
            QtCore.Qt.FramelessWindowHint | 
            QtCore.Qt.WindowStaysOnTopHint
        )
        self.DriverDisplay = QWidget(MainWindow)
        self.DriverDisplay.setObjectName(u"DriverDisplay")
        self.gearContainer = QFrame(self.DriverDisplay)
        self.gearContainer.setObjectName(u"gearContainer")
        self.gearContainer.setGeometry(QRect(310, 80, 181, 241))
        self.gearContainer.setStyleSheet(u"border-width: 2px")
        self.gearContainer.setFrameShape(QFrame.StyledPanel)
        self.gearContainer.setFrameShadow(QFrame.Plain)
        self.gearContainer.setLineWidth(4)
        self.gearLabel = QLabel(self.gearContainer)
        self.gearLabel.setObjectName(u"gearLabel")
        self.gearLabel.setGeometry(QRect(4, 5, 171, 211))
        self.gearLabel.setStyleSheet(u"color:white;\n"
"font: 110pt \"Formula1\";\n"
"")
        
        self.gearLabel.setTextFormat(Qt.PlainText)
        self.gearLabel.setAlignment(Qt.AlignCenter)
        self.speedContainer = QFrame(self.DriverDisplay)
        self.speedContainer.setObjectName(u"speedContainer")
        self.speedContainer.setGeometry(QRect(310, 10, 181, 61))
        self.speedContainer.setStyleSheet(u"border-width: 2px")
        self.speedContainer.setFrameShape(QFrame.StyledPanel)
        self.speedContainer.setFrameShadow(QFrame.Plain)
        self.speedContainer.setLineWidth(4)
        self.speedLabel = QLabel(self.speedContainer)
        self.speedLabel.setObjectName(u"speedLabel")
        self.speedLabel.setGeometry(QRect(4, 10, 171, 41))
        self.speedLabel.setStyleSheet(u"color:white;\n"
"font: 29pt \"Formula1\";\n"
"")
        self.speedLabel.setAlignment(Qt.AlignCenter)
        self.leftView = QFrame(self.DriverDisplay)
        self.leftView.setObjectName(u"leftView")
        self.leftView.setGeometry(QRect(20, 80, 281, 241))
        self.leftView.setFrameShape(QFrame.StyledPanel)
        self.leftView.setFrameShadow(QFrame.Plain)
        self.oilPressureLabel_5 = QFrame(self.leftView)
        self.oilPressureLabel_5.setObjectName(u"oilPressureLabel_5")
        self.oilPressureLabel_5.setGeometry(QRect(0, 120, 281, 61))
        self.oilPressureLabel_5.setFrameShape(QFrame.StyledPanel)
        self.oilPressureLabel_5.setFrameShadow(QFrame.Plain)
        self.oilPressLabel = QLabel(self.oilPressureLabel_5)
        self.oilPressLabel.setObjectName(u"oilPressLabel")
        self.oilPressLabel.setGeometry(QRect(10, 10, 261, 41))
        self.oilPressLabel.setStyleSheet(u"color:white;\n"
"font: 16pt \"Formula1\";\n"
"")
        self.oilPressLabel.setAlignment(Qt.AlignCenter)
        self.oilPressureLabel_7 = QFrame(self.leftView)
        self.oilPressureLabel_7.setObjectName(u"oilPressureLabel_7")
        self.oilPressureLabel_7.setGeometry(QRect(0, 0, 281, 61))
        self.oilPressureLabel_7.setFrameShape(QFrame.StyledPanel)
        self.oilPressureLabel_7.setFrameShadow(QFrame.Plain)
        self.oilTempLabel = QLabel(self.oilPressureLabel_7)
        self.oilTempLabel.setObjectName(u"oilTempLabel")
        self.oilTempLabel.setGeometry(QRect(10, 10, 261, 41))
        self.oilTempLabel.setStyleSheet(u"color:white;\n"
"font: 16pt \"Formula1\";\n"
"")
        self.oilTempLabel.setAlignment(Qt.AlignCenter)
        self.oilPressureLabel_6 = QFrame(self.leftView)
        self.oilPressureLabel_6.setObjectName(u"oilPressureLabel_6")
        self.oilPressureLabel_6.setGeometry(QRect(0, 180, 281, 61))
        self.oilPressureLabel_6.setStyleSheet(u"background-color: rgb(240, 240, 0)")
        self.oilPressureLabel_6.setFrameShape(QFrame.StyledPanel)
        self.oilPressureLabel_6.setFrameShadow(QFrame.Plain)
        self.speedLabel_11 = OutlinedLabel(self.oilPressureLabel_6)
        self.speedLabel_11.setObjectName(u"speedLabel_11")
        self.speedLabel_11.setGeometry(QRect(0, 0, 281, 61))
        self.speedLabel_11.setStyleSheet(u"color:white;\n"
"font: 23pt \"Formula1\";\n"
"")
        self.speedLabel_11.setAlignment(Qt.AlignCenter)
        self.oilPressureLabel_8 = QFrame(self.leftView)
        self.oilPressureLabel_8.setObjectName(u"oilPressureLabel_8")
        self.oilPressureLabel_8.setGeometry(QRect(0, 60, 281, 61))
        self.oilPressureLabel_8.setStyleSheet(u"background-color: rgb(240, 0, 0)")
        self.oilPressureLabel_8.setFrameShape(QFrame.StyledPanel)
        self.oilPressureLabel_8.setFrameShadow(QFrame.Plain)
        self.speedLabel_23 = OutlinedLabel(self.oilPressureLabel_8)
        self.speedLabel_23.setObjectName(u"speedLabel_23")
        self.speedLabel_23.setGeometry(QRect(0, 0, 281, 61))
        self.speedLabel_23.setStyleSheet(u"color:white;\n"
"font: 23pt \"Formula1\";\n"
"")
        self.speedLabel_23.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.DriverDisplay)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 440, 41, 41))
        self.label.setPixmap(QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "media", "gcu-racing-logo.jpeg")))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.DriverDisplay)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 450, 281, 16))
        self.label_2.setStyleSheet(u"color:white;\n"
"font: 10pt \"Formula1\";\n"
"")
        self.oilTempLabel_6 = QFrame(self.DriverDisplay)
        self.oilTempLabel_6.setObjectName(u"oilTempLabel_6")
        self.oilTempLabel_6.setGeometry(QRect(20, 330, 281, 41))
        self.oilTempLabel_6.setFrameShape(QFrame.StyledPanel)
        self.oilTempLabel_6.setFrameShadow(QFrame.Plain)
        self.oilTempLabel_7 = QFrame(self.oilTempLabel_6)
        self.oilTempLabel_7.setObjectName(u"oilTempLabel_7")
        self.oilTempLabel_7.setGeometry(QRect(0, 0, 141, 41))
        self.oilTempLabel_7.setFrameShape(QFrame.StyledPanel)
        self.oilTempLabel_7.setFrameShadow(QFrame.Plain)
        self.speedLabel_24 = QLabel(self.oilTempLabel_7)
        self.speedLabel_24.setObjectName(u"speedLabel_24")
        self.speedLabel_24.setGeometry(QRect(10, 10, 121, 21))
        self.speedLabel_24.setStyleSheet(u"color:white;\n"
"font: 12pt \"Formula1\";\n"
"")
        self.speedLabel_24.setAlignment(Qt.AlignCenter)
        self.oilTempLabel_8 = QFrame(self.oilTempLabel_6)
        self.oilTempLabel_8.setObjectName(u"oilTempLabel_8")
        self.oilTempLabel_8.setGeometry(QRect(140, 0, 141, 41))
        self.oilTempLabel_8.setFrameShape(QFrame.StyledPanel)
        self.oilTempLabel_8.setFrameShadow(QFrame.Plain)
        self.speedLabel_27 = QLabel(self.oilTempLabel_8)
        self.speedLabel_27.setObjectName(u"speedLabel_27")
        self.speedLabel_27.setGeometry(QRect(10, 10, 121, 21))
        self.speedLabel_27.setStyleSheet(u"color:white;\n"
"font: 12pt \"Formula1\";\n"
"")
        self.speedLabel_27.setAlignment(Qt.AlignCenter)
        self.oilTempLabel_15 = QFrame(self.DriverDisplay)
        self.oilTempLabel_15.setObjectName(u"oilTempLabel_15")
        self.oilTempLabel_15.setGeometry(QRect(500, 330, 281, 41))
        self.oilTempLabel_15.setFrameShape(QFrame.StyledPanel)
        self.oilTempLabel_15.setFrameShadow(QFrame.Plain)
        self.oilTempLabel_16 = QFrame(self.oilTempLabel_15)
        self.oilTempLabel_16.setObjectName(u"oilTempLabel_16")
        self.oilTempLabel_16.setGeometry(QRect(0, 0, 141, 41))
        self.oilTempLabel_16.setFrameShape(QFrame.StyledPanel)
        self.oilTempLabel_16.setFrameShadow(QFrame.Plain)
        self.speedLabel_35 = QLabel(self.oilTempLabel_16)
        self.speedLabel_35.setObjectName(u"speedLabel_35")
        self.speedLabel_35.setGeometry(QRect(10, 10, 121, 21))
        self.speedLabel_35.setStyleSheet(u"color:white;\n"
"font: 12pt \"Formula1\";\n"
"")
        self.speedLabel_35.setAlignment(Qt.AlignCenter)
        self.oilTempLabel_17 = QFrame(self.oilTempLabel_15)
        self.oilTempLabel_17.setObjectName(u"oilTempLabel_17")
        self.oilTempLabel_17.setGeometry(QRect(140, 0, 141, 41))
        self.oilTempLabel_17.setFrameShape(QFrame.StyledPanel)
        self.oilTempLabel_17.setFrameShadow(QFrame.Plain)
        self.speedLabel_36 = QLabel(self.oilTempLabel_17)
        self.speedLabel_36.setObjectName(u"speedLabel_36")
        self.speedLabel_36.setGeometry(QRect(10, 10, 121, 21))
        self.speedLabel_36.setStyleSheet(u"color:white;\n"
"font: 12pt \"Formula1\";\n"
"")
        self.speedLabel_36.setAlignment(Qt.AlignCenter)
        self.leftView_2 = QFrame(self.DriverDisplay)
        self.leftView_2.setObjectName(u"leftView_2")
        self.leftView_2.setGeometry(QRect(500, 80, 281, 241))
        self.leftView_2.setFrameShape(QFrame.StyledPanel)
        self.leftView_2.setFrameShadow(QFrame.Plain)
        self.oilPressureLabel_17 = QFrame(self.leftView_2)
        self.oilPressureLabel_17.setObjectName(u"oilPressureLabel_17")
        self.oilPressureLabel_17.setGeometry(QRect(0, 120, 281, 61))
        self.oilPressureLabel_17.setFrameShape(QFrame.StyledPanel)
        self.oilPressureLabel_17.setFrameShadow(QFrame.Plain)
        self.speedLabel_16 = QLabel(self.oilPressureLabel_17)
        self.speedLabel_16.setObjectName(u"speedLabel_16")
        self.speedLabel_16.setGeometry(QRect(10, 10, 261, 41))
        self.speedLabel_16.setStyleSheet(u"color:white;\n"
"font: 16pt \"Formula1\";\n"
"")
        self.speedLabel_16.setAlignment(Qt.AlignCenter)
        self.oilPressureLabel_18 = QFrame(self.leftView_2)
        self.oilPressureLabel_18.setObjectName(u"oilPressureLabel_18")
        self.oilPressureLabel_18.setGeometry(QRect(0, 0, 281, 61))
        self.oilPressureLabel_18.setFrameShape(QFrame.StyledPanel)
        self.oilPressureLabel_18.setFrameShadow(QFrame.Plain)
        self.speedLabel_41 = QLabel(self.oilPressureLabel_18)
        self.speedLabel_41.setObjectName(u"speedLabel_41")
        self.speedLabel_41.setGeometry(QRect(10, 10, 261, 41))
        self.speedLabel_41.setStyleSheet(u"color:white;\n"
"font: 16pt \"Formula1\";\n"
"")
        self.speedLabel_41.setAlignment(Qt.AlignCenter)
        self.oilPressureLabel_19 = QFrame(self.leftView_2)
        self.oilPressureLabel_19.setObjectName(u"oilPressureLabel_19")
        self.oilPressureLabel_19.setGeometry(QRect(0, 180, 281, 61))
        self.oilPressureLabel_19.setStyleSheet(u"background-color: rgb(0, 240, 0)")
        self.oilPressureLabel_19.setFrameShape(QFrame.StyledPanel)
        self.oilPressureLabel_19.setFrameShadow(QFrame.Plain)
        self.speedLabel_17 = OutlinedLabel(self.oilPressureLabel_19)
        self.speedLabel_17.setObjectName(u"speedLabel_17")
        self.speedLabel_17.setGeometry(QRect(0, 0, 281, 61))
        self.speedLabel_17.setStyleSheet(u"color:white;\n"
"font: 23pt \"Formula1\";\n"
"")
        self.speedLabel_17.setAlignment(Qt.AlignCenter)
        self.oilPressureLabel_20 = QFrame(self.leftView_2)
        self.oilPressureLabel_20.setObjectName(u"oilPressureLabel_20")
        self.oilPressureLabel_20.setGeometry(QRect(0, 60, 281, 61))
        self.oilPressureLabel_20.setStyleSheet(u"background-color: rgb(0, 240, 0)")
        self.oilPressureLabel_20.setFrameShape(QFrame.StyledPanel)
        self.oilPressureLabel_20.setFrameShadow(QFrame.Plain)
        self.speedLabel_42 = OutlinedLabel(self.oilPressureLabel_20)
        self.speedLabel_42.setObjectName(u"speedLabel_42")
        self.speedLabel_42.setGeometry(QRect(0, 0, 281, 61))
        self.speedLabel_42.setStyleSheet(u"color:white;\n"
"font: 23pt \"Formula1\";\n"
"")
        self.speedLabel_42.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.DriverDisplay)
        # creating a timer object
        timer = QTimer(MainWindow)
 
        # adding action to timer
        timer.timeout.connect(self.showTime)
 
        # update the timer every tenth second
        timer.start(1)
        
        # creating a timer object
        timer2 = QTimer(MainWindow)
 
        # adding action to timer
        timer2.timeout.connect(self.updateVariables)
 
        # update the timer every tenth second
        timer2.start(0.02)
        
        #MainWindow.showFullScreen() 

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.gearLabel.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.speedLabel.setText(QCoreApplication.translate("MainWindow", u"35", None))
        self.oilPressLabel.setText(QCoreApplication.translate("MainWindow", u"Oil Pressure", None))
        self.oilTempLabel.setText(QCoreApplication.translate("MainWindow", u"Oil Temperature", None))
        self.speedLabel_11.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.speedLabel_23.setText(QCoreApplication.translate("MainWindow", u"110", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GCUR-03 Display V1.0", None))
        self.speedLabel_24.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.speedLabel_27.setText(QCoreApplication.translate("MainWindow", u"14.6V", None))
        self.speedLabel_35.setText(QCoreApplication.translate("MainWindow", u"Run Time", None))
        self.speedLabel_36.setText(QCoreApplication.translate("MainWindow", u"//TIMER//", None))
        self.speedLabel_16.setText(QCoreApplication.translate("MainWindow", u"Coolant Temp", None))
        self.speedLabel_41.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.speedLabel_17.setText(QCoreApplication.translate("MainWindow", u"104", None))
        self.speedLabel_42.setText(QCoreApplication.translate("MainWindow", u"6500", None))
    # retranslateUi
    
    def showTime(self):
        global minutesRT, secondsRT
        self.count += 1
        
        if (self.count == 1000):
            self.count = 0
            secondsRT += 1
            if (secondsRT == 60):
                minutesRT += 1
                secondsRT = 0
        
    
        # showing text
        self.speedLabel_36.setText("{0:02}".format(minutesRT) + "." + "{0:02}".format(secondsRT) + ":" + "{0:03}".format(self.count))
        
    def updateVariables(self):
        global oilTemp, oilPress, rpm, coolantTemp
        
        poilTemp =  oilTemp
        poilPress = oilPress
        pRpm = rpm
        pcoolantTemp = coolantTemp
        
        try:
            dataDF = pd.read_csv("displayData.csv")
            oilTemp = dataDF["oilTemp"].iloc[0]
            oilPress = dataDF["oilPressure"].iloc[0]
            rpm = dataDF["rpm"].iloc[0]
            coolantTemp = dataDF["coolantTemp"].iloc[0]
        except Exception as e:
            print(e)
            oilTemp = poilTemp
            oilPress = poilPress
            rpm = pRpm
            coolantTemp = pcoolantTemp

        
    
        # showing text
        self.speedLabel_23.setText(str(oilTemp))
        self.speedLabel_11.setText(str(oilPress))
        self.speedLabel_42.setText(str(rpm))
        self.speedLabel_17.setText(str(coolantTemp))
        
        if oilTemp <130 :
            self.oilPressureLabel_8.setStyleSheet(u"background-color: rgb(0, 240, 0)")
        elif oilTemp <=90 and oilTemp >=150:
            self.oilPressureLabel_8.setStyleSheet(u"background-color: rgb(240, 240, 0)")
        else:
            self.oilPressureLabel_8.setStyleSheet(u"background-color: rgb(240, 0, 0)")

        if oilPress<30:
            self.oilPressureLabel_6.setStyleSheet(u"background-color: rgb(0, 240, 0)")
        elif oilPress<=31 and oilPress>=15:
            self.oilPressureLabel_6.setStyleSheet(u"background-color: rgb(240, 240, 0)")
        else:
            self.oilPressureLabel_6.setStyleSheet(u"background-color: rgb(240, 0, 0)")
       
        if rpm<5000:
            self.oilPressureLabel_19.setStyleSheet(u"background-color: rgb(0, 240, 0)")
        elif rpm<=8000 and rpm >=5001:
            self.oilPressureLabel_19.setStyleSheet(u"background-color: rgb(240, 240, 0)")
        else:
            self.oilPressureLabel_19.setStyleSheet(u"background-color: rgb(240, 0, 0)")

        if coolantTemp<116:
            self.oilPressureLabel_20.setStyleSheet(u"background-color: rgb(0, 240, 0)")
        elif coolantTemp<=135 and coolantTemp>=116:
            self.oilPressureLabel_20.setStyleSheet(u"background-color: rgb(240, 240, 0)")
        else:
            self.oilPressureLabel_20.setStyleSheet(u"background-color: rgb(240, 0, 0)")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)


    MainWindow = QMainWindow()
    MainWindow.hide()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    def go_to_main_window():
        print("Video done. Transition to main window.")
        MainWindow.opacity_effect = QGraphicsOpacityEffect(MainWindow)
        MainWindow.setGraphicsEffect(MainWindow.opacity_effect)
        MainWindow.opacity_effect.setOpacity(0)
        MainWindow.show()

        anim = QPropertyAnimation(MainWindow.opacity_effect, b"opacity")
        anim.setDuration(10000)
        anim.setStartValue(0)
        anim.setEndValue(1)
        anim.start()
        MainWindow.animation = anim
        splash.close()
        
    splash = SplashVideo(go_to_main_window)

    sys.exit(app.exec_())

