"""
Inheritance in Python
"""


class Car:
    def __init__(self, color, type, mileage, seat_capacity):
        self.color = color
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity

    def base_info(self):
        print(f"Color: {self.color}")
        print(f"Type: {self.type}")
        print(f"Mileage: {self.mileage}")
        print(f"Seat Capacity: {self.seat_capacity}")


class Audi(Car):
    def __init__(self):
        print("Audi INIT")


c1 = Audi()
c1.color = "Red"
c1.type = "Sedan"
c1.mileage = 15
c1.seat_capacity = 5
c1.base_info()
