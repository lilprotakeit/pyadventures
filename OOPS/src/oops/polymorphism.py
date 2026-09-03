"""
simple illustration of polymorphism in python
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    """Represents a dog, inheriting from Animal."""

    def make_sound(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    """Represents a cat, inheriting from Animal."""

    def make_sound(self):
        return f"{self.name} says Meow!"


# Creating instances of different classes
dog = Dog("Buddy")  # Creating an instance of Dog with the name "Buddy"
cat = Cat("Whiskers")  # Creating an instance of Cat with the name "Whiskers"

# Calling the same method on different objects
print(
    dog.make_sound()
)  # Calling the make_sound method on the dog instance, which will output "Buddy says Woof!"
print(
    cat.make_sound()
)  # Calling the make_sound method on the cat instance, which will output "Whiskers says Meow!"
