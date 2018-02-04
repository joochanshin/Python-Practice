from math import *
from complex import Complex


c1 = Complex(-2, -2)


def z(n, c):
    if n == 0:
        return 0
    else:
        return (z(n-1, c) ** 2) + c


def accept_c(c):
    if abs(z(10, c)) > 2:
        return False
    else:
        return True




