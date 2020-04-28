import unittest #we have to import this package to handle our tests
import os
import sys
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

from python_unit_testing.survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)


    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()


# Reference code: Python Crash Course: A Hands-On, Project-Based Introduction to Programming By Eric Matthes