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

from python_unit_testing.survey import AnonymousSurvey


# Main block
if __name__ == "__main__":
    # Define a question, and make a survey.
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)

    # Show the question, and store responses to the question.
    my_survey.show_question()
    print("Enter 'q' at any time to quit.\n")

    while True:
        response = input("Language: ")
        if response == 'q':
            break
        my_survey.store_response(response)

    # Show the survey results.
    print("\nThank you to everyone who participated in the survey!")
    my_survey.show_results()
