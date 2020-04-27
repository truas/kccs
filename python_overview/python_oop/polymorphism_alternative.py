
class BadCake:
    def makeCake(self,):
        print("Making a simple cake")

    def makeCake(self, stuff):
        print("Making a simple cake, with " + stuff + " inside")


class GoodCake:
    def makeCake(self,stuff=None):
        if not stuff:
            print("Making a simple cake")
        else:
            print("Making a simple cake, with " + stuff + " inside")


if __name__ == "__main__":
    '''
    when we run this the last function definition will be considered for badCake, 
        so it will be expecting an argument Uncomment line 27 to see the problem
    Polymorphism is not allowed in python in this way. Use keyword/optional parameters instead
    '''
    badcake = BadCake()
    goodcake = GoodCake()

    # badcake.makeCake()

    '''
    Now for our good cake, there is only one function makeCake, 
    and we control the optional parameters there
    '''
    ingredient = input("Provide a special ingredient please: ")
    goodcake.makeCake(ingredient)
