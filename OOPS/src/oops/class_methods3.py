"""
Sample program to show the use of class methods in Python.
-----------------------------------------------------------
This is yet another example of class methods in Python.
Class methods are methods that are bound to the class and not the instance of the class.
"""


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, user_string):
        name, age = user_string.split("-")
        return cls(name, int(age))


user = User.from_string("John-25")
print(f"Name: {user.name}, Age: {user.age}")
