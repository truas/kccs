from abc import ABC, abstractmethod #yes this is the name of the actual abstract class
'''
From the documentation:
"This module provides the infrastructure for defining abstract base classes (ABCs) in Python"
'''
class AbstractBaseAnimal(ABC):
    '''
    Here we have two methods that need to be implemented by any class that extends AbstractBaseAnimal
    '''

    @abstractmethod
    def feed(self, other_food=None):
        print("All animals have to feed!")

    @abstractmethod
    def sleep(self, state=1):
        if state == 1:
            print("This animal needs to sleep")
        else:
            print("This animal does not need to sleep")

    # no abstract, we can implement if we want, but it is not required
    def exist(self):
        print("I am alive!")


class Dolphins(AbstractBaseAnimal):
    '''
    All the abstract methods need to be implemented otherwise we cannot  instantiate any object
    from this class
    '''
    def __init__(self, food="Fish"):
        self.food_type = food

    '''
    Note that the abstract functions need to be implemented, even if with 'pass' (try that)
    We don't need to follow the same signature of the function but it has to be implemented
    Notice we do not implement the method 'exist()'. Why ? Try to spot the difference between
        this exist() and the other methods. That's right, exist() is not an abstract method,
        thus we do not need to implement in our class.   
    '''

    # this is an abstract method from our base class
    def feed(self, alternative=None):
        print("I like to eat ", self.food_type)
        print("I can also eat other things, such as ", alternative)

    # this is an abstract method from our base class
    def sleep(self, state=-1):
        if state == 1:
            print("This animal needs to sleep.")
        elif state == 0:
            print("This animal does not need to sleep.")
        elif state == -1:
            print("This animal only sleeps with half of the brain.")