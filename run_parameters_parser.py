import astra_comparison_data


class ParameterParser:

    def __init__(self):
        self.data = astra_comparison_data.AstraComparisonData()
        self.parameters = self.data.get_parameters()
        self.input_file_name = 'runs_made.txt'

    def parse_parameter_input_file(self):
        parameters = []
        run_file = open(self.input_file_name, 'r')
        param_line_next = False
        for line in run_file:
            if param_line_next:
                parameters = line.split(' ')
                print parameters
            if 'run' in line:
                param_line_next = True
        print parameters


if __name__ == '__main__':
    parser = ParameterParser()
    parser.parse_parameter_input_file()
