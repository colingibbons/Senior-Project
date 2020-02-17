# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Colin Gibbons\PycharmProjects\Senior-Project\gui\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BrewMaster(object):
    def setupUi(self, BrewMaster):
        BrewMaster.setObjectName("BrewMaster")
        BrewMaster.resize(840, 579)
        self.centralwidget = QtWidgets.QWidget(BrewMaster)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 0, 401, 71))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 70, 401, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.searchLabel.setObjectName("searchLabel")
        self.horizontalLayout_2.addWidget(self.searchLabel)
        self.dataSearchText = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.dataSearchText.setObjectName("dataSearchText")
        self.horizontalLayout_2.addWidget(self.dataSearchText)
        self.searchForData = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.searchForData.setObjectName("searchForData")
        self.horizontalLayout_2.addWidget(self.searchForData)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(150, 120, 161, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tempButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.tempButton.setObjectName("tempButton")
        self.horizontalLayout_3.addWidget(self.tempButton)
        self.pHButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.pHButton.setObjectName("pHButton")
        self.horizontalLayout_3.addWidget(self.pHButton)
        self.plotWidget = QtWidgets.QWidget(self.centralwidget)
        self.plotWidget.setGeometry(QtCore.QRect(0, 230, 841, 351))
        self.plotWidget.setObjectName("plotWidget")
        BrewMaster.setCentralWidget(self.centralwidget)

        self.retranslateUi(BrewMaster)
        QtCore.QMetaObject.connectSlotsByName(BrewMaster)

    def retranslateUi(self, BrewMaster):
        _translate = QtCore.QCoreApplication.translate
        BrewMaster.setWindowTitle(_translate("BrewMaster", "MainWindow"))
        self.label.setText(_translate("BrewMaster", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Welcome to the BrewMaster Homebrewing <br> Assistant!</span></p></body></html>"))
        self.searchLabel.setText(_translate("BrewMaster", "Select Data to Import"))
        self.searchForData.setText(_translate("BrewMaster", "Browse"))
        self.tempButton.setText(_translate("BrewMaster", "Temperature"))
        self.pHButton.setText(_translate("BrewMaster", "pH"))
