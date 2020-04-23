import os
import logging
import numpy as np
import imageio

import yaml
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as figureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as navigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from util.fileDialog import FileDialog
from generated import mainWindow_ui
from pathlib import Path
from util import constants, util
import random

logger = logging.getLogger(__name__)


# class for main window of UI
class MainWindow(QMainWindow, mainWindow_ui.Ui_BrewMaster):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        #self.plotWidget.mpl_connect('motion_notify_event', self.on_plotWidget_mouseMoved)
        #self.plotWidget.mpl_connect('key_press_event', self.on_plotWidget_keyPressed)
        #self.plotWidget.mpl_connect('button_press_event', self.on_plotWidget_clicked)

        self.setWindowTitle("BrewMaster Homebrewing Assistant")
        self.setWindowIcon(QIcon('beer_detail.png'))

        self.tempTimeList = []
        self.pHTimeList = []
        self.tempList = []
        self.pHList = []
        self.averageTemp = 0
        self.averagepH = 0
        self.maximumTemp = 0
        self.minimumTemp = 0
        self.maximumpH = 0
        self.minimumpH = 0




    def dataStats(self):

        #Finds the min and max temp
        self.maximumTemp = max(self.tempList)
        self.minimumTemp = min(self.tempList)

        #Finds average temp
        tempSum = 0
        for i in range(len(self.tempList)):
            tempSum = tempSum + self.tempList[i]
            self.averageTemp = tempSum/(len(self.tempList))

        #Finds min and max pH
        self.maximumpH = max(self.pHList)
        self.minimumpH = min(self.pHList)

        #Finds average pH
        pHSum = 0
        for i in range(len(self.pHList)):
            pHSum = pHSum + self.pHList[i]
            self.averagepH = pHSum/(len(self.pHList))


    @pyqtSlot()
    def on_plotWidget_mouseMoved(self, event):
        pass


    @pyqtSlot()
    def on_plotWidget_keyPressed(self, event):
        pass

    @pyqtSlot()
    def on_plotWidget_clicked(self, event):
        pass

    @pyqtSlot()
    def on_searchForData_clicked(self):
        # Opens file explorer so user can select text file containing brew data
        fileNameFullPath = FileDialog.getOpenFileName(self, 'Select Brew Data File',
                                                      '', '*.txt')

        # extracts file path from tuple and reformats path to be usable with python file library
        cleanPath = Path(fileNameFullPath[0])

        # populates text box with path of chosen file, opens the file, and reads contents line-by-line
        self.dataSearchText.setText(str(cleanPath))
        file = open(cleanPath, 'r')
        dataList = file.read().splitlines()

        tempReadingTime = dataList[0].split(':')
        tempInterval = int(tempReadingTime[1])
        pHReadingTime = dataList[1].split(':')
        pHInterval = int(pHReadingTime[1])
        for i in range(2, len(dataList)):

            #extracts time, temperature, and pH data from the text file and categorizes the information into their own lists
            currentData = dataList[i].split(':')

            dataType = (currentData[0].strip())

            if 'T' in dataType:

                index = int(dataType[1:])
                tempTime = int(index * tempInterval)
                self.tempTimeList.append(tempTime)

                temp = float(currentData[1].strip())
                self.tempList.append(temp)

            if 'P' in dataType:

                index = int(dataType[1:])
                pHTime = int(index * pHInterval)
                self.pHTimeList.append(pHTime)

                pH = float(currentData[1].strip())
                self.pHList.append(pH)

        self.dataStats()
        self.avgTemp.setText("Average Temperature: %.2f" % self.averageTemp)
        self.avgpH.setText("Average pH: %.2f" % self.averagepH)
        self.maxTemp.setText("Maximum Temperature: %.2f" % self.maximumTemp)
        self.maxpH.setText("Maximum pH: %.2f" % self.maximumpH)
        self.minTemp.setText("Minimum Temperature: %.2f" % self.minimumTemp)
        self.minpH.setText("Minimum pH: %.2f" % self.minimumpH)


    @pyqtSlot(bool)
    def on_temperatureButton_toggled(self, checked):
        print("temperature box checked")
        if self.temperatureButton.isChecked() == False:
            self.plotWidget.setCurrentIndex(1)
            if self.pHButton.isChecked() == False:
                self.pHPlot.clearFigure()


        if self.temperatureButton.isChecked():
            self.plotWidget.setCurrentIndex(0)
            self.tempPlot.plotTemperature(self.tempTimeList, self.tempList)
        if self.pHButton.isChecked():
            self.plotWidget.setCurrentIndex(1)
            self.pHPlot.plotpH(self.pHTimeList, self.pHList)

        if self.pHButton.isChecked() and self.temperatureButton.isChecked():
            self.plotWidget.setCurrentIndex(2)
            self.bothPlot.plotBoth(self.tempTimeList, self.tempList, self.pHTimeList, self.pHList)

    @pyqtSlot(bool)
    def on_pHButton_toggled(self, checked):
        print('pH box checked')
        if self.pHButton.isChecked() == False:
            self.plotWidget.setCurrentIndex(0)
            if self.temperatureButton.isChecked() == False:
                self.tempPlot.clearFigure()

        if self.pHButton.isChecked():
            self.plotWidget.setCurrentIndex(1)
            self.pHPlot.plotpH(self.pHTimeList, self.pHList)
        if self.temperatureButton.isChecked():
            self.plotWidget.setCurrentIndex(0)
            self.tempPlot.plotTemperature(self.tempTimeList, self.tempList)


        if self.temperatureButton.isChecked() and self.pHButton.isChecked():
            self.plotWidget.setCurrentIndex(2)
            self.bothPlot.plotBoth(self.tempTimeList, self.tempList, self.pHTimeList, self.pHList)


