import sys
from math import sin, cos, radians

import pygame
from vectors import Vector, Point


class PygameVector:
    basis = None

    def __init__(self, v, basis):
        self.v = v
        self.basis = basis

        self.absolute_x = self.basis.x + self.v.x
        self.absolute_y = self.basis.y + self.v.y

    def draw(self, color):
        vec_from_basis = (self.absolute_x,
                          self.absolute_y)
        pygame.draw.line(screen,
                         color,
                         (self.basis.x, self.basis.y),
                         vec_from_basis)

    def scale(self, scalar):
        self.v = self.v.multiply(scalar)
        self._recalculate_basis()

    def rebase(self, base):
        self.basis = base
        self._recalculate_basis()

    def move(self, x, y):
        self.basis.x += x
        self.basis.y += y
        self._recalculate_basis()

    def rotate(self, angle):
        theta = radians(float(angle))
        temp_x = self.v.x
        temp_y = self.v.y
        self.v.x = temp_x * cos(theta) - temp_y * sin(theta)
        self.v.y = temp_y * cos(theta) + temp_x * sin(theta)
        self._recalculate_basis()

    def _recalculate_basis(self):
        self.absolute_x = self.basis.x + self.v.x
        self.absolute_y = self.basis.y + self.v.y


class VectorPolygon:
    points = []
    vectors = []
    basis = None

    def __init__(self, points, basis):
        self.basis = basis
        base = basis

        for point in points:
            v = Vector(point.x, point.y, 1)
            vec = PygameVector(v, base)
            base = Point(vec.absolute_x, vec.absolute_y, 1)
            self.points = points
            self.vectors.append(vec)

    def draw(self, color):
        for vector in self.vectors:
            vector.draw(color)

    def move(self, x, y):

        for vector in self.vectors:
            vector.move(x, y)

    def scale(self, scalar):
        base = self.basis

        for vec in self.vectors:
            vec.rebase(base)
            vec.scale(scalar)
            base = Point(vec.absolute_x, vec.absolute_y, 1)

    def rotate(self, angle):
        base = self.basis

        for vec in self.vectors:
            vec.rebase(base)
            vec.rotate(angle)
            base = Point(vec.absolute_x, vec.absolute_y, 1)


class Cube(VectorPolygon):
    velocity = None

    def __init__(self, size, basis, velocity):
        self.cube = [Point(0, 1, 0),
                     Point(1, 0, 0),
                     Point(0, -1, 0),
                     Point(-1, 0, 0)]

        super().__init__(self.cube, basis)
        self.velocity = velocity
        self.scale(size)

    def update(self):
        self.move(self.velocity.x, self.velocity.y)


class Triangle(VectorPolygon):
    velocity = None

    def __init__(self, size, basis, velocity):
        self.triangle = [Point(1, 0, 0),
                         Point(-1 / 2, 1, 0),
                         Point(0, 0, 0)]

        super().__init__(self.triangle, basis)
        self.velocity = velocity
        self.scale(size)

    def update(self):
        self.move(self.velocity.x, self.velocity.y)


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Linear Algebra")

    clock = pygame.time.Clock()

    v = Vector(100, 100, 0)

    c_base = Point(100, 100, 0)
    t_base = Point(100, 100, 0)

    cube = Cube(10, c_base, Vector(1, 0, 0))
    triangle = Triangle(10, t_base, Vector(-1, 0, 0))

    while True:
        clock.tick(50)

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Clear the screen
        screen.fill((0, 0, 0))

        cube.update()
        triangle.update()
        triangle.draw((255, 255, 255))
        cube.draw((255, 255, 255))
        cube.rotate(-1)

        # Update the screen
        pygame.display.flip()
