"""This is a generic class to represent a car."""


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. (constructor)"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = dummy"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(dummy"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """
    Generic class for a Battery
    A simple attempt to model a battery for an electric car.
    The class creation could have been done in a different file as well!
    The abstraction of your code that will tell how to group things in the same file/package/etc
    """

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes.(constructor)
        Every child object from this class will initialize a battery
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(dummy"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(dummy"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """
    A type of car - Electric - which is extending our generic class Car up in this program
    Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.

        Notice we are not implementing any method from our parent class (Car)
        All methods in our parent class can be accessed through this child class
        """
        super().__init__(make, model, year)
        self.battery = Battery()
