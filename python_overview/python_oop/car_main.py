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

from python_oop.car_generic import Car  # we are importing just the class Car (we have other classes there)
from python_oop.car_generic import ElectricCar as eCar  # this will allow us to create a specific electric car
from python_oop.car_generic import ElectricCar  # we can use the same layout as before for Car

if __name__ == "__main__":

    print('===Car Dealer===\n')

    print('Generic Car 01:')
    car_obj_01 = Car('audi', 'a4', 2019)  # we create a new object from the class Car
    print(car_obj_01.get_descriptive_name())  # print out its details
    car_obj_01.odometer_reading = 23  # set a new reading on odometer (attribute set as 0 in constructor)
    car_obj_01.read_odometer()  # read new value under odometer

    print('\nGeneric Car 02:')
    car_obj_02 = Car('volkswagen', 'beetle', 2019)  # we create a new object from the same class car
    print(car_obj_02.get_descriptive_name())

    print('\nSpecific Eletric Car 01:')
    my_tesla = eCar('tesla', 'model s', 2020)  # notice we used a different class to instantiate our object
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()

    print('\nSpecific Eletric Car 02:')
    my_tesla = ElectricCar('tesla', 'roadster', 2019)  # here we are not using the alias we used in the previous car
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
