"""
Implementation of encapsulation using protected access modifier in Python.
In python, we can make a variable protected by adding _ before the variable name.
Protected variables can be accessed within the class and its subclasses.
"""


class Father:
    def __init__(self) -> None:
        self.father_name = input("Enter father's name: ")
        self._bank_balance = input(
            "Enter father's bank balance: "
        )  # protected variable, accessible in child class
        self.__phone_model = input("Enter father's phone model: ")

    def displayFather(self):
        print(f"Father's Name: {self.father_name}")
        print(
            f"Father's Bank Balance: {self._bank_balance}"
        )  # accessing protected variable
        print(
            f"Father's Phone Model: {self.__phone_model}"
        )  # accessing private variable


class Child(Father):
    def __init__(self) -> None:
        super().__init__()
        self.child_name = input("Enter child's name: ")

    def displayChild(self):
        print(f"Child's Name: {self.child_name}")
        print(
            f"Father's Bank Balance (accessed from child class): {self._bank_balance}"
        )  # accessing protected variable


child = Child()
# Displaying the details of father and child
child.displayChild()
