# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 170, 255, 255));\n"
"")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 340, 201, 51))
        self.lineEdit.setStyleSheet("background-color: rgb(247, 250, 255);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 320, 91, 31))
        self.pushButton.setStyleSheet("\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.reset = QtWidgets.QPushButton(self.centralWidget)
        self.reset.setGeometry(QtCore.QRect(680, 360, 91, 31))
        self.reset.setStyleSheet("\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"")
        self.lineEdit.setText("Canada")



        self.reset.setObjectName("reset")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 510, 1431, 450))
        self.textEdit_2.setStyleSheet("background-color: rgb(215, 253, 255);;\n"
"font: 12pt \"Berlin Sans FB\";\n"
"")
        self.textEdit_2.setText("")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(680, 160, 491, 91))
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"background-color: rgb(0, 89, 133);\n"
"    border-color: rgb(0, 91, 136);\n"
"border: 1px solid black;\n"
"     border-radius: 5px;\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 430, 201, 51))
        self.lineEdit_3.setStyleSheet("background-color: rgb(247, 250, 255);\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.reset_2 = QtWidgets.QPushButton(self.centralWidget)
        self.reset_2.setGeometry(QtCore.QRect(680, 450, 91, 31))
        self.reset_2.setStyleSheet("\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"")
        self.reset_2.setObjectName("reset_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 410, 91, 31))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1000, 320, 91, 31))
        self.pushButton_3.setStyleSheet("\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.reset_3 = QtWidgets.QPushButton(self.centralWidget)
        self.reset_3.setGeometry(QtCore.QRect(1000, 360, 91, 31))
        self.reset_3.setStyleSheet("\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"")
        self.reset_3.setObjectName("reset_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(790, 340, 201, 51))
        self.lineEdit_4.setStyleSheet("background-color: rgb(247, 250, 255);\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(500, 310, 151, 20))
        self.label.setStyleSheet("  background-color: rgb(175, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(500, 400, 151, 20))
        self.label_2.setStyleSheet("  background-color: rgb(175, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(790, 310, 201, 20))
        self.label_3.setStyleSheet("  background-color: rgb(175, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.reset_4 = QtWidgets.QPushButton(self.centralWidget)
        self.reset_4.setGeometry(QtCore.QRect(1300, 450, 91, 31))
        self.reset_4.setStyleSheet("\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"")
        self.reset_4.setObjectName("reset_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1300, 410, 91, 31))
        self.pushButton_4.setStyleSheet("\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"")
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(1130, 430, 131, 21))
        self.lineEdit_5.setStyleSheet("background-color: rgb(247, 250, 255);\n"
"")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(1120, 400, 151, 20))
        self.label_4.setStyleSheet("  background-color: rgb(175, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(1130, 460, 131, 21))
        self.lineEdit_6.setStyleSheet("background-color: rgb(247, 250, 255);\n"
"")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(1120, 280, 151, 20))
        self.label_5.setStyleSheet("  background-color: rgb(175, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1300, 320, 91, 31))
        self.pushButton_5.setStyleSheet("\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"")
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(1130, 340, 131, 21))
        self.lineEdit_7.setStyleSheet("background-color: rgb(247, 250, 255);\n"
"")

        self.lineEdit_25 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_25.setGeometry(QtCore.QRect(1130, 310, 131, 21))
        self.lineEdit_25.setStyleSheet("background-color: rgb(247, 250, 255);\n"
                                      "")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.reset_5 = QtWidgets.QPushButton(self.centralWidget)
        self.reset_5.setGeometry(QtCore.QRect(1300, 360, 91, 31))
        self.reset_5.setStyleSheet("\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"")
        self.reset_5.setObjectName("reset_5")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(1130, 370, 131, 21))
        self.lineEdit_8.setStyleSheet("background-color: rgb(247, 250, 255);\n"
"")
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.reset_6 = QtWidgets.QPushButton(self.centralWidget)
        self.reset_6.setGeometry(QtCore.QRect(1000, 450, 91, 31))
        self.reset_6.setStyleSheet("\n"

"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"")
        self.reset_6.setObjectName("reset_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1000, 410, 91, 31))
        self.pushButton_6.setStyleSheet("\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}\n"
"")
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(790, 430, 201, 51))
        self.lineEdit_9.setStyleSheet("background-color: rgb(247, 250, 255);\n"
"")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_26.setGeometry(QtCore.QRect(1430, 330, 131, 45))
        self.lineEdit_26.setStyleSheet("background-color: rgb(247, 250, 255);\n"
                                       "")
        self.lineEdit_26.setObjectName("lineEdit_26")

        self.reset_25 = QtWidgets.QPushButton(self.centralWidget)
        self.reset_25.setGeometry(QtCore.QRect(1575, 360, 91, 31))
        self.reset_25.setStyleSheet("\n"
       "QPushButton:pressed {\n"
       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
       "}\n"
       "QPushButton {\n"
       "     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
       "     border-radius: 5px;\n"
       "     font: 75 14pt \"Verdana\";\n"
       "}\n"
       "\n"
       "QPushButton:disabled {\n"
       "    background-color: rgb(170, 170, 127)\n"
       "}\n"
       "")
        self.reset_25.setObjectName("reset_25")
        self.label_25 = QtWidgets.QLabel(self.centralWidget)
        self.label_25.setGeometry(QtCore.QRect(1430, 290, 140, 20))
        self.label_25.setStyleSheet("  background-color: rgb(175, 230, 255); border: 1px solid black;\n"
                                   "     border-radius: 5px;\n"
                                   "     font: 75 14pt \"Arial\";")
        self.label_25.setObjectName("label_25")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_25.setGeometry(QtCore.QRect(1575, 320, 91, 31))
        self.pushButton_25.setStyleSheet("\n"
    "QPushButton:pressed {\n"
    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))\n"
    "}\n"
    "QPushButton {\n"
    "     background-color: rgb(211, 230, 255); border: 1px solid black;\n"
    "     border-radius: 5px;\n"
    "     font: 75 14pt \"Verdana\";\n"
    "}\n"
    "\n"
    "QPushButton:disabled {\n"
    "    background-color: rgb(170, 170, 127)\n"
    "}\n"
    "")
        self.pushButton_25.setAutoDefault(False)
        self.pushButton_25.setDefault(False)
        self.pushButton_25.setObjectName("pushButton_25")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(790, 400, 201, 20))
        self.label_6.setStyleSheet("  background-color: rgb(175, 230, 255); border: 1px solid black;\n"
"     border-radius: 5px;\n"
"     font: 75 14pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def getText1(self):
        text1 = self.lineEdit.text()

        return text1

    def getText2(self):
        text2 = self.lineEdit_2.text()

        return text2

    def setText2(self, sText2):
        self.textEdit_2.setText(sText2)

    def getText3(self):
        text3 = self.lineEdit_3.text()

        return text3

    def getText4(self):
        text4 = self.lineEdit_4.text()

        return text4

    def getText5(self):
        text5 = self.lineEdit_5.text()

        return text5
    def getText6(self):
        text6 = self.lineEdit_6.text()

        return text6
    def getText7(self):
        text7 = self.lineEdit_7.text()

        return text7
    def getText8(self):
        text8 = self.lineEdit_8.text()

        return text8
    def getText25(self):
        text25 = self.lineEdit_25.text()

        return text25
    def getText9(self):
        text9 = self.lineEdit_9.text()

        return text9

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; color:#f0f0ff;\">CSV PARSER</span></p></body></html>"))
        self.reset_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_2.setText(_translate("MainWindow", "Submit"))
        self.pushButton_3.setText(_translate("MainWindow", "Submit"))
        self.reset_3.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "Isolate Row"))
        self.label_2.setText(_translate("MainWindow", "Isolate Column"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Find Key in Row</p></body></html>"))
        self.reset_4.setText(_translate("MainWindow", "Reset"))
        self.pushButton_4.setText(_translate("MainWindow", "Submit"))
        self.lineEdit_5.setText(_translate("MainWindow", "col 1 (x)"))
        self.label_4.setText(_translate("MainWindow", "Plot Columns"))
        self.lineEdit_6.setText(_translate("MainWindow", "col 2 (y)"))
        self.label_5.setText(_translate("MainWindow", "Thresholds"))
        self.pushButton_5.setText(_translate("MainWindow", "Submit"))
        self.lineEdit_7.setText(_translate("MainWindow", "Lower Threshold"))
        self.reset_5.setText(_translate("MainWindow", "Reset"))
        self.lineEdit_8.setText(_translate("MainWindow", "Upper Threshold"))
        self.reset_6.setText(_translate("MainWindow", "Reset"))
        self.pushButton_6.setText(_translate("MainWindow", "Submit"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Find Key in Column</p></body></html>"))
        self.reset_25.setText(_translate("MainWindow", "Reset"))
        self.lineEdit_26.setText(_translate("MainWindow", "key"))
        self.label_25.setText(_translate("MainWindow", "Find Key in All"))
        self.pushButton_25.setText(_translate("MainWindow", "Submit"))

