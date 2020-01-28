# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


app = QApplication([])
label = QLabel("Oh my god it's happening!")
label.show()
sys.exit(app.exec_())
