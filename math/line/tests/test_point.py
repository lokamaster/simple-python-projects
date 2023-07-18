import unittest

from line import Point


RANGE = 100


class TestPointArithmetic(unittest.TestCase):

    def test_addition(self):
        for i in range(-RANGE, RANGE+1):
            for j in range(-RANGE, RANGE+1):
                # Create points:
                a = Point(i, j)
                b = Point(j, i)
                
                # Do addition.
                c = a+b
                
                # Assert x and y coordinates are correct.
                self.assertEqual(c.x, i+j)
                self.assertEqual(c.y, j+i)
                
    def test_subtraction(self):
        for i in range(-RANGE, RANGE+1):
            for j in range(-RANGE, RANGE+1):
                # Create points:
                a = Point(i, j)
                b = Point(j, i)
                
                # Do subtraction.
                c = a-b
                
                # Assert x and y coordinates are correct.
                self.assertEqual(c.x, i-j)
                self.assertEqual(c.y, j-i)

    def test_length(self):
        for i in range(-RANGE, RANGE+1):
            for j in range(-RANGE, RANGE+1):
                a = Point(i, j)
                self.assertEqual(abs(a), (i**2 + j**2)**0.5)


class TestPointRepresentation(unittest.TestCase):

    def test_repr(self):
        for i in range(-RANGE, RANGE+1):
            for j in range(-RANGE, RANGE+1):
                a = Point(i, j)
                self.assertEqual(repr(a), f'Point({a.x}, {a.y})')

    def test_str(self):
        for i in range(-RANGE, RANGE+1):
            for j in range(-RANGE, RANGE+1):
                a = Point(i, j)
                self.assertEqual(str(a), f'({a.x}, {a.y})')
