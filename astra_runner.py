import sys
from PyQt4.QtGui import QMainWindow, QApplication
from PyQt4 import QtGui, uic


ui_main_window, QtBaseClass = uic.loadUiType('astra_comparison_gui.ui')

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.ui = ui_main_window()
		self.ui.setupUi(self)
		self.ui.runButton.clicked.connect(self.run_astra)
		self.show()
	
	def setParameterLabels(parameter_labels, self):
	# Instead of hardcoding the parameter labels in the .ui file
	# we can just define a list of parameter strings here and set
	# the labels to them via python.
	
	def collect_parameters(self):
	# here we can just grab all of the inputs from the QLineEdits
	# and put them into a list to be passed to 'run_astra' function
	
	def check_parameters(parameters, self):
	# here we will check that the values of the parameters are 
	# of the correct type for the ASTRA command
	#    1) Needs to be of correct type
	#    2) Needs to be of realistic values
	#    3) ????
	
	def run_astra(parameters, self):
	# parameter values will be in a list gathered from
	# the QLineEdits due to input into ASTRA command
		print 'RUN ASTRA CLICKED'
		
		
if __name__ == '__main__':
	application = QtGui.QApplication(sys.argv)
	astra_runner_window = MyWindow()
	sys.exit(application.exec_())
