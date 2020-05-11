class Being(object):
    def beingAlive(self):
        print("I am alive!")


class Mammal:
    def drinkMilk(self):
        print("Glub, glub, glub.")


class Carnivore(Being, Mammal): # we can have multiple classes
    def eatMeat(self):
        print("Chomp, chomp, chomp.")


class Hunter:
    def run(self):
        print("VOOSH")


class AquaHunter(Hunter):
    def run(self):  # we are implementing the run method accordingly to the aqua hunter class
        print("PLOOSH!")


class Killer:
    def killPrey(self):
        print("Game over...")


class KillerWhale(Carnivore, AquaHunter, Killer):  # we can extend our class from multiple sources
    def __init__(self):
        self.beingAlive()
        self.eatMeat()
        self.run()
        self.killPrey()
