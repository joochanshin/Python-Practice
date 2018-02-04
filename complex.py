from math import *
from decimal import *
import cmath

class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getReal(self):
        return self.x

    def getImaginary(self):
        return self.y

    def __add__(self, other):
        x = self.x
        y = self.y
        a = other.getReal()
        b = other.getImaginary()
        return Complex((a + x), ((b + y) ))

    def __sub__(self, other):
        x = self.x
        y = self.y
        a = other.getReal()
        b = other.getImaginary()
        return Complex((a - x), ((b - y) ))
    def __mul__(self, other):
        x = self.x
        y = self.y
        a = other.getReal()
        b = other.getImaginary()
        return Complex(((a * x) - (b * y)), (((a * y) + (b * x)) ))

    def __abs__(self):
        x = self.x
        y = self.y
        return sqrt((Decimal(x) ** 2) + (Decimal(y) ** 2))

    def __str__(self):
        return 'Real: %s \nImag: %s' % (self.x, self.y)
