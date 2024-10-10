from abc import ABC, abstractmethod
import math

# Abstract class Figure
class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

# The Rectangle class inherits from Shape
class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2 * (self.__length + self.__width)

# The Rhombus class inherits from Figure
class Rhombus(Figure):
    def __init__(self, side, angle):
        self.__side = side
        self.__angle = math.radians(angle)  # An angle in degrees is converted to radians

    def get_area(self):
        # The formula for the area of a rhombus: a^2 * sin(angle)
        return self.__side ** 2 * math.sin(self.__angle)

    def get_perimeter(self):
        # Perimeter of a rhombus: 4 * a
        return 4 * self.__side


figures = [
    Rectangle(4, 6),
    Rhombus(5, 60),
    Rectangle(10, 20),
    Rhombus(8, 45)
]

# A loop to calculate the area and perimeter of each figure
for figure in figures:
    print(f"Area: {figure.get_area():.2f}, Perimeter: {figure.get_perimeter():.2f}")
