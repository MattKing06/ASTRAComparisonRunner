import sys
from PyQt4.QtGui import QMainWindow, QApplication
from PyQt4 import QtGui, uic
import astra_comparison_controller as controller


if __name__ == '__main__':
    application = QtGui.QApplication(sys.argv)
    astra_runner_window = controller.AstraComparisonController()
    sys.exit(application.exec_())
