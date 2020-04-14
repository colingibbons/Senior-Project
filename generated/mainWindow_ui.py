# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USER\PycharmProjects\Senior-Project\gui\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BrewMaster(object):
    def setupUi(self, BrewMaster):
        BrewMaster.setObjectName("BrewMaster")
        BrewMaster.resize(880, 611)
        self.centralwidget = QtWidgets.QWidget(BrewMaster)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 0, 401, 71))
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
        self.plotWidget = SliceWidget(self.centralwidget)
        self.plotWidget.setGeometry(QtCore.QRect(60, 170, 601, 411))
        self.plotWidget.setMouseTracking(False)
        self.plotWidget.setTabletTracking(False)
        self.plotWidget.setObjectName("plotWidget")
        self.pHButton = QtWidgets.QCheckBox(self.centralwidget)
        self.pHButton.setGeometry(QtCore.QRect(240, 130, 81, 16))
        self.pHButton.setObjectName("pHButton")
        self.temperatureButton = QtWidgets.QCheckBox(self.centralwidget)
        self.temperatureButton.setGeometry(QtCore.QRect(140, 130, 81, 16))
        self.temperatureButton.setObjectName("temperatureButton")
        self.label.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.pHButton.raise_()
        self.temperatureButton.raise_()
        self.plotWidget.raise_()
        BrewMaster.setCentralWidget(self.centralwidget)

        self.retranslateUi(BrewMaster)
        QtCore.QMetaObject.connectSlotsByName(BrewMaster)

    def retranslateUi(self, BrewMaster):
        _translate = QtCore.QCoreApplication.translate
        BrewMaster.setWindowTitle(_translate("BrewMaster", "MainWindow"))
        self.label.setText(_translate("BrewMaster", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Welcome to the BrewMaster Homebrewing <br> Assistant!</span></p></body></html>"))
        self.searchLabel.setText(_translate("BrewMaster", "Select Data to Import"))
        self.searchForData.setText(_translate("BrewMaster", "Browse"))
        self.pHButton.setText(_translate("BrewMaster", "pH"))
        self.temperatureButton.setText(_translate("BrewMaster", "Temperature"))
from gui.sliceWidget import SliceWidget
