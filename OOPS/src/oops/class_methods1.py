"""
sample code to illustrate class methods in python

"""

from pathlib import Path


class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}, \nAge: {self.age}, \nGender: {self.gender}")

    @classmethod
    def create_student_using_params(cls, name, age, gender):
        return cls(name, age, gender)

    @classmethod
    def create_student_using_file(cls, filename):
        # get the directory of the current file(class_methods.py)
        base_dir = Path(__file__).resolve().parent
        # create the full path to the file (student.txt)
        file_path = (
            base_dir / filename
        )  # read the overloaded "/" property of Path object
        with open(file_path, "r") as f:
            name, age, gender = f.read().strip().split(" ")
        return cls(name, int(age), gender)


s1 = Student.create_student_using_params("Alice", 20, "Female")
s1.display()
print("----------")
s2 = Student.create_student_using_file("student.txt")
s2.display()
