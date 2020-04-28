import argparse
import distutils.util as util

'''
Generic class for us to add our parameters to execute our code via command line (standard I/O).
This is particular important to use the standard I/O and scripts.
With the parameter definitions we can better organize what are the required components/paramters so our 
    code runs.
'''


class CommandLine:

    def __init__(self):
        """
        Arguments for command line - standard input and output
        The names of the parameters under args.X are the ones we defined under
            "dest" in "command_line_parameters(self)"
        For the other flags please take a look at:
            https://docs.python.org/3/library/argparse.html#the-add-argument-method
        Some data types need to be properly processed, such as bool, that needs to be parsed from string
            into bool
        """
        parser = self.command_line_parameters()
        args = parser.parse_args()
        self.input_folder = args.inf
        self.output_folder = args.ouf
        self.flag_switch = args.flag
        self.number = args.num

    def command_line_parameters(self):
        """
        parameter list for command line
        """
        parser = argparse.ArgumentParser(description="Default command line for standard input and output")
        parser.add_argument('--input', '-i', type=str, action='store', dest='inf', metavar='<path>',
                            required=True,
                            help='Provide the desired input folder.')
        parser.add_argument('--output', '-o', type=str, action='store', dest='ouf', metavar='<path>',
                            required=True, help='Provide the desired input folder')
        parser.add_argument('--flag', '-f', type=util.strtobool, action='store', dest='flag', metavar='<parameter>',
                            required=False, default=False,
                            help='[optional] Flag value True or False (Default: False).',
                            choices=[True, False])
        parser.add_argument('--number', '-n', type=int, action='store', dest='num', metavar='<value>',
                            required=False, default=42,
                            help='[optional] Provide a random seed number (0, 1 or 42).\n'
                                 'If none is provided "42" will be used',
                            choices=[0, 1, 42])
        return parser

