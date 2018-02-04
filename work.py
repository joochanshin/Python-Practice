from math import *
from decimal import *
from complex import Complex


c1 = Complex(-2, 1)


def z(n, c):
    if n == 0:
        return Complex(0, 0)
    else:
        tmp = z(n - 1, c)
        return tmp * tmp + c


def accept_c(c):
    if abs(z(10, c)) > 2:
        return False
    else:
        return True


print accept_c(c1)

for x in range(-2, 3):
    for y in range(-2, 3):
        print accept_c(Complex(x, y))
    print "\n"