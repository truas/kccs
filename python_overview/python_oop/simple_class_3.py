class MyOtherClass:
    num = 12345  # we have the same attribute in our class definition
    dum = 300  # shared attribute

    def __init__(self, num=42):
        self.num = num  # and we create the same one inside the constructor


if __name__ == "__main__":
    '''
    We don't need  to separate classes and the "main" program
    but this is highly recommended. That way we have a more organized code
    '''
    # Make an instance object!
    x = MyOtherClass()  # when the object is created the attribute value is the one in the constructor

    # Before we start, is x.num the same as MyOtherClass.num?
    print('Object and Class attribute: ', x.num is MyOtherClass.num)  # False - that give us a hint that these attribute-objects have different references
    print('Object 1 attribute value: ', x.num)
    print('Class attribute value: ', MyOtherClass.num)

    # If we create a second object from the same class and pass a different value
    y = MyOtherClass(-42)
    print('\nObject and Class attribute: ', y.num is MyOtherClass.num)  # False - that give us a hint that these attribute-objects have different references
    print('Object 2 attribute value: ', y.num)
    print('Class attribute value: ', MyOtherClass.num)
    '''
    See how each object instance has its own "num" value, either initialized or not
    However, this class attribute, is common to both of them and unaltered 
    '''
    print('\nPython attributes')
    print('Common attribute verification (dum): ', x.dum is y.dum)
    print('Common attribute verification (num): ', x.num is y.num)

    print('\n=========Scope Search==============')
    print('First attribute search from object 1: ', x.num)  # 42 or 12345?
    print('Deleting attribute from object 1...')
    del x.num  # deleting this attribute from the object instance, does not remove the class one, yet
    print('Second attribute search: ', x.num)  # 42 or 12345?

    '''
    Let's delete it one more time
    Now there will be no place to find the attribute "num" 
    uncomment and see what happens
    '''
    # del x.num  # in the third time, the only attribute of this object is the class itself.
    # print('Third attribute search: ', x.num)  # 42 or 12345? or something else?

