class Robot(object):
    def __init__(self):
        self.__version = 42
        self.__name = 'Cranky'
        self._weak_name = 'Howdy'

    def getVersion(self):
        return(self.__version)

    def setVersion(self, version):
        self.__version = version

    def __secret__(self):
        print("Shhh I am private")

    def _makeNoise(self):
        print("Brr...Brr...BEEP!")

    def __turnOFF(self):
        print('Turining OFF...bye')