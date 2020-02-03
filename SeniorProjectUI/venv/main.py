from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from SeniorProjectUI.mainwindow import Ui_BrewMaster

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        ui = Ui_BrewMaster()
        ui.setupUi(self)
        self.setWindowTitle("BrewMaster Homebrewing Assistant")
        self.setWindowIcon(QIcon('beer_detail.png'))


    @pyqtSlot()
    def on_pushButton_clicked(self):
        print("hi")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


