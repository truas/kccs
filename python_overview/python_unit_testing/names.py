class Names:

    def get_formatted_name(self, first, last, middle=''):
        """Generate a neatly formatted full name."""
        if middle:
            full_name = f"{first} {middle} {last}"
        else:
            full_name = f"{first} {last}"
        return full_name.title()


# Reference code: Python Crash Course: A Hands-On, Project-Based Introduction to Programming By Eric Matthes