import random

from itertools import combinations
from math import sqrt
from functools import lru_cache

QUADRANT_ONE = 1
QUADRANT_TWO = 2
QUADRANT_THREE = 3
QUADRANT_FOUR = 4


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return "<{}, {}>".format(self.x, self.y)


@lru_cache()
def find_orthogonal_vector(v1, v2):
    """
    Finds a vector with origin (0,0) that is orthogonal to a line segment
    beginning at v1 and ending at v2
    """
    try:
        slope = (v1.y - v2.y) / (v1.x - v2.x)
    except ZeroDivisionError:
        slope = 0

    offset = v1.y - slope * v1.x

    if slope == 0:
        if v1.x - v2.x == 0:
            x = v1.x
            y = 0
        else:
            x = 0
            y = offset
    else:
        ortho_line = (1.0 / slope) * -1.0
        x = offset / (ortho_line + (slope * -1))
        y = x * ortho_line

    return Vector(x, y)


def quadrant(v):
    """
    Returns the quadrant a point lies in
    """
    if v.y > v.x and v.y < v.x * -1:
        return QUADRANT_ONE
    elif v.y < v.x and v.y < v.x * -1:
        return QUADRANT_TWO
    elif v.y < v.x and v.y > v.x * -1:
        return QUADRANT_THREE
    elif v.y > v.x and v.y > v.x * -1:
        return QUADRANT_FOUR


def quad_distinct(v1, v2):
    """
    :returns False if the two points lie in the same quadrant True otherwise
    """
    return quadrant(v1) != quadrant(v2)


def enclosing_triangles(*args):
    count = 0

    # Loop through all possible triangles
    for triangle in combinations(args, 3):
        valid = True
        # Loop through all line segments of a triangle
        for line in combinations(triangle, 2):

            v1, v2 = line

            # If two points lie in the same quadrant then triangle is invalid
            if not quad_distinct(v1, v2):
                valid = False
                break
            # Find an orthogonal vector from the origin to the line segment
            o = find_orthogonal_vector(v1, v2)

            # If that vector has length less than one then triangle is invalid
            if o.length() < 1.0:
                valid = False
                break
        if valid:
            count += 1
    return count


if __name__ == "__main__":
    random.seed(12345)
    points = [Vector(3, -1), Vector(1, 3), Vector(-1, -1), Vector(-5, -2)]

    print(enclosing_triangles(*points))
