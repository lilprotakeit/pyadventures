"""
Sample implementation of class methods in python
----------------------------------------------------
@classmethod is used to create a method that works with the class instead of an object instance.
IMP: |--- A CLASS METHOD RECEIVES THE CLASS ITSELF AS THE FIRST ARGUMENT USING CLS ---|
It is commonly used to access class variables, create factory methods and perform operations related to the class.

In the program below, we have a class Student with a class variable school_name and
two class methods get_school_name() and create_student().
"""


class Student:
    school_name = "ABC School"  # class variable

    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age  # instance variable

    @classmethod
    def get_school_name(cls):
        """In the get_school_name() method, we access the class variable school_name using cls."""
        # accessing class variable using cls
        return cls.school_name

    @classmethod
    def create_student(cls, name, age):
        """In the create_student() method, we create an instance of the class using cls and return it."""
        return cls(name, age)  # creating an instance of the class using cls


# creating an instance of Student using class method
Student1 = Student.create_student("Alice", 20)
# accessing class variable using class method
print(f"Student Name: {Student1.name}, Age: {Student1.age}")
# accessing class variable using class method
print(f"School Name: {Student.get_school_name()}")
