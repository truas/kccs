import unittest
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

from python_unit_testing.names import Names

class NamesTestCase(unittest.TestCase):
    """Tests for 'names.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        name_obj = Names()
        formatted_name = name_obj.get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        name_obj = Names()
        formatted_name = name_obj.get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

# Reference code: Python Crash Course: A Hands-On, Project-Based Introduction to Programming By Eric Matthes