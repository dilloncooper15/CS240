# Dillon J. Cooper
# CS 240 lab 07

# Exercise 1: In Chapter 14, complete exercise 5, parts a, b, c, and d in your
# text.


# Exercise 2: Add __str__, __repr__, __eq__, for both classes you implemented
# in exercise 5.

import math


class Point:
    def __init__(self, x, y):
        """(Point, int, int) -> NoneType
        Establishes a point located at (x, y).

        >>> first_point = Point(5, 10)
        >>> first_point.x
        5
        >>> first_point.y
        10
        """

        self.x = x
        self.y = y

    def __str__(self):
        """(Point) -> str

        Returns the string of the contents of Point.

        >>> str(Point(5, 10))
        '(5, 10)'
        """
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        """(Point) -> str

        Returns the string of the input needed to generate
        the Point obj.

        >>> repr(Point(5, 10))
        'Point(5, 10)'
        """
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, obj):
        """(Point, Point) -> bool

        Compares two points and decides if they are equivalent to eachother.
        If they are, returns True. If they are not equivalent, then it will
        return False.

        >>> Point(5, 10) == Point(5, 10)
        True
        >>> Point(5, 10) == Point(10, 5)
        False
        >>> Point(5, 10) == Point(10, 5)
        False
        >>> Point(1, 2) == Point(9, 8)
        False
        >>> Point(1, 2) == Point(1, 3)
        False
        >>> Point(1, 2) == Point(0, 2)
        False
        """
        # if self.x == obj.x and self.y == obj.y:
        #     return True
        # else:
        #     return False
        return (self.x, self.y) == (obj.x, obj.y)


class LineSegment:
    def __init__(self, first_point, second_point):
        """(LineSegment, Point, Point) -> NoneType
        Connects two points, first_point and second_point, together.

        >>> first_point = Point(1, 3)
        >>> second_point = Point(3, 2)
        >>> seg = LineSegment(first_point, second_point)
        >>> seg.initial == first_point
        True
        >>> seg.final == second_point
        True
        """

        self.initial = first_point
        self.final = second_point

    def __str__(self):
        """(LineSegment) -> str

        Returns a string containing the length and slope of two points.

        >>> a = LineSegment(Point(16, 1), Point(1, 16))
        >>> str(a)
        'Length: 21.21\\nSlope: -1.00'
        """
        return 'Length: {:0.2f}\nSlope: {:0.2f}'.format(
            self.length(), self.slope())

    def __repr__(self):
        """(LineSegment) -> str

        Returns a string that is required to generate the LineSegment.

        >>> repr(LineSegment(Point(16, 1), Point(1, 16)))
        'LineSegment(Point(16, 1), Point(1, 16))'
        """
        return 'LineSegment({}, {})'.format(
            repr(self.initial), repr(self.final))

    def __eq__(self, obj):
        """(LineSegment, LineSegment) -> bool

        Compares two LineSegments and decides if they are equivalent to
        eachother. If they are, returns True. If they are not equivalent,
        then it will return False.

        >>> LineSegment(Point(16, 1), Point(1, 16)) == LineSegment(Point(16, 1), Point(1, 16))
        True
        >>> LineSegment(Point(5, 10), Point(5, 10)) == LineSegment(Point(11, 12), Point(2, 4))
        False
        >>> LineSegment(Point(16, 1), Point(1, 16)) == LineSegment(Point(16, 1), Point(1, 15))
        False
        >>> LineSegment(Point(16, 1), Point(1, 16)) == LineSegment(Point(16, 1), Point(0, 16))
        False
        """
        if (self.initial, self.final) == (obj.initial, obj.final):
            return True
        else:
            return False

    def slope(self):
        """(LineSegment) -> float
        Returns the slope of the line between two segments.

        >>> a = LineSegment(Point(16, 1), Point(1, 16))
        >>> a.slope()
        -1.0
        """

        return (self.final.y - self.initial.y) / (
            self.final.x - self.initial.x)

    def length(self):
        """(LineSegment) -> float

        >>> segment = LineSegment(Point(2, 5), Point(4, 7))
        >>> segment.length()
        2.8284271247461903
        """
        return math.sqrt((self.final.y - self.initial.y) ** 2 + (
            self.final.x - self.initial.x) ** 2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
