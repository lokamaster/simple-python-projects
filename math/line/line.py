from typing import Self


class Point:
    """Representation of a point in 2d space.

    Attributes:
        x : float,
        y : float
            The x and y coordinate of the point.
    """
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


class LineSegment:

    def __init__(self, a: Point, b: Point) -> None:
        self.a = a
        self.b = b


class Line:

    def __init__(self, slope: float, intercept: float) -> None:
        self.slope = slope
        self.intercept = intercept

    def __repr__(self) -> str:
        return f'Line({self.slope}, {self.intercept})'

    def __str__(self) -> str:
        """Generate line y = mx + b."""
        operator = "+" if self.intercept >= 0 else "-"
        return f'y = {self.slope:g}x {operator} {abs(self.intercept):g}'

    @classmethod
    def from_points(cls, point1: Point, point2: Point) -> Self:
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

        Raises:
            ValueError
                If point1 == point2 or point1.x == point2.x, i.e. the two
                points are the same or they share x-coordinate.
        """
        # Guard if points are the same, or x is the same.
        if point1 == point2:
            raise ValueError(
                "The two points are the same, no line can be calculated."
            )
        elif point1.x == point2.x:
            raise ValueError(
                f'x = {point1.x}. No intercept or slope can be calculated.'
            )

        # Calculate m.
        delta_x = point1.x - point2.x
        delta_y = point1.y - point2.y
        m = delta_y / delta_x

        # Calculate b.
        b = point1.y - m*point1.x
        
        # Return line
        return cls(m, b)

    @classmethod
    def from_point_slope(cls, point: Point, slope: float) -> Self:
        """Calculate the line y = mx + b from self and a given slope.

        With the slope m and a sample point (self) given, b can be
        calculated as
            y = mx + b
         => b = y - mx
        Where y, m and x are all given.
        """
        b = point.y - slope*point.x
        return cls(slope, b)

