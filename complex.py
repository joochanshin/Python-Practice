from math import *


class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


z = Complex(5, 5)
print Complex.get_x(z)
print Complex.get_y(z)
