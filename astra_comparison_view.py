from PyQt4.QtGui import QMainWindow, QApplication
from PyQt4 import QtGui, uic
import sys
ui_main_window, QtBaseClass = uic.loadUiType('astra_comparison_gui.ui')


class AstraComparisonView(QMainWindow):

    def __init__(self):
        # what components will we access the most?
        # - QLineEdits
        # - Run button
        # - Grid/Form Layouts
        #
        # maybe store a list of the names for each of these so we can access by area?

