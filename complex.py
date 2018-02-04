from math import *
import cmath

class Complex:
    def __init__(self, x, y):
        self.real = x
        self.imag = y

    def getReal(self):
        return self.real

    def getImaginary(self):
        return self.imag

    def __add__(self, other):
        x = self.x
        y = self.y
        a = other.getReal()
        b = other.getImaginary()
        return (a - x) + ((b - y) * 1j)

    def __sub__(self, other):
        x = self.x
        y = self.y
        a = other.getReal()
        b = other.getImaginary()
        return (a - x) + ((b - y) * 1j)

    def __mult__(self, other):
        x = self.x
        y = self.y
        a = other.getReal()
        b = other.getImaginary()
        return ((a * x) - (b * y)) + (((a * y) + (b * x)) * 1j)

    def __abs__(self):
        x = self.x
        y = self.y
        return (((x ** 2) + (y ** 2)) ** .5)

    def __str__(self):
        return 'Real: %s \nImag: %s' % (self.real, self.imag)

    def __trunc__(self):
        return int(self.real)

z = Complex(5, 5)


