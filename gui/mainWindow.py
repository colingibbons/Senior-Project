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

        self.plotWidget.mpl_connect('motion_notify_event', self.on_plotWidget_mouseMoved)
        self.plotWidget.mpl_connect('key_press_event', self.on_plotWidget_keyPressed)
        self.plotWidget.mpl_connect('button_press_event', self.on_plotWidget_clicked)

        self.setWindowTitle("BrewMaster Homebrewing Assistant")
        self.setWindowIcon(QIcon('beer_detail.png'))

        self.timeList = []
        self.tempList = []
        self.pHList = []


    @pyqtSlot()
    def on_plotWidget_mouseMoved(self, event):
        pass
        # print('on_sliceWidgetBMode_mouseMoved')

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

        headers = dataList[0]
        for i in range(1, len(dataList)):

            #extracts time, temperature, and pH data from the text file and categorizes the information into their own lists
            currentData = dataList[i].split(',')

            time = float(currentData[0].strip())
            self.timeList.append(time)

            temp = float(currentData[1].strip())
            self.tempList.append(temp)

            pH = float(currentData[2].strip())
            self.pHList.append(pH)

    @pyqtSlot(bool)
    def on_temperatureButton_toggled(self, checked):
        print("temperature box checked")
        if self.temperatureButton.isChecked() == False:
            self.plotWidget.clearFigure()

        if self.temperatureButton.isChecked():
            self.plotWidget.plotTemperature(self.timeList, self.tempList)
        if self.pHButton.isChecked():
            self.plotWidget.plotpH(self.timeList, self.pHList)

        if self.pHButton.isChecked() and self.temperatureButton.isChecked():
            self.plotWidget.clearFigure()
            self.plotWidget.plotBoth(self.timeList, self.tempList, self.pHList)

    @pyqtSlot(bool)
    def on_pHButton_toggled(self, checked):
        print('pH box checked')
        if self.pHButton.isChecked() == False:
            self.plotWidget.clearFigure()

        if self.pHButton.isChecked():
            self.plotWidget.plotpH(self.timeList, self.pHList)
        if self.temperatureButton.isChecked():
            self.plotWidget.plotTemperature(self.timeList, self.tempList)


        if self.temperatureButton.isChecked() and self.pHButton.isChecked():
            self.plotWidget.clearFigure()
            self.plotWidget.plotBoth(self.timeList, self.tempList, self.pHList)


