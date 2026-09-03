"""
sample implementation of generators in python
Code below shows three ways to use generators in python.
The first way is to use the yield statement in a function,
the second way is to use the next() function to get the next value from the generator object,
and the third way is to use a for loop to iterate over the generator object.
"""


def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


# when we call the function numbers()
# it will return a generator object
x = numbers()
print(x)  # <generator object numbers at 0x1045df280>

print("--------------------------------")

# in this case, the call to the function numbers() will return a generator object f
# and we can use the next() function to get the next value from the generator object
y = numbers()
print(next(y))
# likewise we can call the next() function multiple times to get the next value from the generator object
print(next(y))
print(next(y))
print(next(y))
print(next(y))
# this will raise a StopIteration exception because
# there are no more values to yield from the generator object
# print(next(y))

print("--------------------------------")

# but when we use a for loop to iterate over the generator object,
# it will automatically handle the StopIteration exception and stop the
# iteration when there are no more values to yield
for i in numbers():
    print(i)
