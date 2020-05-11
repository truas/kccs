
class MyClassConstructor:
    '''
    Every time we crate an object from our Class, we want it to have two attributes
    at the time of its creation real and imaginary

    In case no value is provided initialize them with default ones
    '''
    def __init__(self, real=1.0, imaginary=-1.0):
        self.real = real
        self.imag = imaginary

    '''
        Can we create another constructor? to initialize our objects differently?
        Well, in Python this is not straight forward. We only use one constructor 
        This constructor should deal with all cases.
        Uncomment the block below and see what happens.
    '''
    # def __init__(self, real=1):
    #     self.real = real


if __name__ == "__main__":
    '''
    We don't need  to separate classes and the "main" program
    but this is highly recommended. That way we have a more organized code
    '''
    # Make an instance object!
    const_obj = MyClassConstructor(42.0, -42.0)  # try to pass an int to see what the IDE will say
                                                 # as python does not check for types it will warn you
                                                 # but your code will run. The same if you change the
                                                 # value type up there in the class defintion
    print(const_obj.real, const_obj.imag)
