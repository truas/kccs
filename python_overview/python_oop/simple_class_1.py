class MyClass:
    """A simple example class."""
    num = 12345  # generic attribute for our class

    def greet(self):    # M1 (mark 1)
        return "Hello world!"



if __name__ == "__main__":
    '''
    We don't need  to separate classes and the "main" program
    but this is highly recommended. That way we have a more organized code
    '''
    tiny_obj = MyClass()  # creating a object from our MyClass class
    tiny_obj.greet()  # 'Hello world!'
    '''
    M1 : What is this 'self' as argument in our function? why we called, did not pass anything
         And it worked?
    self is an object reference to the object itself, so basically is the reference
    for the object calling the function (which is also an object - everything is in Python)
    '''

    print(type(tiny_obj.greet))  # method <bound method MyClass.greet of ...>
    print(type(MyClass.greet))  # function <function MyClass.greet(self)>
    print(tiny_obj.num is MyClass.num)  # True since there is only one attribute in the class/object
    print(tiny_obj.greet is MyClass.greet)  # False

    '''
    A method is like a function attached to an object
        method is approx. a pair of (object, function)

    Methods calls invoke special semantics
        object.method(arguments) = function(object, arguments)

    '''
