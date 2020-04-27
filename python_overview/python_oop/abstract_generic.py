from abc import ABC, abstractmethod #yes this is the name of the actual abstract class
'''
From the documentation:
"This module provides the infrastructure for defining abstract base classes (ABCs) in Python"
'''
class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        print("Some implementation!")

    # @abstractmethod
    # def do_something2(self):
    #     print("Another implementation!")


class AnotherSubclass(AbstractClassExample):
    '''
    All the abstract methods need to be implemented otherwise we cannot  instantiate any object
    from this class
    '''

    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubclass")

    '''
    uncomment do_something2 in the abstract class and do not implement it here to see the result
    in the abstract_main program
    '''
    # def do_something2(self):
    #     print("The enrichment from AnotherSubclass - Double Tap")


# base reference for the example : https://www.python-course.eu/python3_abstract_classes.php