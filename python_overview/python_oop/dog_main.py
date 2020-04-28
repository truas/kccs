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

from python_oop.dog_generic import DogBad
from python_oop.dog_generic import DogGood

if __name__ == "__main__":
    print('===Tricks for Bad Dogs===')
    # Let us create two dogs
    bad_dog_a = DogBad('Fido')
    bad_dog_b = DogBad('Buddy')

    # Teach them tricks! Different ones of course!
    bad_dog_a.teach_trick('roll over')
    bad_dog_b.teach_trick('come here')

    # Let us check wha they have learned
    print('Tricks {0}: {1}'.format(bad_dog_a.name, bad_dog_a.dog_tricks))
    print('Tricks {0}: {1}'.format(bad_dog_b.name, bad_dog_b.dog_tricks))
    '''
    Wait a second... we just taught Fido and Buddy different tricks!
    Yes, indeed we did, but take a look un which list we are appending the tricks
    That's right, the list is not exclusive for Fido or Buddy, instead
        it is a list present in the class DogBad itselsef.
    Therefore, all instances of that class will share this common attribute.
    Is there are way to fix this? Can we 'construct' a list of tricks in way
        they do not interfere with each other? Take a look on DogGood (dog_generic) to see the solution.
    '''
    print('===Tricks for Good Dogs===')
    # Let us create two dogs
    good_dog_a = DogGood('Farah')
    good_dog_b = DogGood('Shelly')

    # Teach them tricks! Different ones of course!
    good_dog_a.teach_trick('roll over')
    good_dog_b.teach_trick('come here')

    # Let us check wha they have learned
    print('Tricks {0}: {1}'.format(good_dog_a.name, good_dog_a.dog_tricks))
    print('Tricks {0}: {1}'.format(good_dog_b.name, good_dog_b.dog_tricks))
    '''
    Look in the constructor of DogGood, for each object we create a new list of tricks
        as a result, each trick added to each object instance (each dog) will have their
        separate control.
    '''