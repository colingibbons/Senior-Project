import matplotlib
import numpy as np

matplotlib.use('Qt5Agg')
from PyQt5 import QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.patches as patches
from PyQt5.Qt import *
import matplotlib.pyplot as plt

import cv2
import imageio

class SliceWidget(FigureCanvas):
    def __init__(self, parent=None, dpi=100):
        # Create figure and axes, the axes should cover the entire figure size
        self.figure = Figure(dpi=dpi, frameon=False)
        self.axes = self.figure.add_axes((1/12, 1/12, 11/12, 11/12), facecolor='white')

        # Show the x and y axis
        self.axes.set_axis_on()


        # Initialize the parent FigureCanvas
        FigureCanvas.__init__(self, self.figure)
        self.setParent(parent)

        # Set widget to have strong focus to receive key press events
        self.setFocusPolicy(Qt.StrongFocus)

        # Create navigation toolbar and hide it
        # We don't want the user to see the toolbar but we are making our own in the user interface that will call
        # functions from the toolbar
        self.toolbar = NavigationToolbar(self, self)
        self.toolbar.hide()

        # Update size policy and geometry
        #FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        #FigureCanvas.updateGeometry(self)

    def plotTemperature(self, time, temp):

        #plots the temperature versus time
        self.axes.plot(time, temp, label='Temperature', color='red')
        self.draw()

    def plotpH(self, time, pH):

        #plots the pH versus time
        self.axes.plot(time, pH, label='pH', color='blue')
        self.draw()

    def plotBoth(self, tempTime, temp, pHTime, pH):

        self.figure, self.axes = plt.subplots(2,1)
        self.axes[0].plot(tempTime, temp, color='red')
        self.axes[0].set_title('Temperature')
        self.axes[1].plot(pHTime, pH, color='blue')
        self.axes[1].set_title('pH')

        self.draw()

    def clearFigure(self):

        self.axes = self.figure.add_axes((1 / 12, 1 / 12, 11 / 12, 11 / 12), facecolor='white')
        self.axes.clear()
        self.draw()

    def clearBoth(self):

        self.axes[0].clear()
        self.axes[1].clear()
        self.draw()