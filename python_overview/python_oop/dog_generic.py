class DogBad:
    """A simple attempt to model a dog."""
    dog_tricks = []  # all dogs will have tricks (this might be problematic)

    def __init__(self, name):
        """Initialize name and age attributes."""
        self.name = name

    def teach_trick(self,trick):
        self.dog_tricks.append(trick)  # add new trick to a dog


class DogGood:
    """A simple attempt to model a dog."""

    def __init__(self, name):
        """Initialize name and age attributes."""
        self.name = name
        self.dog_tricks = []  # each dog should lear their own tricks! that makes more sense.

    def teach_trick(self,trick):
        self.dog_tricks.append(trick)