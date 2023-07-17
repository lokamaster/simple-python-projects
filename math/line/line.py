from typing import Self


class Point:
    
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __abs__(self) -> float:
        return (self.x**2 + self.y**2)**0.5

    def __add__(self, other: Self) -> Self:
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return type(self)(self.x - other.x, self.y - other.y)

    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    @staticmethod
    def _generate_line(m: float, b: float) -> str:
        """Generate line y = mx + b."""
        operator = "+" if b >= 0 else "-"
        return f'y = {m:g}x {operator} {abs(b):g}'

    def line(self, other: Self) -> str:
        """Calculate the line y = mx + b from two points.

        From the two points (x1, y2) and (x2, y2) m can be calculated as
            m = (y2 - y1) / (x2 - x1).
        Substituting x and y for either of the pairs and m with the
        calculation above, b can be calculated as
            y = mx + b
         => b = y1 - m*x1

         If x2 = x1, the two points lie on the same vertical line hence
         the line spans all the points on the form (-b/m, y) for all y,
         which means that x is just a constant.
        """
        # GUard if self and other are the same point.
        if self == other:
            return "Two points are the same, no line can be calculated."

        # Calculate m.
        delta_x = self.x - other.x
        delta_y = self.y - other.y
        if delta_x:
            m = delta_y / delta_x
        else:
            return f'x = {self.x:g}'

        # Calculate b.
        b = self.y - m*self.x
        
        # Return line
        return self._generate_line(m, b)


    def line_from_slope(self, m: float) -> str:
        """Calculate the line y = mx + b from self and a given slope.

        With the slope m and a sample point (self) given, b can be
        calculated as
            y = mx + b
         => b = y - mx
        Where y, m and x are all given.
        """
        b = self.y - m*self.x
        return self._generate_line(m, b)

