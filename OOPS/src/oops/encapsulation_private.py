"""
Implementation of private access modifier in python using encapsulation.
In python, we can make a variable private by adding __ before the variable name.
Private variables cannot be accessed outside the class.
We can access private variables using getter and setter methods.
"""

from random import randint


class Bank:
    def __init__(self):
        self.name = input("Enter your name: ")
        # __ represents private variable, it cannot be accessed outside the class
        self.__account_number = randint(100000, 999999)
        self.__balance = 25

    def display(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")


obj = Bank()
obj.display()
obj.__account_number = 1  # will create a new variable __account_number in the object, it will not change the private variable __account_number of the class
obj.display()
print(vars(obj))
# {'name': 'praveen', '_Bank__account_number': 126528, '_Bank__balance': 0, '__account_number': 1}
print(
    obj._Bank__account_number
)  # will print the private variable __account_number of the class
