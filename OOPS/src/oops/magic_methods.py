"""
Magic methods in Python whcih are also known as dunder methods (double underscore methods) are special methods that allow you to define the behavior of your objects for built-in operations. These methods have names that start and end with double underscores,
such as __init__, __str__, __add__, etc.
"""


class Father:
    def __init__(self):
        self.father_name = input("Enter father name: ")
        self._bank_balance = input("Enter bank balance: ")
        self.__phone_model = input("Enter phone model: ")

    def __str__(self):
        return f"Father's name: {self.father_name}, Bank balance: {self._bank_balance}, Phone model: {self.__phone_model}"


obj1 = Father()
obj2 = Father()
# the same method __str__ is called when we print the object,
# so we can see the output of the object in a human-readable format.
print(obj1)
print(obj2)
