from collections import OrderedDict


class AstraComparisonData:

    def __init__(self):
        self.parameters = OrderedDict([('astra_run_number', ''), ('macro_particle', ''), ('laser_pulse_length', ''),
                                       ('spot_size', ''), ('charge', ''), ('gun_gradient', ''), ('gun_phase', ''),
                                       ('linac1_gradient', ''), ('linac1_phase', ''),
                                       ('bucking_coil_and_sol_strength', ''), ('linac1_sol1_strength', ''),
                                       ('linac1_sol2_strength', ''), ('end_of_line', ''),
                                       ('injector_space_charge', 'T'), ('s02_quad1_strength', ''),
                                       ('s02_quad2_strength', ''), ('s02_quad3_strength', ''),
                                       ('s02_quad4_strength', ''), ('c2v_quad1_strength', ''),
                                       ('c2v_quad2_strength', ''), ('c2v_quad3_strength', ''),
                                       ('vela_quad1_strength', ''), ('vela_quad2_strength', ''),
                                       ('vela_quad3_strength', ''), ('vela_quad4_strength', ''),
                                       ('vela_quad5_strength', ''), ('vela_quad6_strength', ''),
                                       ('ba1_quad1_strength', ''), ('ba1_quad2_strength', ''),
                                       ('ba1_quad3_strength', ''), ('ba1_quad4_strength', ''),
                                       ('ba1_quad5_strength', ''), ('ba1_quad6_strength', ''),
                                       ('ba1_quad7_strength', ''), ('rest_of_line_space_charge', ''),
                                       ('directory', '')])
        self.commands = []

    def set_parameters(self, key, value):
        self.parameters[key] = value

    def get_parameters(self):
        return self.parameters

    def set_commands(self, commands):
        self.commands = commands
