"""
This is a simple example of a decorator in Python.
A decorator is a function that takes another function as an argument
and extends or modifies its behavior without explicitly changing its code.
In this example, the `decorator_function` wraps the `ordinary_function`,
adding additional behavior before calling the original function.
"""


def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()

    return wrapper_function


@decorator_function
def ordinary_function():
    print("I am an ordinary function.")


ordinary_function()
