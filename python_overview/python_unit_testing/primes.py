
class Prime:

    def is_prime(self,number):
        """Return True if *number* is prime."""
        if number in (0, 1):
            return False

        if number < 0:
            return False  # can we combine these last two ?

        for element in range(2, number):
            if number % element == 0:
                return False

        return True

    def print_next_prime(self, number):
        """Print the closest prime number larger than *number*."""
        index = number
        while True:
            index += 1
            if self.is_prime(index):
                print('The next prime after {0} is {1}'.format(number, index))
                return index

# Reference for the code: https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/