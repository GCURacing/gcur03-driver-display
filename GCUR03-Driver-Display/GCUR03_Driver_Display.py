from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QTimer)
from PyQt5 import QtCore
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import time

oilTemp = 90
oilPress = 40
fuelTemp = 40
coolantTemp = 75
rpm = 0
speed = 0
tyrePressFL = 50
tyrePressFR = 40
tyrePressRL = 30
tyrePressRR = 20
minutesRT = 0
secondsRT = 0





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
        self.speedLabel_10 = QLabel(self.oilPressureLabel_5)
        self.speedLabel_10.setObjectName(u"speedLabel_10")
        self.speedLabel_10.setGeometry(QRect(10, 10, 261, 41))
        self.speedLabel_10.setStyleSheet(u"color:white;\n"
"font: 16pt \"Formula1\";\n"
"")
        self.speedLabel_10.setAlignment(Qt.AlignCenter)
        self.oilPressureLabel_7 = QFrame(self.leftView)
        self.oilPressureLabel_7.setObjectName(u"oilPressureLabel_7")
        self.oilPressureLabel_7.setGeometry(QRect(0, 0, 281, 61))
        self.oilPressureLabel_7.setFrameShape(QFrame.StyledPanel)
        self.oilPressureLabel_7.setFrameShadow(QFrame.Plain)
        self.speedLabel_21 = QLabel(self.oilPressureLabel_7)
        self.speedLabel_21.setObjectName(u"speedLabel_21")
        self.speedLabel_21.setGeometry(QRect(10, 10, 261, 41))
        self.speedLabel_21.setStyleSheet(u"color:white;\n"
"font: 16pt \"Formula1\";\n"
"")
        self.speedLabel_21.setAlignment(Qt.AlignCenter)
        self.oilPressureLabel_6 = QFrame(self.leftView)
        self.oilPressureLabel_6.setObjectName(u"oilPressureLabel_6")
        self.oilPressureLabel_6.setGeometry(QRect(0, 180, 281, 61))
        self.oilPressureLabel_6.setStyleSheet(u"background-color: rgb(255, 255, 0)")
        self.oilPressureLabel_6.setFrameShape(QFrame.StyledPanel)
        self.oilPressureLabel_6.setFrameShadow(QFrame.Plain)
        self.speedLabel_11 = QLabel(self.oilPressureLabel_6)
        self.speedLabel_11.setObjectName(u"speedLabel_11")
        self.speedLabel_11.setGeometry(QRect(0, 0, 281, 61))
        self.speedLabel_11.setStyleSheet(u"color:white;\n"
"font: 16pt \"Formula1\";\n"
"")
        self.speedLabel_11.setAlignment(Qt.AlignCenter)
        self.oilPressureLabel_8 = QFrame(self.leftView)
        self.oilPressureLabel_8.setObjectName(u"oilPressureLabel_8")
        self.oilPressureLabel_8.setGeometry(QRect(0, 60, 281, 61))
        self.oilPressureLabel_8.setStyleSheet(u"background-color: rgb(255, 0, 0)")
        self.oilPressureLabel_8.setFrameShape(QFrame.StyledPanel)
        self.oilPressureLabel_8.setFrameShadow(QFrame.Plain)
        self.speedLabel_23 = QLabel(self.oilPressureLabel_8)
        self.speedLabel_23.setObjectName(u"speedLabel_23")
        self.speedLabel_23.setGeometry(QRect(0, 0, 281, 61))
        self.speedLabel_23.setStyleSheet(u"color:white;\n"
"font: 16pt \"Formula1\";\n"
"")
        self.speedLabel_23.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.DriverDisplay)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 440, 41, 41))
        self.label.setPixmap(QPixmap(u"gcu-racing-logo.jpeg"))
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
        self.oilTempLabel_9 = QFrame(self.DriverDisplay)
        self.oilTempLabel_9.setObjectName(u"oilTempLabel_9")
        self.oilTempLabel_9.setGeometry(QRect(310, 330, 181, 121))
        self.oilTempLabel_9.setFrameShape(QFrame.StyledPanel)
        self.oilTempLabel_9.setFrameShadow(QFrame.Plain)
        self.oilTempLabel_10 = QFrame(self.oilTempLabel_9)
        self.oilTempLabel_10.setObjectName(u"oilTempLabel_10")
        self.oilTempLabel_10.setGeometry(QRect(0, 0, 181, 41))
        self.oilTempLabel_10.setFrameShape(QFrame.StyledPanel)
        self.oilTempLabel_10.setFrameShadow(QFrame.Plain)
        self.speedLabel_29 = QLabel(self.oilTempLabel_10)
        self.speedLabel_29.setObjectName(u"speedLabel_29")
        self.speedLabel_29.setGeometry(QRect(10, 10, 161, 21))
        self.speedLabel_29.setStyleSheet(u"color:white;\n"
"font: 12pt \"Formula1\";\n"
"")
        self.speedLabel_29.setAlignment(Qt.AlignCenter)
        self.oilTempLabel_11 = QFrame(self.oilTempLabel_9)
        self.oilTempLabel_11.setObjectName(u"oilTempLabel_11")
        self.oilTempLabel_11.setGeometry(QRect(0, 40, 91, 41))
        self.oilTempLabel_11.setStyleSheet(u"background-color: rgb(0, 255, 0)")
        self.oilTempLabel_11.setFrameShape(QFrame.StyledPanel)
        self.oilTempLabel_11.setFrameShadow(QFrame.Plain)
        self.speedLabel_30 = QLabel(self.oilTempLabel_11)
        self.speedLabel_30.setObjectName(u"speedLabel_30")
        self.speedLabel_30.setGeometry(QRect(10, 10, 71, 21))
        self.speedLabel_30.setStyleSheet(u"color:white;\n"
"font: 12pt \"Formula1\";\n"
"")
        self.speedLabel_30.setAlignment(Qt.AlignCenter)
        self.oilTempLabel_12 = QFrame(self.oilTempLabel_9)
        self.oilTempLabel_12.setObjectName(u"oilTempLabel_12")
        self.oilTempLabel_12.setGeometry(QRect(0, 80, 91, 41))
        self.oilTempLabel_12.setStyleSheet(u"background-color: rgb(255, 255, 0)")
        self.oilTempLabel_12.setFrameShape(QFrame.StyledPanel)
        self.oilTempLabel_12.setFrameShadow(QFrame.Plain)
        self.speedLabel_31 = QLabel(self.oilTempLabel_12)
        self.speedLabel_31.setObjectName(u"speedLabel_31")
        self.speedLabel_31.setGeometry(QRect(10, 10, 71, 21))
        self.speedLabel_31.setStyleSheet(u"color:white;\n"
"font: 12pt \"Formula1\";\n"
"")
        self.speedLabel_31.setAlignment(Qt.AlignCenter)
        self.oilTempLabel_13 = QFrame(self.oilTempLabel_9)
        self.oilTempLabel_13.setObjectName(u"oilTempLabel_13")
        self.oilTempLabel_13.setGeometry(QRect(90, 40, 91, 41))
        self.oilTempLabel_13.setStyleSheet(u"background-color: rgb(255, 0, 0)")
        self.oilTempLabel_13.setFrameShape(QFrame.StyledPanel)
        self.oilTempLabel_13.setFrameShadow(QFrame.Plain)
        self.speedLabel_33 = QLabel(self.oilTempLabel_13)
        self.speedLabel_33.setObjectName(u"speedLabel_33")
        self.speedLabel_33.setGeometry(QRect(10, 10, 71, 21))
        self.speedLabel_33.setStyleSheet(u"color:white;\n"
"font: 12pt \"Formula1\";\n"
"")
        self.speedLabel_33.setAlignment(Qt.AlignCenter)
        self.oilTempLabel_14 = QFrame(self.oilTempLabel_9)
        self.oilTempLabel_14.setObjectName(u"oilTempLabel_14")
        self.oilTempLabel_14.setGeometry(QRect(90, 80, 91, 41))
        self.oilTempLabel_14.setStyleSheet(u"background-color: rgb(0, 255, 0)")
        self.oilTempLabel_14.setFrameShape(QFrame.StyledPanel)
        self.oilTempLabel_14.setFrameShadow(QFrame.Plain)
        self.speedLabel_34 = QLabel(self.oilTempLabel_14)
        self.speedLabel_34.setObjectName(u"speedLabel_34")
        self.speedLabel_34.setGeometry(QRect(10, 10, 71, 21))
        self.speedLabel_34.setStyleSheet(u"color:white;\n"
"font: 12pt \"Formula1\";\n"
"")
        self.speedLabel_34.setAlignment(Qt.AlignCenter)
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
        self.oilPressureLabel_19.setStyleSheet(u"background-color: rgb(0, 255, 0)")
        self.oilPressureLabel_19.setFrameShape(QFrame.StyledPanel)
        self.oilPressureLabel_19.setFrameShadow(QFrame.Plain)
        self.speedLabel_17 = QLabel(self.oilPressureLabel_19)
        self.speedLabel_17.setObjectName(u"speedLabel_17")
        self.speedLabel_17.setGeometry(QRect(0, 0, 281, 61))
        self.speedLabel_17.setStyleSheet(u"color:white;\n"
"font: 16pt \"Formula1\";\n"
"")
        self.speedLabel_17.setAlignment(Qt.AlignCenter)
        self.oilPressureLabel_20 = QFrame(self.leftView_2)
        self.oilPressureLabel_20.setObjectName(u"oilPressureLabel_20")
        self.oilPressureLabel_20.setGeometry(QRect(0, 60, 281, 61))
        self.oilPressureLabel_20.setStyleSheet(u"background-color: rgb(0, 255, 0)")
        self.oilPressureLabel_20.setFrameShape(QFrame.StyledPanel)
        self.oilPressureLabel_20.setFrameShadow(QFrame.Plain)
        self.speedLabel_42 = QLabel(self.oilPressureLabel_20)
        self.speedLabel_42.setObjectName(u"speedLabel_42")
        self.speedLabel_42.setGeometry(QRect(0, 0, 281, 61))
        self.speedLabel_42.setStyleSheet(u"color:white;\n"
"font: 16pt \"Formula1\";\n"
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
        timer2.timeout.connect(self.cycleVariables)
 
        # update the timer every tenth second
        timer2.start(300)
        
        #MainWindow.showFullScreen() 

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.gearLabel.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.speedLabel.setText(QCoreApplication.translate("MainWindow", u"35", None))
        self.speedLabel_10.setText(QCoreApplication.translate("MainWindow", u"Oil Pressure", None))
        self.speedLabel_21.setText(QCoreApplication.translate("MainWindow", u"Oil Temperature", None))
        self.speedLabel_11.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.speedLabel_23.setText(QCoreApplication.translate("MainWindow", u"110", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GCUR-03 Display V1.0", None))
        self.speedLabel_24.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.speedLabel_27.setText(QCoreApplication.translate("MainWindow", u"6500", None))
        self.speedLabel_29.setText(QCoreApplication.translate("MainWindow", u"Tyre Pressure", None))
        self.speedLabel_30.setText(QCoreApplication.translate("MainWindow", u"1.72", None))
        self.speedLabel_31.setText(QCoreApplication.translate("MainWindow", u"1.85", None))
        self.speedLabel_33.setText(QCoreApplication.translate("MainWindow", u"1.72", None))
        self.speedLabel_34.setText(QCoreApplication.translate("MainWindow", u"1.85", None))
        self.speedLabel_35.setText(QCoreApplication.translate("MainWindow", u"Run Time", None))
        self.speedLabel_36.setText(QCoreApplication.translate("MainWindow", u"//TIMER//", None))
        self.speedLabel_16.setText(QCoreApplication.translate("MainWindow", u"Fuel Temp", None))
        self.speedLabel_41.setText(QCoreApplication.translate("MainWindow", u"Coolant Temp", None))
        self.speedLabel_17.setText(QCoreApplication.translate("MainWindow", u"70", None))
        self.speedLabel_42.setText(QCoreApplication.translate("MainWindow", u"104", None))
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
        
    def cycleVariables(self):
        global oilTemp, oilPress, fuelTemp, coolantTemp, tyrePressFL, tyrePressFR, tyrePressRL, tyrePressRR
        
        oilTemp += 5
        oilPress -= 5
        fuelTemp += 5
        coolantTemp += 5
        tyrePressFR -= 3
        tyrePressRR -= 3
        tyrePressRL -= 3
        tyrePressFL -= 3
        
        if (oilTemp == 150):
            oilTemp = 90
           
        if (oilPress == 10):
            oilPress = 40
            
        if (fuelTemp == 90):
            fuelTemp = 40
            
        if (coolantTemp == 130):
            coolantTemp = 75
           
        if (tyrePressFL <= 5):
            tyrePressFL = 30
            
        if (tyrePressRL <= 5):
            tyrePressRL = 30
            
        if (tyrePressFR <= 5):
            tyrePressFR = 30
            
        if (tyrePressRR <= 5):
            tyrePressRR = 30

        
    
        # showing text
        self.speedLabel_23.setText(str(oilTemp))
        self.speedLabel_11.setText(str(oilPress))
        self.speedLabel_42.setText(str(fuelTemp))
        self.speedLabel_17.setText(str(coolantTemp))
        self.speedLabel_30.setText(str(tyrePressFL))
        self.speedLabel_31.setText(str(tyrePressRL))
        self.speedLabel_33.setText(str(tyrePressFR))
        self.speedLabel_34.setText(str(tyrePressRR))
        
        if oilTemp <130 :
            self.oilPressureLabel_8.setStyleSheet(u"background-color: rgb(0, 255, 0)")
        elif oilTemp <=90 and oilTemp >=150:
            self.oilPressureLabel_8.setStyleSheet(u"background-color: rgb(255, 255, 0)")
        else:
            self.oilPressureLabel_8.setStyleSheet(u"background-color: rgb(255, 0, 0)")

        if oilPress<30:
            self.oilPressureLabel_6.setStyleSheet(u"background-color: rgb(0, 255, 0)")
        elif oilPress<=31 and oilPress>=15:
            self.oilPressureLabel_6.setStyleSheet(u"background-color: rgb(255, 255, 0)")
        else:
            self.oilPressureLabel_6.setStyleSheet(u"background-color: rgb(255, 0, 0)")
       
        if fuelTemp<50:
            self.oilPressureLabel_19.setStyleSheet(u"background-color: rgb(0, 255, 0)")
        elif fuelTemp<=90 and fuelTemp >=50:
            self.oilPressureLabel_19.setStyleSheet(u"background-color: rgb(255, 255, 0)")
        else:
            self.oilPressureLabel_19.setStyleSheet(u"background-color: rgb(255, 0, 0)")

        if coolantTemp<116:
            self.oilPressureLabel_20.setStyleSheet(u"background-color: rgb(0, 255, 0)")
        elif coolantTemp<=135 and coolantTemp>=116:
            self.oilPressureLabel_20.setStyleSheet(u"background-color: rgb(255, 255, 0)")
        else:
            self.oilPressureLabel_20.setStyleSheet(u"background-color: rgb(255, 0, 0)")

        if tyrePressFL>30:
            self.oilTempLabel_11.setStyleSheet(u"background-color: rgb(0, 255, 0)")
        elif tyrePressFL<=30 and tyrePressFL>=24:
            self.oilTempLabel_11.setStyleSheet(u"background-color: rgb(255, 255, 0)")
        else:
            self.oilTempLabel_11.setStyleSheet(u"background-color: rgb(255, 0, 0)")

        if tyrePressRL>30:
           self.oilTempLabel_12.setStyleSheet(u"background-color: rgb(0, 255, 0)")
        elif tyrePressRL<=30 and tyrePressRL>=24:
            self.oilTempLabel_12.setStyleSheet(u"background-color: rgb(255, 255, 0)")
        else:
            self.oilTempLabel_12.setStyleSheet(u"background-color: rgb(255, 0, 0)")
       
        if tyrePressFR>30:
            self.oilTempLabel_13.setStyleSheet(u"background-color: rgb(0, 255, 0)")
        elif tyrePressFR<=30 and tyrePressFR>=24:
            self.oilTempLabel_13.setStyleSheet(u"background-color: rgb(255, 255, 0)")
        else:
            self.oilTempLabel_13.setStyleSheet(u"background-color: rgb(255, 0, 0)")

        if tyrePressRR>30:
            self.oilTempLabel_14.setStyleSheet(u"background-color: rgb(0, 255, 0)")
        elif tyrePressRR<=30 and tyrePressRR >=24:
            self.oilTempLabel_14.setStyleSheet(u"background-color: rgb(255, 255, 0)")
        else:
            self.oilTempLabel_14.setStyleSheet(u"background-color: rgb(255, 0, 0)")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

