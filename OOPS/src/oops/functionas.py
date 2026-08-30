"""
Functions playground: Toy code to illustrate the use of functions in Python.
"""


def add(*args):
    print("Sum of numbers is:", sum(args))
    print("Number of arguments passed:", len(args))
    print("Second argument:", args[1])


add(1, 2, 3)
add(4, 5, 6, 6, 7, 8)
add(1, 2)

# add a horizontal line to separate the output of the two functions
print("-" * 40)


def add_more(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
    for k, v in kwargs.items():
        print(f"{k}: {v}")


add_more(name="John", age=30, city="New York")
