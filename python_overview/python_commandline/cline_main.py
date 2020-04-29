import sys
import os
''' 
The line below is used to adjust the relative path of our current main.py to the parent folder. 
    We are basically setting up the PYTHONPATH. That way, when Python looks for the package it will find it.
If you are using an IDE you don't have to worry about it, almost of them do this automatically.
However, via command line  you can either:
    1. Include the the path to your module in PYTHONPATH;
    2. Use the line below to set the new path. It is important do to this before the import from other 
    packages and scripts you are importing in your program.
'''
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

from python_commandline.cline_base import CommandLine

# Main block
if __name__ == "__main__":
    command_line = CommandLine()

    # IO and default logs
    input_folder = command_line.input_folder
    output_folder = command_line.output_folder
    numbers = command_line.number
    flag_used = command_line.flag_switch

    # Helper explanation
    '''
    When we call our main.py with the -h parameter, the following result is observed
    
        $python3 cline_main.py --help
        >   cline_main.py [-h] --input <path> --output <path> [--flag <parameter>]
                             [--number <value>] 
                             ...
     Even though the help-output shows all of them as "optional parameters" it's because of their 
     grouping. This website explains in details all about arparse
        https://pymotw.com/2/argparse/
                         
    All optional parameters are enclosed with the [], the ones without it are required.
    
    '''

    print("Input folder: ", input_folder)
    print("Output folder: ", output_folder)
    print("Number: ", numbers)
    print("Flag-used: ", flag_used)

    # output observation
    '''
        Run the command below to see the actual output.
            $python3 cline_main.py -i f1 -o f1 -dummy True -n 42
            >   Input folder:  f1
                Output folder:  f1
                Number:  42
                Flag-used:  1
    '''

