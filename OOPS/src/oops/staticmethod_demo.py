"""
Static method demo
-------------------
A static method is a method that belongs to a class rather than an
instance of the class. It does not require access to the instance (self) or class (cls)
variables. Static methods are defined using the @staticmethod decorator.
"""


class TemperatureConverter:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        """Convert Celsius to Fahrenheit."""
        # see how we can call the static method from an instance method
        # and it prefixed with the class name
        return TemperatureConverter.celsius_to_fahrenheit(self.celsius)

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9 / 5) + 32

    @staticmethod
    def is_freezing(celsius: float) -> bool:
        """Check if the temperature is at or below freezing point."""
        return celsius <= 0


# called directly from the class without creating an instance
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(25)
print(f"25°C is equal to {fahrenheit}°F")
is_freezing = TemperatureConverter.is_freezing(-5)
print(f"Is -5°C at or below the freezing point? {is_freezing}")
