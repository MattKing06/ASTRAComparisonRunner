import PyQt4.Qt as Qt
import astra_comparison_data as data
import astra_comparison_ui as ui
import run_parameters_parser as yaml_parser


class AstraComparisonController(Qt.QMainWindow):
    def __init__(self):
        super(AstraComparisonController, self).__init__()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.double_input_validator = Qt.QDoubleValidator()
        self.integer_input_validator = Qt.QIntValidator()
        self.data = data.AstraComparisonData()
        self.ui.runButton.clicked.connect(self.run_astra)
        self.ui.actionImport_YAML.triggered.connect(self.import_parameter_values_from_yaml_file)
        self.ui.actionExport_YAML.triggered.connect(self.export_parameter_values_to_yaml_file)
        self.show()

    def import_parameter_values_from_yaml_file(self):
        dialog = Qt.QFileDialog()
        filename = Qt.QFileDialog.getOpenFileName(dialog, caption='Open file',
                                                  directory='c:\\', filter="YAML files (*.YAML *.YML *.yaml *.yml)")
        if not filename.isEmpty():
            loaded_parameter_list = yaml_parser.parse_parameter_input_file(filename)
            line_edit_list = self.get_all_line_edits_in_main_window()
            self.set_all_line_edits_in_main_window(line_edit_list, loaded_parameter_list)
            check_box_list = self.get_all_check_boxes_in_main_window()
            self.set_all_check_boxes_in_main_window(check_box_list, loaded_parameter_list)
        else:
            print 'Failed to import, please provide a filename.'

    def export_parameter_values_to_yaml_file(self):
        dialog = Qt.QFileDialog()
        dialog.setFileMode(Qt.QFileDialog.DirectoryOnly)
        filename, _filter = Qt.QFileDialog.getSaveFileNameAndFilter(dialog, caption='Save File', directory='c:\\',
                                                                    filter="YAML Files (*.YAML *.YML *.yaml *.yml")
        # we have a validation check in collect_line_edit_text() called by collect_parameters()
        # so if a value isn't valid, that entry for the data.parameters is not set.
        #
        # Currently, this means that if we have an invalid input, the yaml file isn't written out.
        # However, all of this is implicit. So need to find a way to explicitly validate for YAML exporting
        if not filename.isEmpty():
            self.collect_parameters()
            parameter_values = self.data.get_parameters()
            # IF validate(parameter_values) THEN:
            yaml_parser.write_parameter_output_file(filename, parameter_values)
            # ELSE: RAISE EXCEPTION/DISPLAY INVALID INPUT TO USER
        else:
            print 'Failed to export, please provide a filename.'

    def set_validators_for_all_line_edits_from_form_layout(self, line_edit_list):
        for line_edit in line_edit_list:
            if line_edit.objectName() == "macro_particle_line_edit":
                line_edit.setValidator(self.integer_input_validator)
            elif line_edit.objectName() == "directory_line_edit":
                pass
            else:
                line_edit.setValidator(self.double_input_validator)

    @staticmethod
    def set_all_line_edits_in_main_window(line_edit_list, values_to_set_dict):
        print values_to_set_dict
        for line_edit in line_edit_list:
            # our YAML values dict has keys without the '_line_edit' suffix, so we must add this suffix to
            # access the line_edit dict which has keys containing the '_line_edit' suffix.
            parameter_value_str = str(values_to_set_dict[str(line_edit.objectName()).replace('_line_edit', '')])
            line_edit.setText(parameter_value_str)

    @staticmethod
    def set_all_check_boxes_in_main_window(check_box_list, values_to_set_dict):
        for check_box in check_box_list:
            # our YAML values dict has keys without the '_check_box' suffix, so we must add this suffix to
            # access the check_box_list dict which has keys containing the '_check_box' suffix.
            parameter_value_str = str(values_to_set_dict[str(check_box.objectName()).replace('_check_box', '')])
            # now we convert from T/F to Checked/Unchecked for the check-boxes
            if parameter_value_str == 'T':
                check_box.setChecked(True)
            elif parameter_value_str == 'F':
                check_box.setChecked(False)

    def get_all_line_edits_in_main_window(self):
        line_edit_list = []
        main_window = self.ui.centralwidget
        # gather all the children of the central widget
        # which will be the gird layouts containing the line-edits
        # and check-box widgets
        grid_layouts = main_window.children()
        for widget in grid_layouts:
            if isinstance(widget, Qt.QLineEdit):
                line_edit_list.append(widget)
        return line_edit_list

    def get_all_check_boxes_in_main_window(self):
        check_box_list = []
        main_window = self.ui.centralwidget
        # gather all the children of the central widget
        # which will be the gird layouts containing the line-edits
        # and check-box widgets
        grid_layouts = main_window.children()
        for widget in grid_layouts:
            if isinstance(widget, Qt.QCheckBox):
                check_box_list.append(widget)
        return check_box_list

    def collect_line_edit_text(self, line_edit_list):
        for line_edit in line_edit_list:
            object_name = str(line_edit.objectName()).replace('_line_edit', '')
            line_edit_text = str(line_edit.text())
            print line_edit_text
            if line_edit.hasAcceptableInput():
                self.data.set_parameters(object_name, line_edit_text)
            else:
                print 'UNACCEPTABLE INPUT FOR:', object_name, "FIELD. "
                palette = Qt.QPalette()
                palette.setColor(Qt.QPalette.Base, Qt.QColor('red'))
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

    @staticmethod
    def set_parameter_labels(parameter_labels, self):
        # Instead of hard-coding the parameter labels in the .ui file
        # we can just define a list of parameter strings here and set
        # the labels to them via python.
        print 'setParameterLabels method'

