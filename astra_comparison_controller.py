import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import Qt
import astra_comparison_data as data
import astra_comparison_ui as ui


class AstraComparisonController(QtGui.QMainWindow):
    def __init__(self):
        super(AstraComparisonController, self).__init__()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.double_input_validator = QtGui.QDoubleValidator()
        self.integer_input_validator = QtGui.QIntValidator()
        self.data = data.AstraComparisonData()
        self.ui.runButton.clicked.connect(self.run_astra)
        self.show()

    def set_validators_for_all_line_edits_from_form_layout(self, line_edit_list):
        for line_edit in line_edit_list:
            if line_edit.objectName() == "macro_particle_line_edit":
                line_edit.setValidator(self.integer_input_validator)
            elif line_edit.objectName() == "directory_line_edit":
                pass
            else:
                line_edit.setValidator(self.double_input_validator)

    def get_all_line_edits_in_main_window(self):
        line_edit_list = []
        main_window = self.ui.centralwidget
        grid_layouts = main_window.children()
        for grid in grid_layouts:
            widget_list = grid.children()
            for widget in widget_list:
                if isinstance(widget, QtGui.QLineEdit):
                    line_edit_list.append(widget)
        return line_edit_list

    def get_all_check_boxes_in_main_window(self):
        check_box_list = []
        main_window = self.ui.centralwidget
        grid_layouts = main_window.children()
        for grid in grid_layouts:
            widget_list = grid.children()
            for widget in widget_list:
                if isinstance(widget, QtGui.QCheckBox):
                    check_box_list.append(widget)
        return check_box_list

    def collect_line_edit_text(self, line_edit_list):
        for line_edit in line_edit_list:
            object_name = str(line_edit.objectName()).replace('_line_edit', '')
            line_edit_text = str(line_edit.text())
            if line_edit.hasAcceptableInput():
                self.data.set_parameters(object_name, line_edit_text)
            else:
                print 'UNACCEPTABLE INPUT FOR:', object_name, "FIELD. "
                palette = QtGui.QPalette()
                palette.setColor(QtGui.QPalette.Base, QtCore.Qt.red)
                line_edit.setPalette(palette)
                
    def collect_check_box_state(self, check_box_list):
        for check_box in check_box_list:
            object_name = str(check_box.objectName()).replace('_check_box', '')
            if check_box.isChecked():
                self.data.set_parameters(object_name, 'T')
            else:
                self.data.set_parameters(object_name, 'F')

    def collect_parameters(self):
        line_edit_list = self.get_all_line_edits_in_main_window()
        check_box_list = self.get_all_check_boxes_in_main_window()
        self.set_validators_for_all_line_edits_from_form_layout(line_edit_list)
        self.collect_line_edit_text(line_edit_list)
        self.collect_check_box_state(check_box_list)

    def run_astra(self):
        # parameter values will be in a list gathered from
        # the QLineEdits due to input into ASTRA command
        self.collect_parameters()
        print(self.data.get_parameters())
        # self.check_parameters(self.data.get_parameters())
        # code to set up ASTRA command
        print 'RUN ASTRA CLICKED'

    def set_parameter_labels(parameter_labels, self):
        # Instead of hardcoding the parameter labels in the .ui file
        # we can just define a list of parameter strings here and set
        # the labels to them via python.
        print 'setParameterLabels method'

    def check_parameters(self):
        # here we will check that the values of the parameters are
        # of the correct type for the ASTRA command
        #    1) Needs to be of correct type
        #    2) Needs to be of realistic values
        #    3) ????
        print 'check_parameters method'
