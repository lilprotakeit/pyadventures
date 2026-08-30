"""
sample code to illustrate the use of args and kwargs in python
"""


def add(n1, n2, n3, *args, **kwargs):
    print(f"{n1=}")
    print(f"{n2=}")
    print(f"{n3=}")
    print(f"{args=}")
    print(f"{kwargs=}")


# add(1, 2, 3)
add(1, 2, 3, 4, 5, 6)
