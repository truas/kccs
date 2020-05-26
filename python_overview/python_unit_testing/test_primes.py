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

from python_unit_testing.primes import Prime
#from python_unit_testing.primes import print_next_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`. @thanks to Jeff Knupp"""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        punit = Prime()
        self.assertTrue(punit.is_prime(5))

    def test_is_four_non_prime(self):
        """Is four correctly determined not to be prime?"""
        punit = Prime()
        self.assertFalse(punit.is_prime(4), msg='Four is not prime!')

    def test_next_prime(self):
        """What is the next prime"""
        punit = Prime()
        self.assertEqual(punit.print_next_prime(4), 5, msg="the next prime after 4 is 5")
        # create more test cases for this function as we did for the primes

    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        punit = Prime()
        self.assertFalse(punit.is_prime(0))

    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        punit = Prime()
        for index in range(-1, -10, -1):
            self.assertFalse(punit.is_prime(index), msg='{} should not be determined to be prime'.format(index))

if __name__ == '__main__':
    unittest.main()

#Reference for the code: https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/