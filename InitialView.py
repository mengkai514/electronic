# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InitialView.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QWidget)

class Ui_InitialViewWindow(object):
    def setupUi(self, InitialViewWindow):
        if not InitialViewWindow.objectName():
            InitialViewWindow.setObjectName(u"InitialViewWindow")
        InitialViewWindow.resize(846, 776)
        font = QFont()
        font.setPointSize(12)
        InitialViewWindow.setFont(font)
        self.centralwidget = QWidget(InitialViewWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_top = QLabel(self.centralwidget)
        self.label_top.setObjectName(u"label_top")
        self.label_top.setGeometry(QRect(300, 0, 144, 61))
        font1 = QFont()
        font1.setPointSize(36)
        font1.setBold(True)
        self.label_top.setFont(font1)
        self.label_camera1 = QLabel(self.centralwidget)
        self.label_camera1.setObjectName(u"label_camera1")
        self.label_camera1.setGeometry(QRect(60, 90, 61, 31))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_camera1.setFont(font2)
        self.label_camera2 = QLabel(self.centralwidget)
        self.label_camera2.setObjectName(u"label_camera2")
        self.label_camera2.setGeometry(QRect(310, 90, 61, 31))
        self.label_camera2.setFont(font2)
        self.label_camera3 = QLabel(self.centralwidget)
        self.label_camera3.setObjectName(u"label_camera3")
        self.label_camera3.setGeometry(QRect(570, 90, 61, 31))
        self.label_camera3.setFont(font2)
        self.textBrowser_camera1 = QTextBrowser(self.centralwidget)
        self.textBrowser_camera1.setObjectName(u"textBrowser_camera1")
        self.textBrowser_camera1.setGeometry(QRect(130, 90, 141, 31))
        self.textBrowser_camera2 = QTextBrowser(self.centralwidget)
        self.textBrowser_camera2.setObjectName(u"textBrowser_camera2")
        self.textBrowser_camera2.setGeometry(QRect(380, 90, 141, 31))
        self.textBrowser_camera3 = QTextBrowser(self.centralwidget)
        self.textBrowser_camera3.setObjectName(u"textBrowser_camera3")
        self.textBrowser_camera3.setGeometry(QRect(640, 90, 141, 31))
        self.label_camera4 = QLabel(self.centralwidget)
        self.label_camera4.setObjectName(u"label_camera4")
        self.label_camera4.setGeometry(QRect(60, 130, 61, 31))
        self.label_camera4.setFont(font2)
        self.label_camera5 = QLabel(self.centralwidget)
        self.label_camera5.setObjectName(u"label_camera5")
        self.label_camera5.setGeometry(QRect(310, 130, 61, 31))
        self.label_camera5.setFont(font2)
        self.textBrowser_camera5 = QTextBrowser(self.centralwidget)
        self.textBrowser_camera5.setObjectName(u"textBrowser_camera5")
        self.textBrowser_camera5.setGeometry(QRect(380, 130, 141, 31))
        self.label_PLC = QLabel(self.centralwidget)
        self.label_PLC.setObjectName(u"label_PLC")
        self.label_PLC.setGeometry(QRect(570, 130, 61, 31))
        self.label_PLC.setFont(font2)
        self.textBrowser_PLC = QTextBrowser(self.centralwidget)
        self.textBrowser_PLC.setObjectName(u"textBrowser_PLC")
        self.textBrowser_PLC.setGeometry(QRect(640, 130, 141, 31))
        self.label_curParams = QLabel(self.centralwidget)
        self.label_curParams.setObjectName(u"label_curParams")
        self.label_curParams.setGeometry(QRect(60, 180, 141, 31))
        self.label_curParams.setFont(font2)
        self.label_curCameraParams = QLabel(self.centralwidget)
        self.label_curCameraParams.setObjectName(u"label_curCameraParams")
        self.label_curCameraParams.setGeometry(QRect(60, 220, 141, 31))
        font3 = QFont()
        font3.setPointSize(13)
        self.label_curCameraParams.setFont(font3)
        self.label_camera1_1 = QLabel(self.centralwidget)
        self.label_camera1_1.setObjectName(u"label_camera1_1")
        self.label_camera1_1.setGeometry(QRect(60, 260, 61, 31))
        self.label_camera1_1.setFont(font2)
        self.pushButton_VCamera1 = QPushButton(self.centralwidget)
        self.pushButton_VCamera1.setObjectName(u"pushButton_VCamera1")
        self.pushButton_VCamera1.setGeometry(QRect(130, 260, 91, 41))
        self.pushButton_VCamera1.setFont(font2)
        self.label_camera2_1 = QLabel(self.centralwidget)
        self.label_camera2_1.setObjectName(u"label_camera2_1")
        self.label_camera2_1.setGeometry(QRect(240, 260, 61, 31))
        self.label_camera2_1.setFont(font2)
        self.pushButton_VCamera2 = QPushButton(self.centralwidget)
        self.pushButton_VCamera2.setObjectName(u"pushButton_VCamera2")
        self.pushButton_VCamera2.setGeometry(QRect(310, 260, 91, 41))
        self.pushButton_VCamera2.setFont(font2)
        self.label_camera3_1 = QLabel(self.centralwidget)
        self.label_camera3_1.setObjectName(u"label_camera3_1")
        self.label_camera3_1.setGeometry(QRect(60, 310, 61, 31))
        self.label_camera3_1.setFont(font2)
        self.pushButton_VCamera3 = QPushButton(self.centralwidget)
        self.pushButton_VCamera3.setObjectName(u"pushButton_VCamera3")
        self.pushButton_VCamera3.setGeometry(QRect(130, 310, 91, 41))
        self.pushButton_VCamera3.setFont(font2)
        self.label_camera4_1 = QLabel(self.centralwidget)
        self.label_camera4_1.setObjectName(u"label_camera4_1")
        self.label_camera4_1.setGeometry(QRect(240, 310, 61, 31))
        self.label_camera4_1.setFont(font2)
        self.pushButton_VCamera4 = QPushButton(self.centralwidget)
        self.pushButton_VCamera4.setObjectName(u"pushButton_VCamera4")
        self.pushButton_VCamera4.setGeometry(QRect(310, 310, 91, 41))
        self.pushButton_VCamera4.setFont(font2)
        self.pushButton_VCamera5 = QPushButton(self.centralwidget)
        self.pushButton_VCamera5.setObjectName(u"pushButton_VCamera5")
        self.pushButton_VCamera5.setGeometry(QRect(130, 360, 91, 41))
        self.pushButton_VCamera5.setFont(font2)
        self.label_camera5_1 = QLabel(self.centralwidget)
        self.label_camera5_1.setObjectName(u"label_camera5_1")
        self.label_camera5_1.setGeometry(QRect(60, 360, 61, 31))
        self.label_camera5_1.setFont(font2)
        self.pushButton_VIP = QPushButton(self.centralwidget)
        self.pushButton_VIP.setObjectName(u"pushButton_VIP")
        self.pushButton_VIP.setGeometry(QRect(180, 420, 91, 41))
        self.pushButton_VIP.setFont(font2)
        self.label_VIP = QLabel(self.centralwidget)
        self.label_VIP.setObjectName(u"label_VIP")
        self.label_VIP.setGeometry(QRect(60, 420, 111, 31))
        self.label_VIP.setFont(font2)
        self.label_OtherParams = QLabel(self.centralwidget)
        self.label_OtherParams.setObjectName(u"label_OtherParams")
        self.label_OtherParams.setGeometry(QRect(60, 470, 111, 31))
        self.label_OtherParams.setFont(font2)
        self.label_VIP_2 = QLabel(self.centralwidget)
        self.label_VIP_2.setObjectName(u"label_VIP_2")
        self.label_VIP_2.setGeometry(QRect(60, 510, 121, 31))
        self.label_VIP_2.setFont(font2)
        self.textBrowser_VConveyorSpeed = QTextBrowser(self.centralwidget)
        self.textBrowser_VConveyorSpeed.setObjectName(u"textBrowser_VConveyorSpeed")
        self.textBrowser_VConveyorSpeed.setGeometry(QRect(180, 510, 141, 31))
        self.textBrowser_VConveyorSpeed.setFont(font)
        self.textBrowser_camera4 = QTextBrowser(self.centralwidget)
        self.textBrowser_camera4.setObjectName(u"textBrowser_camera4")
        self.textBrowser_camera4.setGeometry(QRect(130, 130, 141, 31))
        self.textBrowser_camera4.setFont(font)
        self.textBrowser_camera4_3 = QTextBrowser(self.centralwidget)
        self.textBrowser_camera4_3.setObjectName(u"textBrowser_camera4_3")
        self.textBrowser_camera4_3.setGeometry(QRect(180, 550, 141, 31))
        self.textBrowser_camera4_3.setFont(font)
        self.label_VIP_3 = QLabel(self.centralwidget)
        self.label_VIP_3.setObjectName(u"label_VIP_3")
        self.label_VIP_3.setGeometry(QRect(60, 550, 121, 31))
        self.label_VIP_3.setFont(font2)
        self.textBrowser_camera4_4 = QTextBrowser(self.centralwidget)
        self.textBrowser_camera4_4.setObjectName(u"textBrowser_camera4_4")
        self.textBrowser_camera4_4.setGeometry(QRect(180, 590, 141, 31))
        self.textBrowser_camera4_4.setFont(font)
        self.label_VIP_4 = QLabel(self.centralwidget)
        self.label_VIP_4.setObjectName(u"label_VIP_4")
        self.label_VIP_4.setGeometry(QRect(60, 590, 121, 31))
        self.label_VIP_4.setFont(font2)
        self.label_curParams_2 = QLabel(self.centralwidget)
        self.label_curParams_2.setObjectName(u"label_curParams_2")
        self.label_curParams_2.setGeometry(QRect(440, 190, 141, 31))
        self.label_curParams_2.setFont(font2)
        self.label_curCameraParams_2 = QLabel(self.centralwidget)
        self.label_curCameraParams_2.setObjectName(u"label_curCameraParams_2")
        self.label_curCameraParams_2.setGeometry(QRect(440, 220, 141, 31))
        self.label_curCameraParams_2.setFont(font3)
        self.label_camera3_2 = QLabel(self.centralwidget)
        self.label_camera3_2.setObjectName(u"label_camera3_2")
        self.label_camera3_2.setGeometry(QRect(440, 310, 61, 31))
        self.label_camera3_2.setFont(font2)
        self.pushButton_MCamera2 = QPushButton(self.centralwidget)
        self.pushButton_MCamera2.setObjectName(u"pushButton_MCamera2")
        self.pushButton_MCamera2.setGeometry(QRect(690, 260, 91, 41))
        self.pushButton_MCamera2.setFont(font2)
        self.label_camera4_2 = QLabel(self.centralwidget)
        self.label_camera4_2.setObjectName(u"label_camera4_2")
        self.label_camera4_2.setGeometry(QRect(620, 310, 61, 31))
        self.label_camera4_2.setFont(font2)
        self.label_camera5_2 = QLabel(self.centralwidget)
        self.label_camera5_2.setObjectName(u"label_camera5_2")
        self.label_camera5_2.setGeometry(QRect(440, 360, 61, 31))
        self.label_camera5_2.setFont(font2)
        self.pushButton_MCamera4 = QPushButton(self.centralwidget)
        self.pushButton_MCamera4.setObjectName(u"pushButton_MCamera4")
        self.pushButton_MCamera4.setGeometry(QRect(690, 310, 91, 41))
        self.pushButton_MCamera4.setFont(font2)
        self.pushButton_MCamera5 = QPushButton(self.centralwidget)
        self.pushButton_MCamera5.setObjectName(u"pushButton_MCamera5")
        self.pushButton_MCamera5.setGeometry(QRect(510, 360, 91, 41))
        self.pushButton_MCamera5.setFont(font2)
        self.label_camera2_2 = QLabel(self.centralwidget)
        self.label_camera2_2.setObjectName(u"label_camera2_2")
        self.label_camera2_2.setGeometry(QRect(620, 260, 61, 31))
        self.label_camera2_2.setFont(font2)
        self.label_camera1_2 = QLabel(self.centralwidget)
        self.label_camera1_2.setObjectName(u"label_camera1_2")
        self.label_camera1_2.setGeometry(QRect(440, 260, 61, 31))
        self.label_camera1_2.setFont(font2)
        self.pushButton_MCamera1 = QPushButton(self.centralwidget)
        self.pushButton_MCamera1.setObjectName(u"pushButton_MCamera1")
        self.pushButton_MCamera1.setGeometry(QRect(510, 260, 91, 41))
        self.pushButton_MCamera1.setFont(font2)
        self.pushButton_MCamera3 = QPushButton(self.centralwidget)
        self.pushButton_MCamera3.setObjectName(u"pushButton_MCamera3")
        self.pushButton_MCamera3.setGeometry(QRect(510, 310, 91, 41))
        self.pushButton_MCamera3.setFont(font2)
        self.label_VIP_5 = QLabel(self.centralwidget)
        self.label_VIP_5.setObjectName(u"label_VIP_5")
        self.label_VIP_5.setGeometry(QRect(440, 420, 111, 31))
        self.label_VIP_5.setFont(font2)
        self.pushButton_VIP_2 = QPushButton(self.centralwidget)
        self.pushButton_VIP_2.setObjectName(u"pushButton_VIP_2")
        self.pushButton_VIP_2.setGeometry(QRect(560, 420, 91, 41))
        self.pushButton_VIP_2.setFont(font2)
        self.label_VIP_6 = QLabel(self.centralwidget)
        self.label_VIP_6.setObjectName(u"label_VIP_6")
        self.label_VIP_6.setGeometry(QRect(440, 590, 121, 31))
        self.label_VIP_6.setFont(font2)
        self.label_VIP_7 = QLabel(self.centralwidget)
        self.label_VIP_7.setObjectName(u"label_VIP_7")
        self.label_VIP_7.setGeometry(QRect(440, 510, 121, 31))
        self.label_VIP_7.setFont(font2)
        self.label_VIP_8 = QLabel(self.centralwidget)
        self.label_VIP_8.setObjectName(u"label_VIP_8")
        self.label_VIP_8.setGeometry(QRect(440, 550, 121, 31))
        self.label_VIP_8.setFont(font2)
        self.label_OtherParams_2 = QLabel(self.centralwidget)
        self.label_OtherParams_2.setObjectName(u"label_OtherParams_2")
        self.label_OtherParams_2.setGeometry(QRect(440, 470, 151, 31))
        self.label_OtherParams_2.setFont(font2)
        self.lineEdit_MConveyorSpeed = QLineEdit(self.centralwidget)
        self.lineEdit_MConveyorSpeed.setObjectName(u"lineEdit_MConveyorSpeed")
        self.lineEdit_MConveyorSpeed.setGeometry(QRect(560, 509, 141, 31))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(560, 550, 141, 31))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(560, 590, 141, 31))
        self.pushButton_Next = QPushButton(self.centralwidget)
        self.pushButton_Next.setObjectName(u"pushButton_Next")
        self.pushButton_Next.setGeometry(QRect(290, 660, 111, 41))
        font4 = QFont()
        font4.setPointSize(17)
        font4.setBold(True)
        self.pushButton_Next.setFont(font4)
        self.pushButton_Quit = QPushButton(self.centralwidget)
        self.pushButton_Quit.setObjectName(u"pushButton_Quit")
        self.pushButton_Quit.setGeometry(QRect(440, 660, 111, 41))
        self.pushButton_Quit.setFont(font4)
        InitialViewWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(InitialViewWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 846, 27))
        InitialViewWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(InitialViewWindow)
        self.statusbar.setObjectName(u"statusbar")
        InitialViewWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InitialViewWindow)


        QMetaObject.connectSlotsByName(InitialViewWindow)
    # setupUi

    def retranslateUi(self, InitialViewWindow):
        InitialViewWindow.setWindowTitle(QCoreApplication.translate("InitialViewWindow", u"MainWindow", None))
        self.label_top.setText(QCoreApplication.translate("InitialViewWindow", u"\u521d\u59cb\u5316", None))
        self.label_camera1.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a1\uff1a", None))
        self.label_camera2.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a2\uff1a", None))
        self.label_camera3.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a3\uff1a", None))
        self.label_camera4.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a4\uff1a", None))
        self.label_camera5.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a5\uff1a", None))
        self.label_PLC.setText(QCoreApplication.translate("InitialViewWindow", u"PLC:", None))
        self.label_curParams.setText(QCoreApplication.translate("InitialViewWindow", u"\u7cfb\u7edf\u5f53\u524d\u53c2\u6570\uff1a", None))
        self.label_curCameraParams.setText(QCoreApplication.translate("InitialViewWindow", u"\u5f53\u524d\u76f8\u673a\u53c2\u6570\uff1a", None))
        self.label_camera1_1.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a1\uff1a", None))
        self.pushButton_VCamera1.setText(QCoreApplication.translate("InitialViewWindow", u"\u67e5\u770b", None))
        self.label_camera2_1.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a2\uff1a", None))
        self.pushButton_VCamera2.setText(QCoreApplication.translate("InitialViewWindow", u"\u67e5\u770b", None))
        self.label_camera3_1.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a3\uff1a", None))
        self.pushButton_VCamera3.setText(QCoreApplication.translate("InitialViewWindow", u"\u67e5\u770b", None))
        self.label_camera4_1.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a4\uff1a", None))
        self.pushButton_VCamera4.setText(QCoreApplication.translate("InitialViewWindow", u"\u67e5\u770b", None))
        self.pushButton_VCamera5.setText(QCoreApplication.translate("InitialViewWindow", u"\u67e5\u770b", None))
        self.label_camera5_1.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a5\uff1a", None))
        self.pushButton_VIP.setText(QCoreApplication.translate("InitialViewWindow", u"\u67e5\u770b", None))
        self.label_VIP.setText(QCoreApplication.translate("InitialViewWindow", u"\u67e5\u770bIP\u5730\u5740\uff1a", None))
        self.label_OtherParams.setText(QCoreApplication.translate("InitialViewWindow", u"\u5176\u4ed6\u53c2\u6570\uff1a", None))
        self.label_VIP_2.setText(QCoreApplication.translate("InitialViewWindow", u"\u4f20\u9001\u5e26\u901f\u5ea6\uff1a", None))
        self.textBrowser_VConveyorSpeed.setHtml(QCoreApplication.translate("InitialViewWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_camera4_3.setHtml(QCoreApplication.translate("InitialViewWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_VIP_3.setText(QCoreApplication.translate("InitialViewWindow", u"*******\uff1a", None))
        self.textBrowser_camera4_4.setHtml(QCoreApplication.translate("InitialViewWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_VIP_4.setText(QCoreApplication.translate("InitialViewWindow", u"********\uff1a", None))
        self.label_curParams_2.setText(QCoreApplication.translate("InitialViewWindow", u"\u4fee\u6539\u7cfb\u7edf\u53c2\u6570\uff1a", None))
        self.label_curCameraParams_2.setText(QCoreApplication.translate("InitialViewWindow", u"\u4fee\u6539\u76f8\u673a\u53c2\u6570\uff1a", None))
        self.label_camera3_2.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a3\uff1a", None))
        self.pushButton_MCamera2.setText(QCoreApplication.translate("InitialViewWindow", u"\u4fee\u6539", None))
        self.label_camera4_2.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a4\uff1a", None))
        self.label_camera5_2.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a5\uff1a", None))
        self.pushButton_MCamera4.setText(QCoreApplication.translate("InitialViewWindow", u"\u4fee\u6539", None))
        self.pushButton_MCamera5.setText(QCoreApplication.translate("InitialViewWindow", u"\u4fee\u6539", None))
        self.label_camera2_2.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a2\uff1a", None))
        self.label_camera1_2.setText(QCoreApplication.translate("InitialViewWindow", u"\u76f8\u673a1\uff1a", None))
        self.pushButton_MCamera1.setText(QCoreApplication.translate("InitialViewWindow", u"\u4fee\u6539", None))
        self.pushButton_MCamera3.setText(QCoreApplication.translate("InitialViewWindow", u"\u4fee\u6539", None))
        self.label_VIP_5.setText(QCoreApplication.translate("InitialViewWindow", u"\u4fee\u6539IP\u5730\u5740\uff1a", None))
        self.pushButton_VIP_2.setText(QCoreApplication.translate("InitialViewWindow", u"\u4fee\u6539", None))
        self.label_VIP_6.setText(QCoreApplication.translate("InitialViewWindow", u"********\uff1a", None))
        self.label_VIP_7.setText(QCoreApplication.translate("InitialViewWindow", u"\u4f20\u9001\u5e26\u901f\u5ea6\uff1a", None))
        self.label_VIP_8.setText(QCoreApplication.translate("InitialViewWindow", u"*******\uff1a", None))
        self.label_OtherParams_2.setText(QCoreApplication.translate("InitialViewWindow", u"\u4fee\u6539\u5176\u4ed6\u53c2\u6570\uff1a", None))
        self.lineEdit_MConveyorSpeed.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.pushButton_Next.setText(QCoreApplication.translate("InitialViewWindow", u"\u7ee7\u7eed", None))
        self.pushButton_Quit.setText(QCoreApplication.translate("InitialViewWindow", u"\u9000\u51fa", None))
    # retranslateUi

