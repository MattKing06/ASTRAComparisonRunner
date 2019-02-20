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
		self.parameters = []
		self.show()

	def run_astra(parameters, self):
	# parameter values will be in a list gathered from
	# the QLineEdits due to input into ASTRA command
		parameters = astra_runner_window.collect_parameters()
		print astra_runner_window.parameters
		astra_runner_window.check_parameters(parameters)
		#code to set up ASTRA command
		print 'RUN ASTRA CLICKED'
		last_run_parameters = parameters
		astra_runner_window.parameters = []

	def set_parameter_labels(parameter_labels, self):
	# Instead of hardcoding the parameter labels in the .ui file
	# we can just define a list of parameter strings here and set
	# the labels to them via python.
		print 'setParameterLabels method'

	def collect_parameters(self):
		#Grab all of the formLayouts that are in the grid layout
		#we have 4 of them in one gridlayout
		form_layout_list = self.ui.gridLayout.children()
		
		#go through the forms and get all of the children (QWidgets) that 
		# are contained within that form
		for form in form_layout_list:
			number_of_elements = form.count()
			for i in range(0,number_of_elements):
				#if we have a QLineEdit then put its text into the parameter list
				 if isinstance(form.itemAt(i).widget(), QtGui.QLineEdit):
					 astra_runner_window.parameters.append(str(form.itemAt(i).widget().text()))
				# if we have a QLabel then we just pass over it (we can maybe do something with this)
				 elif isinstance(form.itemAt(i).widget(), QtGui.QLabel):
					pass
				# if we have neither, we have clearly gone wrong somewhere
				# so just output an error message to cmd-line (could be a splash screen), and exit the GUI
				 else:
					print "Cannot Access GUI Component, please inform a developer."
					sys.exit(0)

	def check_parameters(parameters, self):
	# here we will check that the values of the parameters are
	# of the correct type for the ASTRA command
	#    1) Needs to be of correct type
	#    2) Needs to be of realistic values
	#    3) ????
		print 'check_parameters method'

if __name__ == '__main__':
	application = QtGui.QApplication(sys.argv)
	astra_runner_window = MyWindow()
	sys.exit(application.exec_())
