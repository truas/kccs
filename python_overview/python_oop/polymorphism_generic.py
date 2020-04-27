'''
Even though our classes have the same signature/name for the methods, they are implementing them
accordingly to their specific behavior
Take a look how they change from class to class
Plymorphism with classes is allowed
'''

class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):  # generic flight
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):  # sparrow flight
        print("Sparrows can fly.")

class ostrich(Bird):
    def flight(self):  # ostrich flight - no flight here :)
        print("Ostriches cannot fly.")
