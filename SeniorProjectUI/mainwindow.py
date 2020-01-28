# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BrewMaster(object):
    def setupUi(self, BrewMaster):
        BrewMaster.setObjectName("BrewMaster")
        BrewMaster.resize(771, 557)
        self.centralwidget = QtWidgets.QWidget(BrewMaster)
        self.centralwidget.setObjectName("centralwidget")
        self.Separator = QtWidgets.QFrame(self.centralwidget)
        self.Separator.setGeometry(QtCore.QRect(250, 0, 20, 571))
        self.Separator.setFrameShape(QtWidgets.QFrame.VLine)
        self.Separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Separator.setObjectName("Separator")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 200, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 0, 511, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tempWidget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.tempWidget.setObjectName("tempWidget")
        self.verticalLayout.addWidget(self.tempWidget)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(260, 260, 509, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(260, 260, 511, 271))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.phWidget = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.phWidget.setObjectName("phWidget")
        self.verticalLayout_2.addWidget(self.phWidget)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 261, 261))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        BrewMaster.setCentralWidget(self.centralwidget)

        self.retranslateUi(BrewMaster)
        QtCore.QMetaObject.connectSlotsByName(BrewMaster)

    def retranslateUi(self, BrewMaster):
        _translate = QtCore.QCoreApplication.translate
        BrewMaster.setWindowTitle(_translate("BrewMaster", "MainWindow"))
        self.textEdit.setHtml(_translate("BrewMaster", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; color:#5500ff;\">WELCOME TO THE BREWMASTER</span></p></body></html>"))
        self.pushButton.setText(_translate("BrewMaster", "Don\'t Push"))
