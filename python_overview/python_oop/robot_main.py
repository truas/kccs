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

from python_oop.robot_encapsulation import Robot

if __name__ == "__main__":
    '''
    Encapsulation is all about hiding information that does not need to be public (restricting access)
    Python does not enforce this, as in other languages with public, protected, and private
    However there are ways to indicate!
    (keep in mind this will not prevent from accessing, just a strong recommendation)
    Single underscore -> Private
    Double underscore -> Private - harder
    '''
    obj = Robot()
    print('Before: ', obj.getVersion())  # using a getter we can get our version value

    # Notice we cannot access the attributes with double underscore directly
    # Try to run the following lines
    # print(obj.__version)
    # print(obj.__name)

    # Now let's try to access a weak binded attribute
    print('Robot weak name: ', obj._weak_name)  # See that the IDE does not list this directly by default

    '''
    The same thing happen with the methods, uncomment one line at a time and see the result
    You will be able to call _functions (the IDE will highlight this is "protected")
    For __functions this will probably not work
    '''
    #obj._makeNoise()
    #obj.__turnOFF()


