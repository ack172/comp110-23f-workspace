"""Challenge Question 07- Mutation of Functions."""

from __future__ import annotations
__author__ = "730385079"


class Point: 
    """This is my class to represent a point on an (x,y) coordinate graph."""
    x: float
    y: float

    def __init__(self, x_init=0.0, y_init=0.0):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        """Updates the x and y attributes so that x = x * factor and y = y * factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Returns a new point with x and y attributes equal to self.x * factor and self.y * factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self):
        """Returns the function back to itself."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: int | float) -> Point:
        """Returns a new point with the x and y attributes equal to self.x * factor and self.y * factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point

    def __add__(self, factor: int | float) -> Point:
        """Returns a new point with the x and y attributes equal to self.x * factor and self.y * factor."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point
